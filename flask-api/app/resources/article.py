#!/usr/bin/env python
# encoding: utf-8
from copy import deepcopy
from flask_restful import reqparse, marshal
from app.utils.util import get_time, get_values_by_keys, get_datetime
from app.model import Article as ArticleModel, Category as CategoryModel, Tag as TagModel
from flask import current_app
from app.resources import BaseResource, base_settings


# 最新文章
class NewPosts(BaseResource):
    def __init__(self):
        super(NewPosts, self).__init__()
        self.parser = reqparse.RequestParser()
        # 请求的热门文章的个数
        self.parser.add_argument('count', type=int, location="args")
        # 用于格式化文章的响应
        self.fields = deepcopy(base_settings.article_fields)
        # 除去文章内容
        self.fields.pop('content')

    def get(self):
        response_data = deepcopy(self.base_response_data)
        count, = get_values_by_keys(self.parser.parse_args(), [
            ('count', current_app.config["DEFAULTCOUNT"])
        ])
        articles = self.requester.get_new_posts(ArticleModel, count=count)
        response_data['data'] = marshal(data=articles, fields=self.fields)
        return response_data, 200


# 热门文章
class PopularArticles(BaseResource):
    def __init__(self):
        super(PopularArticles, self).__init__()
        self.parser = reqparse.RequestParser()
        # 请求的热门文章的个数
        self.parser.add_argument('count', type=int, location="args")
        # 用于格式化文章的响应
        self.fields = deepcopy(base_settings.article_fields)
        # 除去文章内容
        self.fields.pop('content')

    def get(self):
        response_data = deepcopy(self.base_response_data)
        count, = get_values_by_keys(self.parser.parse_args(), [
            ('count', current_app.config["DEFAULTCOUNT"])
        ])
        articles = self.requester.get_popular_posts(ArticleModel, count=count)
        response_data['data'] = marshal(data=articles, fields=self.fields)
        return response_data, 200


class ArticleList(BaseResource):
    def __init__(self):
        super(ArticleList, self).__init__()

        # 接受的数据类型
        self.parser = reqparse.RequestParser()
        # get请求参数
        self.parser.add_argument('page', type=int, location='args')
        self.parser.add_argument('size', type=int, location='args')
        # 用于格式化文章响应
        self.fields = deepcopy(base_settings.article_fields)
        self.fields.pop('content')

    def get(self):
        response_data = deepcopy(self.base_response_data)
        page, size = get_values_by_keys(self.parser.parse_args(), [
            ('page', current_app.config['DEFAULTPAGE']),
            ('size', current_app.config['DEFAULTSIZE'])
        ])
        response_data = self.make_pagination_data(page, size, response_data)
        return response_data, 200

    def make_pagination_data(self, page, size, data):
        """
        查询分页数据.
        :param page: 页数
        :param size: 每页的个数
        :param data: 返回的数据
        :return: data
        """
        pagination_data = self.requester.get_pagination(page, size, error_out=False)
        total_pages, articles, total_articles_num = pagination_data.pages, pagination_data.items, pagination_data.total  # 总页数和文章数据
        data['totalPage'] = total_pages
        data['currentPage'] = page
        data['totalNum'] = total_articles_num
        data['data'] = marshal(data=articles, fields=self.fields)  # 使用 marshal 格式化输出字段

        return data


class Article(BaseResource):

    def __init__(self):
        super(Article, self).__init__()

        # post/put请求参数
        self.parser.add_argument('title', type=str)
        self.parser.add_argument('content', type=str)
        self.parser.add_argument('likeNum', type=int)
        self.parser.add_argument('category', type=str)
        self.parser.add_argument('tags', type=str, action='append')
        self.parser.add_argument("viewNum", type=int)
        self.parser.add_argument('abstract', type=str)
        self.parser.add_argument("postTime", type=int)
        self.parser.add_argument('uuid', type=str),
        self.parser.add_argument('coverImgUrl', type=str)
        # 用于过滤文章响应数据
        self.fields = deepcopy(base_settings.article_fields)

    def get(self):
        # 响应数据
        response_data = deepcopy(self.base_response_data)

        # 从请求中查询参数
        article_uuid, = get_values_by_keys(self.parser.parse_args(), [('uuid', '-1')])
        res, article = self.requester.get_model_by_uuid(ArticleModel, article_uuid)
        if res:  # 查找成功
            response_data['data'] = marshal(data=article, fields=self.fields)
        else:
            response_data['res'] = 0
            response_data['message'] = 'the uuid is invalid.'
        return response_data, 200

    def put(self):
        response_data = deepcopy(self.base_response_data)

        # 从parser中获取提交的数据，如果提交的数据没有通过验证将自动返回错误信息。
        title, content, abstract, c_name, t_names, like_num, view_num, post_time, cover_img_url = get_values_by_keys(
            self.parser.parse_args(), [
                'title', 'content', 'abstract', 'category', 'tags', ('likeNum', 0), ('viewNum', 0), ("postTime", None),
                ("coverImgUrl", "")
            ])  # tags 为列表，其余为字符串
        res, new_post = self.build_article(title=title, content=content, abstract=abstract,
                                           c_name=c_name, t_names=t_names,
                                           like_num=like_num, view_num=view_num,
                                           post_time=post_time,
                                           img_url=cover_img_url
                                           )
        if res:
            self.requester.add(new_post)
            self.requester.commit()
        else:
            response_data['res'] = 0
            response_data['message'] = "error"

        return response_data, 201

    def post(self):
        response_data = deepcopy(self.base_response_data)
        # 从parser中获取提交的数据，如果提交的数据没有通过验证将自动返回错误信息。
        args = self.parser.parse_args()
        article_id, = get_values_by_keys(args, [('id', -1)])

        # 根据id查找文章
        res, article = self.requester.get_model_by_id(ArticleModel, article_id)
        if res:
            # 更新文章
            self.update_article(article, args)
        else:
            response_data['res'] = 0
            response_data['message'] = 'the id is invalid.'

        return response_data, 201

    def delete(self):
        response_data = deepcopy(self.base_response_data)
        # 从parser中获取提交的数据，如果提交的数据没有通过验证将自动返回错误信息。
        # 返回值是一个列表，所有加','解包
        article_uuid, = get_values_by_keys(self.parser.parse_args(), [('uuid', -1)])

        res = self.delete_data(ArticleModel, article_uuid)

        if not res:
            response_data['res'] = 0
            response_data['message'] = 'the id is invalid.'
        return response_data, 200

    def update_article(self, article, data):
        """
        修改文章
        :param article: 数据库查询的article
        :param data: 需要更新的数据
        :return: None
        """

        # 处理原文章没有标签添加标签时出错的问题
        if article.tags.all() is None:
            origin_tag_name_list = None
        else:
            origin_tag_name_list = [tag.name for tag in article.tags.all()]
        # 处理原文章没有分类时添加分类出错的问题
        if article.category is None:
            origin_category_name = None
        else:
            origin_category_name = article.category.name
        title, content, abstract, like_num, c_name, t_names, view_num, post_time, img_url = get_values_by_keys(data, [
            ('title', article.title), ('content', article.content), ('abstract', article.abstract),
            ('likeNum', article.like_num),
            ('category', origin_category_name), ('tags', origin_tag_name_list),
            ('viewNum', article.view_num),
            ('postTime', article.post_time),
            ("coverImgUrl", article.img_url)
        ])
        try:
            post_uuid = article.uuid
            if title is not article.title:  # title值被修改需要重新生成uuid
                post_uuid = ArticleModel.generate_uuid(title)
            article.uuid = post_uuid
            article.title = title
            article.content = content
            article.abstract = abstract
            article.like_num = like_num
            article.category = self.requester.get_model_by_name(CategoryModel, c_name)
            article.tags = self.requester.get_model_by_names(TagModel, t_names)
            article.view_num = view_num
            article.img_url = img_url
            # 更新发布时间时需要将前端传来的时间戳转化为datetime对象
            if type(post_time) is int:
                post_time = get_datetime(int(post_time))
            article.post_time = post_time

            self.requester.commit()
            return True
        except:
            return False

    def build_article(self, title, content, abstract, c_name, t_names, img_url="", post_time=None, like_num=0,
                      view_num=0):
        """
        构建文章
        :param img_url:
        :param abstract:
        :param view_num:
        :param post_time:
        :param like_num:
        :param title: 标题
        :param content: 内容
        :param c_name: 分类名
        :param t_names: 标签名
        :return: 状态码，new post
        """
        if post_time is None:
            post_time = get_time()
        else:
            post_time = get_datetime(int(post_time))
        try:
            category = self.requester.get_model_by_name(CategoryModel, name=c_name)
            tags = self.requester.get_model_by_names(TagModel, names=t_names)
            # 添加uuid
            uuid = ArticleModel.generate_uuid(title)
            new_post = ArticleModel(title=title, content=content, abstract=abstract,
                                    like_num=like_num, post_time=post_time,
                                    category=category, tags=tags, uuid=uuid, view_num=view_num, img_url=img_url)
        except:
            return False, None
        return True, new_post
