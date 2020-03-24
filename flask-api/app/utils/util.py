#!/usr/bin/env python
# encoding: utf-8
import datetime
from faker import Faker
from app.model import Article, Category, Tag, db
import random


# 获取时间
def get_time():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=8)


# 根据时间戳返回datetime对象
def get_datetime(time_stamp):
    """
    根据时间戳返回datetime对象
    :param time_stamp: 时间戳
    :return: datetime
    """
    return datetime.datetime.utcfromtimestamp(time_stamp)


def get_values_by_keys(dict_data, keys_defaults):
    """

    :param dict_data: 字典数据
    :param keys_defaults: 列表形式可以指定多个key值，可以使用（key,default）的形式指定默认值
    :return: list
    """
    res = []
    for key_default in keys_defaults:
        if type(key_default) == str:
            res.append(dict_data.get(key_default))
        else:
            key, default = key_default
            data = dict_data.get(key)
            if data is None:
                res.append(default)
            else:
                res.append(data)
    return res


class FakeData(object):
    def __init__(self, article_num=100, category_num=10, tag_num=10):
        """

        :param article_num: 生成的文章个数
        :param category_num: 生成的分类个数
        :param tag_num: 生成的标签个数
        """
        self.article_num = int(article_num)
        self.category_num = int(category_num)
        self.tag_num = int(tag_num)

        self.articles = []
        self.categories = []
        self.tags = []

        self.blog_fake = Faker('zh_CN')

    def make_data(self):
        # self.articles = self._make_article()
        self._make_article()
        self._make_category()
        self._make_tag()
        self._make_relationship()
        db.session.commit()

    def _make_article(self):
        for i in range(self.article_num):
            title = self.blog_fake.text()[:8]
            content = self.blog_fake.text()
            abstract = self.blog_fake.text()[:16]
            like_num = self.blog_fake.random_int()
            view_num = self.blog_fake.random_int()
            post_time = self.blog_fake.date_time()
            # print(title)
            post_uuid = Article.generate_uuid(title)
            new_post = Article(title=title,
                               content=content,
                               abstract=abstract,
                               like_num=like_num,
                               post_time=post_time,
                               uuid=post_uuid,
                               view_num=view_num,
                               img_url="https://s1.ax1x.com/2020/03/24/8bg3oF.png"
                               )

            db.session.add(new_post)
            self.articles.append(new_post)

    def _make_category(self):
        # self.categories.append(Category(name='全部'))
        categories_names = set()
        while len(categories_names) < self.category_num:
            categories_names.add(self.blog_fake.word())

        for name in categories_names:
            new_category = Category(name=name)
            self.categories.append(new_category)
            db.session.add(new_category)

    def _make_tag(self):
        tags_names = set()
        while len(tags_names) < self.tag_num:
            tags_names.add(self.blog_fake.word())
        for name in tags_names:
            new_tag = Tag(name=name)
            self.tags.append(new_tag)
            db.session.add(new_tag)

    def _make_relationship(self):
        # self.articles
        print("*" * 100)
        print("开始虚拟关系")
        print("*" * 100)
        for tag in self.tags:
            # 从生成的文章中随机取出30%
            tmp_articles_index = [random.randint(0, self.article_num - 1) for i in range(int(0.3 * self.article_num))]
            # print(tmp_articles_index)
            tmp_articles = [self.articles[i] for i in tmp_articles_index]
            tag.articles = tmp_articles

        # for article in self.categories:
        for category in self.categories:
            tmp_articles_index = [random.randint(0, self.article_num - 1) for i in range(int(0.3 * self.article_num))]
            tmp_articles = [self.articles[i] for i in tmp_articles_index]
            category.articles = tmp_articles
