#!/usr/bin/env python
# encoding: utf-8
from flask import Flask
from app.model import db, User as UserModel
from app.resources import Article, CategoryList, \
    Category, Tag, TagList, Login, ArticleList, \
    PopularArticles, TagPosts, NewPosts, CategoryPosts, Like, About
from flask_restful import Api
import click
from app.utils.util import FakeData
from app.extensions import bcrypt
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    # 加载配置文件
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.settings')

    # 加载插件
    register_extensions(app)

    # 初始化数据库
    db.init_app(app)
    db.create_all(app=app)

    # 注册api
    register_api(app)
    api = Api(app)
    # 注册命令
    register_commands(app)
    # 解决跨域请求问题
    CORS(app)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    # cache.init_app(app)


def register_commands(app):
    @app.cli.command(help='Reset database.')
    def resetdatabase():  # 重置数据库
        db.drop_all(app=app)
        db.create_all(app=app)
        click.echo('Reset database, successful.')

    @app.cli.command(help='''Initialize the blog Use \'--help\' for more information.''')
    @click.option('-u', prompt=True, help='username')
    @click.option('-p', prompt=True, hide_input=True, confirmation_prompt=True, help='password')
    def init(u, p):
        # 初始化数据库
        db.init_app(app)
        db.create_all(app=app)
        # 新建用户
        new_user = UserModel(name=u, password_hash=UserModel.set_password(p))
        db.session.add(new_user)
        db.session.commit()

        click.echo('Success.')

    @app.cli.command(help='Fake some data.')
    @click.option('-a', prompt=True, help='the number of article.')
    @click.option('-c', prompt=True, help='the number of category.')
    @click.option('-t', prompt=True, help='the number of tag.')
    def fakedata(a, c, t):
        faker = FakeData(article_num=a, category_num=c, tag_num=t)
        faker.make_data()
        click.echo('Fake data,successful.')


def register_api(app):
    """
    注册API
    :param app:
    :return:
    """
    api = Api(app)
    api.add_resource(Article, '/article')
    api.add_resource(ArticleList, '/articles')
    api.add_resource(PopularArticles, "/popularposts")
    api.add_resource(NewPosts, "/newposts")
    api.add_resource(CategoryList, '/categories')
    api.add_resource(Category, '/category')
    api.add_resource(Tag, '/tag')
    api.add_resource(TagList, '/tags')
    api.add_resource(TagPosts, "/tagposts")
    api.add_resource(Login, '/login')
    api.add_resource(CategoryPosts, "/categoryposts")
    api.add_resource(Like, "/likes")
    api.add_resource(About, "/about")
