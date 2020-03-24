#!/usr/bin/env python
# encoding: utf-8

# 与数据库请求相关的方法
from sqlalchemy import func
from app.model import db, Category, Article, Tag
from flask import g


class DatabaseRequest(object):
    def __init__(self):
        pass

    @staticmethod
    def get_articles():
        return Article.query.all()

    @staticmethod
    def get_new_posts(model, count):
        """

        :param model:
        :param count:
        :return:
        """
        res = model.query.all()
        if len(res) > count:
            return res[:count]
        else:
            return res

    @staticmethod
    def get_popular_posts(model, count):
        """

        :param model:
        :param count:
        :return:
        """
        res = model.query.order_by(model.view_num).all()
        # print(type(len(res)))
        if len(res) > count:
            return res[-count:]
        else:
            return res

    @staticmethod
    def get_token():
        return g.user.generate_auth_token()

    def get_articles_by_tag_id(self, tag_id):
        """

        :param tag_id:
        :return:
        """
        return Article.query.order_by(Article.post_time.desc()).filter_by(id=tag_id).all()

    def get_model_all(self, model):
        """

        :param model:
        :return:
        """
        return model.query.all()

    @staticmethod
    def get_pagination(page, size, error_out):
        """

        :param page: 页码
        :param size: 每页的数据
        :param error_out: 不清楚
        :return:
        """
        data = Article.query.order_by(Article.post_time.desc()).paginate(
            page=page,
            per_page=size,
            error_out=False)  # 从数据库中按时间顺序获取数据
        # self.pagination_data = data
        return data

    @staticmethod
    def get_tag_pagination(page, size, tag_id, error_out):
        """

        :param tag_id:
        :param page: 页码
        :param size: 每页的数据
        :param error_out: 不清楚
        :return:
        """
        data = Tag.query.get(tag_id).articles.paginate(page=page, per_page=size, error_out=False)
        return data

    @staticmethod
    def get_category_pagination(page, size, category_id, error_out):
        """

        :param page:
        :param size:
        :param category_id:
        :param error_out:
        :return:
        """
        data = Category.query.get(category_id).articles.paginate(page=page, per_page=size, error_out=False)
        return data

    @staticmethod
    def add(data):
        db.session.add(data)

    @staticmethod
    def commit():
        db.session.commit()

    @staticmethod
    def delete(data):
        db.session.delete(data)

    @staticmethod
    def get_model_by_id(model, model_id):
        """
        使用model_id在model中查找数据. model_id不可为空
        :param model:
        :param model_id:
        :return:
        """
        data = model.query.get(model_id)
        return (False, None) if data is None else (True, data)

    @staticmethod
    def get_model_by_uuid(model, model_uuid):
        """
        使用model_id在model中查找数据. model_id不可为空
        :param model_uuid:
        :param model:
        :return:
        """
        data = model.query.filter_by(uuid=model_uuid).first()
        return (False, None) if data is None else (True, data)

    @staticmethod
    def get_model_by_name(model, name):
        """

        :param model:
        :param name:
        :return:
        """
        return model.query.filter_by(name=name).first()

    @staticmethod
    def get_model_by_names(model, names):
        if names is None:
            names = []
        return model.query.filter(model.name.in_(names)).all()
