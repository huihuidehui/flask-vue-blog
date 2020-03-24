#!/usr/bin/env python
# encoding: utf-8
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import make_response, jsonify

auth_basic = HTTPBasicAuth()
auth_token = HTTPTokenAuth(scheme='Bearer')


@auth_basic.error_handler
def auth_basic_unauthorized():
    return make_response(jsonify({'res': 0, 'message': 'Unauthorized access'}), 401)


@auth_token.error_handler
def auth_basic_unauthorized():
    return make_response(jsonify({'res': 0, 'message': 'Unauthorized access'}), 401)

