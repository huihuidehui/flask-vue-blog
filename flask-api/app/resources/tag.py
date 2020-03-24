#!/usr/bin/env python
# encoding: utf-8
from copy import deepcopy

from flask import current_app
from flask_restful import marshal, reqparse

from app.utils.util import get_values_by_keys
from app.model import Tag as TagModel
from . import base_settings, BaseResource


class TagList(BaseResource):
    def __init__(self):
        super(TagList, self).__init__()
        self.fields = base_settings.tags_fields

    def get(self):
        response_data = deepcopy(self.base_response_data)

        # response_data['data'] = marshal(self.requester.get_model_all(TagModel), self.fields)
        tags_data = self.requester.get_model_all(TagModel)

        # 计算每个标签下的文章数
        tmp_data = []
        for tag in tags_data:
            tmp_data.append(
                {
                    "id": tag.id,
                    "name": tag.name,
                    "articleNum": len(list(tag.articles))
                }
            )
        tags_data = marshal(tmp_data, self.fields)

        response_data['totalNum'] = len(tags_data)
        response_data['data'] = tags_data
        return response_data, 200


# 某一标签下的文章分页数据
class TagPosts(BaseResource):
    def __init__(self):
        super(TagPosts, self).__init__()

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
        tag_id, page, size = get_values_by_keys(self.parser.parse_args(), [
            ('id', -1),
            ('page', current_app.config['DEFAULTPAGE']),
            ('size', current_app.config['DEFAULTSIZE'])
        ])
        response_data = self.make_tag_pagination_data(page, size, tag_id, response_data)
        return response_data, 200

    def make_tag_pagination_data(self, page, size, tag_id, data):
        """
        查询分页数据.
        :param tag_id:
        :param page: 页数
        :param size: 每页的个数
        :param data: 返回的数据
        :return: data
        """
        pagination_data = self.requester.get_tag_pagination(page=page, size=size, tag_id=tag_id, error_out=False)
        total_pages, articles, article_num = pagination_data.pages, pagination_data.items, pagination_data.total  # 总页数和文章数据
        data['totalPage'] = total_pages
        data['currentPage'] = page
        data["articleNum"] = article_num
        data['data'] = marshal(data=articles, fields=self.fields)  # 使用 marshal 格式化输出字段

        return data


class Tag(BaseResource):

    def __init__(self):
        super(Tag, self).__init__()
        self.parser.add_argument('name', type=str, help="the tag's name is invalid.")
        self.fields = base_settings.tag_fields

    def get(self):
        """
        获取指定id所对应的tag信息
        :return:
        """
        response_data = deepcopy(self.base_response_data)
        tag_id = get_values_by_keys(self.parser.parse_args(), [('id', -1)])
        res, tag = self.requester.get_model_by_id(TagModel, tag_id)
        if res:
            response_data['data'] = marshal(tag, fields=self.fields)
        else:
            response_data['res'] = 0
            response_data['message'] = "the id is invalid."
        return response_data, 200

    def put(self):
        response_data = deepcopy(self.base_response_data)
        tag_name, = get_values_by_keys(self.parser.parse_args(), [('name', '全部')])

        res = self.add_new_tag(tag_name)
        if not res:
            response_data['res'] = 0
            response_data['message'] = "the name is invalid."
        return response_data, 200

    def add_new_tag(self, name):
        """
        添加新的标签
        :param name:
        :return: res
        """
        if self.requester.get_model_by_name(TagModel, name) is None:
            # 指定name值有效
            new_tag = TagModel(name=name)
            self.requester.add(new_tag)
            self.requester.commit()
            return True
        else:
            # 指定的name值在数据库中已经存在
            return False

    def post(self):
        """
        修改指定id对应的tag的name
        :return:
        """
        response_data = deepcopy(self.base_response_data)
        tag_id, tag_name = get_values_by_keys(self.parser.parse_args(), [
            ('id', -1), ('name', None)
        ])

        res = self.modify_tag(tag_id, tag_name)
        if not res:
            response_data['res'] = 0
            response_data['message'] = "the id or name is invalid."
        return response_data, 200

    def modify_tag(self, tag_id, tag_name):
        """

        :param tag_id:
        :param tag_name:
        :return: res
        """
        res, tag = self.requester.get_model_by_id(TagModel, tag_id)
        if res:
            # 指定id值有效
            if self.requester.get_model_by_name(TagModel, tag_name) is None:
                # 指定name值有效
                tag.name = tag_name
                self.requester.commit()
                return True
            else:
                # 指定name值在数据库中已经存在
                return False
        else:
            # 指定id值无效
            False

    def delete(self):
        response_data = deepcopy(self.base_response_data)
        tag_id = get_values_by_keys(self.parser.parse_args(), [('id', -1)])
        res = self.delete_data_by_id(TagModel, tag_id)
        if not res:
            response_data['res'] = 0
            response_data['message'] = "the id is invalid."
        return response_data, 200
