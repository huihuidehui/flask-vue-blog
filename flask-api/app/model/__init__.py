#!/usr/bin/env python
# encoding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.model.models import Article, Category, Tag, User, About
