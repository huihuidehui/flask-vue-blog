#!/usr/bin/env python
# encoding: utf-8
from copy import deepcopy

import flask_restful
from flask_restful import fields
from werkzeug.exceptions import HTTPException
from flask import abort as original_flask_abort


class BaseSettings(object):
    def __init__(self):
        # 过滤标签的字段
        self.tags_fields = {
            'name': fields.String(attribute='name'),
            'tagId': fields.Integer(attribute='id'),
            "articleNum": fields.Integer
        }

        self.about_fields = {
            "content": fields.String
        }

        self.article_fields = {
            'title': fields.String,
            'content': fields.String,
            # 重命名属性，在查询到的Article对象中找到'like_num'属性，并以'likeNum'返回出去。
            'likeNum': fields.Integer(attribute='like_num'),
            'viewNum': fields.Integer(attribute='view_num'),
            'postTime': fields.DateTime(attribute='post_time', dt_format='rfc822'),
            'abstract': fields.String(attribute='abstract'),
            'id': fields.Integer(attribute='id'),
            'uuid': fields.String(attribute="uuid"),
            'imgUrl': fields.String(attribute='img_url'),
            'category': fields.String(attribute='category.name'),
            'categoryId': fields.Integer(attribute='category.id'),
            'tags': fields.Nested(self.tags_fields, attribute='tags_list'),
        }

        self.tag_fields = {
            'name': fields.String(attribute='name'),
            'tagId': fields.Integer(attribute='id'),
            # 'articles': fields.Nested(self.article_fields)
        }
        # 用于过滤单个分类的字段
        self.category_fields = {
            'name': fields.String,
            'id': fields.Integer
            # 'articles': fields.Nested(self.article_fields, attribute="articles")
        }
        # 用于多个分类的字段
        self.categories_fields = {
            'name': fields.String(attribute='name'),
            'id': fields.Integer,
            'articleNum': fields.Integer
            # "articles": fields.Nested(self.article_fields)
        }
        # 所有请求的默认响应
        self.base_response_data = {
            'res': 1,
            'message': 'successful',
        }

    def __repr__(self):
        return 'Api 共有的一些设置.'


# 对flask-restful的一些基本设置
class ModifyFramework(object):

    def __init__(self):
        pass

    @classmethod
    def abort(cls, http_status_code, **kwargs):
        """Raise a HTTPException for the given http_status_code. Attach any keyword
        arguments to the exception for later processing.
        用于覆盖原flask-restful中的abort，从而实现自定义参数验证错误信息。
        """
        try:
            original_flask_abort(http_status_code)
        except HTTPException as e:
            if len(kwargs):
                e.data = cls._make_parameter_error_response(http_status_code=e.code, data=kwargs)
            raise

    @classmethod
    def _make_parameter_error_response(cls, http_status_code, data):
        response_data = deepcopy(BaseSettings().base_response_data)
        response_data['message'] = response_data['message'] if data.get('message') is None else data.get('message')
        response_data['res'] = 0 if http_status_code == 400 else 1
        return response_data

    @classmethod
    def apply(cls):
        flask_restful.abort = ModifyFramework.abort  # 覆盖flask-restful原有的abort
