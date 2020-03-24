#!/usr/bin/env python
# encoding: utf-8
from copy import deepcopy

from flask_restful import marshal

from app.utils.util import get_values_by_keys
from app.resources import BaseResource, base_settings
from app.model import About as AboutModel


class About(BaseResource):
    def __init__(self):
        super(About, self).__init__()

        # self.parser.add_argument('title', type=str)
        self.parser.add_argument('content', type=str)

        self.fields = deepcopy(base_settings.about_fields)

    def get(self):
        response_data = deepcopy(self.base_response_data)

        about_data = self.requester.get_model_all(AboutModel)[0]

        response_data['data'] = marshal(data=about_data, fields=self.fields)
        return response_data, 200

    def post(self):
        response_data = deepcopy(self.base_response_data)
        about_data = self.requester.get_model_all(AboutModel)[0]
        new_content, = get_values_by_keys(self.parser.parse_args(), [("content", about_data.content)])
        about_data.content = new_content
        self.requester.commit()

        return response_data
