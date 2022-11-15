from flask import Blueprint, render_template, request
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, get_posts_by_user, search_for_posts
import logging
from logs.loggers import logger_viewers

logger_viewers()
logger_main = logging.getLogger('main')

main_bp = Blueprint('main_bp', __name__, template_folder='templates')


@main_bp.route('/')
def page_index():
    posts = get_posts_all()
    logger_main.info(f'Запрос главной страницы')
    return render_template('index.html', posts=posts)


@main_bp.route('/posts/<int:post_id>')
def page_post_id(post_id):
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    count_comments = len(comments)
    logger_main.info(f'Запрос /posts/{post_id}')
    return render_template('post.html', post=post, comments=comments, count=count_comments)


@main_bp.route('/posts/<user_name>')
def page_post_user(user_name):
    post = get_posts_by_user(user_name)
    logger_main.info(f'Запрос /posts/{user_name}')
    return render_template('user-feed.html', posts=post)


@main_bp.route('/search')
def page_search():
    query = request.args.get('s')
    if query and query != '':
        query_post = search_for_posts(query)
        count = len(query_post)
        logger_main.info(f'Запрос /search/{query}')
    return render_template('search.html', posts=query_post, count=count, tag=query)


@main_bp.route('/tag/<tagname>')
def page_tag(tagname):
    posts = search_for_posts(tagname)
    count = len(posts)
    logger_main.info(f'Запрос /tag/{tagname}')
    return render_template('tag.html', posts=posts, count=count, tag=tagname)
