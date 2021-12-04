from flask import Blueprint
from flask import render_template, redirect, request, url_for
from models import Post, Tag
from app import db
from .forms import PostForms

from flask_security import login_required
posts = Blueprint('posts',__name__, template_folder='templates')


@posts.route('/create')
# @login_required
def create_post():
	form = PostForms()
	return render_template('posts/create_posts.html', form=form)


@posts.route('/<slug>/edit/', methods=['post','get'])
# @login_required
def edit_post(slug):
	post = Post.query.filter(Post.slug==slug).first()
	if request.method=='POST':
		form = PostForms(formdata=request.form, obj=post)
		form.populate_obj(post)
		db.session.commit()
		return redirect(url_for('posts.post_detail', slug=post.slug))

	form = PostForms(obj=post)
	return render_template('posts/edit_post.html', post=post, form=form)


@posts.route('/')
def posts_index():
	# p = Post.query.all()
	page = request.args.get('page')
	if page and page.isdigit():
		page = int(page)
	else:
		page = 1

	p = Post.query.order_by(Post.created.desc())#all()
	pages = p.paginate(page=page, per_page=3)

	return render_template('posts/index.html', posts=p, pages=pages)


@posts.route('/<slug>')
def post_detail(slug):
	post = Post.query.filter(Post.slug==slug).first()
	print(type(post))
	tags = post.tags
	print(tags)
	return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/create', methods=['post', 'get'])
def post_create():
	return render_template('posts/create_posts.html')


@posts.route('/created', methods=['post', 'get'])
def post_created():
	title = request.form.get('title')
	body = request.form.get('body')
	# tag = request.form.get('tag')

	try:
		# t = Tag(name=tag)
		p = Post(title=title, body=body)
		db.session.add(p)
		# db.session.add(t)
		db.session.commit()
		return redirect(url_for('posts.posts_index'))
	except:
		return r'ошибка базы данных'


@posts.route('/tag/<slug>', methods=['get'])
def tags_detail(slug):
	tag = Tag.query.filter(Tag.slug==slug).first()
	posts = tag.posts.all()
	return render_template('posts/tag_detail.html', posts=posts, tag=tag)


@posts.route('/search', methods=['get', 'post'])
def search():
	search_word = request.form.get('search_word')
	posts = Post.query.filter(Post.title.contains(search_word)|Post.body.contains(search_word)).all()
	amount = len(posts)
	return render_template('posts/search.html', search_word=search_word, posts=posts, anount=amount)

