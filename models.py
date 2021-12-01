from app import db
from datetime import datetime
import re
from flask_security import UserMixin, RoleMixin

def slugify(s):
	pattern = r'[^\w+]'
	return re.sub(pattern, '-', s)


class Plat(db.Model):
	time = datetime.utcnow()
	id = db.Column(db.Integer, primary_key=True)
	data_query = db.Column(db.Text)
	date = db.Column(db.DateTime, default=datetime.utcnow())
	# date = db.Column(db.DateTime, default=datetime.utcnow())

	def __repr__(self):
		return '<Последний запрос %r>' %self.data_query


class Block(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	data_query = db.Column(db.Text)
	date = db.Column(db.DateTime, default=datetime.utcnow())

	def __repr__(self):
		return '<Последний запрос %r>' %self.data_query


post_tags = db.Table('post_tags',
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True))


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(140))
	slug = db.Column(db.String(140), unique=True)
	body = db.Column(db.Text)
	created = db.Column(db.DateTime, default=datetime.utcnow())

	def __init__(self, *args, **kwargs):
		super(Post, self).__init__(*args, **kwargs)
		self.generate_slug()

	tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

	def generate_slug(self):
		if self.title:
			self.slug = slugify(self.title)

	def __repr__(self):
		return f'<Post id: {self.id}, title{self.title}'


class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(140))
	slug = db.Column(db.String(140))

	def __init__(self, *args,**kwargs):
		super(Tag, self).__init__(*args,**kwargs)
		self.slug = slugify(self.name)

	def __repr__(self):
		return f'Tag id:{self.id} name:{self.name}'


### flask security ###
roles_users = db.Table('roles_users',
					   db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
					   db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
					   )


class User(db.Model, UserMixin):
	id = db.Column(db.Integer(), primary_key=True)
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(255))
	active = db.Column(db.Boolean())
	roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(100), unique=True)
	discription = db.Column(db.String(255))





