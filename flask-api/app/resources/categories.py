#!/usr/bin/env python
# encoding: utf-8
from copy import deepcopy

from flask import current_app
from flask_restful import marshal
from app.utils.util import get_values_by_keys
from app.model import Category as CategoryModel
from . import base_settings, BaseResource


class CategoryList(BaseResource):

    def __init__(self):
        super(CategoryList, self).__init__()
        self.fields = base_settings.categories_fields

    def get(self):
        response_data = deepcopy(self.base_response_data)
        categories = self.requester.get_model_all(CategoryModel)
        # 计算每个分类下的文章数
        tmp_data = []
        for category in categories:
            # tmp_data.append(len(category.articles))
            # len(category.articles)
            tmp_data.append({
                "id": category.id,
                "name": category.name,
                "articleNum": len(list(category.articles))
            })
        categories_data = marshal(data=tmp_data, fields=self.fields)  # 使用 marshal 格式化输出字段
        response_data['totalNum'] = len(categories_data)
        response_data['data'] = categories_data
        return response_data, 200


class CategoryPosts(BaseResource):
    def __init__(self):
        super(CategoryPosts, self).__init__()

        # self.parser = reqparse.RequestParser()
        # 接受的数据类型
        # get请求参数
        self.parser.add_argument('page', type=int, location='args')
        self.parser.add_argument('size', type=int, location='args')
        # 用于格式化文章响应
        self.fields = deepcopy(base_settings.article_fields)
        self.fields.pop('content')

    def get(self):
        response_data = deepcopy(self.base_response_data)
        category_id, page, size = get_values_by_keys(self.parser.parse_args(), [
            ('id', -1),
            ('page', current_app.config['DEFAULTPAGE']),
            ('size', current_app.config['DEFAULTSIZE'])
        ])
        response_data = self.make_category_pagination_data(page, size, category_id, response_data)
        return response_data, 200

    def make_category_pagination_data(self, page, size, category_id, data):
        """
        查询分页数据.
        :param category_id:
        :param page: 页数
        :param size: 每页的个数
        :param data: 返回的数据
        :return: data
        """
        pagination_data = self.requester.get_category_pagination(page=page, size=size, category_id=category_id,
                                                                 error_out=False)
        total_pages, articles, article_num = pagination_data.pages, pagination_data.items, pagination_data.total  # 总页数和文章数据,总文章数
        data['totalPage'] = total_pages
        data['currentPage'] = page
        data['articleNum'] = article_num
        data['data'] = marshal(data=articles, fields=self.fields)  # 使用 marshal 格式化输出字段

        return data


class Category(BaseResource):

    def __init__(self):
        super(Category, self).__init__()
        # put/post
        self.parser.add_argument('name', type=str, help='the category name is not exist.')
        # get/post/delete
        self.fields = base_settings.category_fields

    def get(self):
        """
        使用id查询某个分类信息
        :return:
        """

        response_data = deepcopy(self.base_response_data)
        category_id, = get_values_by_keys(self.parser.parse_args(), [('id', -1)])
        res, category = self.requester.get_model_by_id(CategoryModel, category_id)
        if res:
            response_data['data'] = marshal(category, self.fields)
        else:
            response_data['res'] = 0
            response_data['message'] = "the id is invalid."
        return response_data, 200

    def put(self):
        """
        添加一个新的分类
        :return:
        """
        response_data = deepcopy(self.base_response_data)
        category_name, = get_values_by_keys(self.parser.parse_args(), [('name', '全部')])
        res = self.add_new_category(name=category_name)
        if not res:
            response_data['res'] = 0
            response_data['message'] = "the name is invalid"
        return response_data

    def post(self):
        """
        修改分类
        :return:
        """
        response_data = deepcopy(self.base_response_data)
        name, category_id = get_values_by_keys(self.parser.parse_args(), [
            ('name', None), ('id', -1)
        ])
        res = self.modify_category(name, category_id)
        if not res:
            response_data['res'] = 0
            response_data['message'] = "the id or name is invalid."
        return response_data, 200

    def delete(self):
        """
        删除分类,同该分类下的文章一同删除
        :return:
        """
        response_data = deepcopy(self.base_response_data)
        category_id = get_values_by_keys(self.parser.parse_args(), [('id', -1)])
        res = self.delete_data_by_id(CategoryModel, category_id)
        if not res:
            response_data['res'] = 0
            response_data['message'] = "the id is invalid."
        return response_data, 200

    def modify_category(self, name, category_id):
        """

        :param name:
        :param category_id:
        :return: res
        """
        res, category = self.requester.get_model_by_id(CategoryModel, category_id)
        if res:
            # id值有效
            if self.requester.get_model_by_name(CategoryModel, name) is None:
                # 数据库中不存在重名的category
                category.name = name
                self.requester.commit()
                return True
            else:
                # 已存在name为要修改值的分类
                return False
        else:
            # id无效
            return False

    def add_new_category(self, name):
        """
        :param name:
        :return:  res
        """
        if self.requester.get_model_by_name(CategoryModel, name) is not None:
            # 数据库中已存在相同name的分类
            return False
        else:
            new_category = CategoryModel(name=name)
            self.requester.add(new_category)
            self.requester.commit()
            return True
