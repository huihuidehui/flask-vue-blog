#!/usr/bin/env python
# encoding: utf-8
# from app.utils.util import get_time
from sqlalchemy.ext.hybrid import hybrid_property

from . import db
from app.extensions import bcrypt, auth_token
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired, BadSignature
from flask import current_app
from app.extensions import auth_basic
from flask import g
import shortuuid

# 使用特定的字符生成uuid
shortuuid.set_alphabet("0123456789")

tag_article_association_table = db.Table('tag_article_association',
                                         db.Column('tag_id', db.Integer,
                                                   db.ForeignKey('article.id')),
                                         db.Column('article_id', db.ForeignKey('tag.id')
                                                   ))


class About(db.Model):
    __tablename__ = "about"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    test_column = db.Column(db.Text)

    post_time = db.Column(db.DateTime)
    like_num = db.Column(db.Integer, default=0)
    view_num = db.Column(db.Integer, default=0)
    tags = db.relationship('Tag',
                           secondary=tag_article_association_table,
                           back_populates='articles',
                           cascade="all",
                           lazy='dynamic'
                           )
    abstract = db.Column(db.String(80), default="")
    # 文章uuid
    uuid = db.Column(db.String(80), unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', back_populates='articles')

    # 文章图片
    img_url = db.Column(db.String(80), default="")
    # 查询时按照post_time进行排序
    #__mapper_args__ = {"order_by": post_time.desc()}

    @classmethod
    def generate_uuid(cls, title):
        return shortuuid.uuid(name=title)[-8:]

    @hybrid_property
    def tags_ids(self):
        return [i.id for i in self.tags.all()]

    @property
    def tags_list(self):
        return self.tags.all()


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    articles = db.relationship('Article', back_populates='category', lazy="dynamic")


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    articles = db.relationship('Article', secondary=tag_article_association_table, back_populates='tags',
                               lazy='dynamic')


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    password_hash = db.Column(db.String(128))

    @staticmethod
    @auth_basic.verify_password
    def verify_password(username, password):
        """
        验证用户名和密码
        :param username:
        :param password:
        :return:
        """
        user = User.query.filter_by(name=username).first()
        if user is not None:
            if User.validate_password(user.password_hash, password):
                g.user = user
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def set_password(password):
        """
        生成hash序列
        :param password:
        :return:
        """
        return bcrypt.generate_password_hash(password).decode('utf-8')

    @staticmethod
    def validate_password(password_hash, password):
        """
        验证密码是否正确
        :param password_hash:
        :param password:
        :return:
        """
        return bcrypt.check_password_hash(password_hash, password)

    def generate_auth_token(self):
        """
        生成token
        :return:
        """
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=current_app.config['TOKEN_EXPIRATION_TIME'])
        return s.dumps({'id': self.id}).decode('utf-8')  # 返回值是一个二进制的

    @staticmethod
    @auth_token.verify_token
    def verify_auth_token(token):
        """
        验证token是否有效
        :param token:
        :return:
        """
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        user = User.query.get(data['id'])
        return True if user is not None else False
