#!/usr/bin/env python
# encoding: utf-8
from copy import deepcopy

from flask_restful import reqparse

from app.resources import BaseResource, base_settings


class Like(BaseResource):
    def __init__(self):
        super(Like, self).__init__()

        # 接受的数据类型
        self.parser = reqparse.RequestParser()
    def get(self):
        # 返回所有文章点赞总数
        response_data = deepcopy(self.base_response_data)
        articles = self.requester.get_articles()
        likes_num = 0
        for i in articles:
            likes_num += i.like_num
        response_data['likesNum'] = likes_num
        return response_data, 200


