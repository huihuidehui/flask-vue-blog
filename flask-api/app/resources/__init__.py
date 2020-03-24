#!/usr/bin/env python
# encoding: utf-8
from copy import deepcopy

from flask_restful import Resource, reqparse
from app.utils.requestdata import DatabaseRequest
from app.extensions import auth_token
from app.resources.settings import ModifyFramework, BaseSettings


class BaseResource(Resource):
    method_decorators = {'delete': [auth_token.login_required],
                         'post': [auth_token.login_required],
                         'put': [auth_token.login_required]
                         }  # 加入权限管理

    def options(self):
        return {'Allow': '*'}, 200, {'Access-Control-Allow-Origin': '*',
                                     'Access-Control-Allow-Methods': 'HEAD, OPTIONS, GET, POST, DELETE, PUT',
                                     'Access-Control-Allow-Headers': 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild',
                                     }

    def __init__(self):
        self.base_response_data = deepcopy(base_settings.base_response_data)
        # 接受的数据类型
        self.parser = reqparse.RequestParser()
        # delete/post/get请求参数
        self.parser.add_argument('id', type=int)
        self.fields = None  # 过滤响应的字段
        # 请求数据库的对象
        self.requester = DatabaseRequest()

    def delete_data_by_id(self, model, model_id):
        """

        :param model:
        :param model_id:
        :return:
        """
        res, data = self.requester.get_model_by_id(model, model_id)
        if res:
            self.requester.delete(data)
            self.requester.commit()
            return True
        else:
            return False

    def delete_data(self, model, model_uuid):
        """
        根据model id在数据库中删除对应的数据
        :param model:
        :param model_id:
        :return: res
        """
        res, data = self.requester.get_model_by_uuid(model, model_uuid)
        if res:
            self.requester.delete(data)
            self.requester.commit()
            return True
        else:
            return False


ModifyFramework.apply()  # 应用对框架的修改
base_settings = BaseSettings()
from .categories import CategoryList, Category, CategoryPosts
from .article import Article, ArticleList, PopularArticles, NewPosts
from .tag import Tag, TagList, TagPosts
from .login import Login
from .like import Like
from .about import About
