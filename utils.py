import json
from json import JSONDecodeError


def read_json(file_name):
    """
    получает имя JSON файла, считывает файл
    и возвращает список словарей
    """
    try:
        with open(file_name, 'r', encoding='UTF-8') as read_file:
            return json.load(read_file)
    except FileNotFoundError:
        return
    except JSONDecodeError:
        return

def get_posts_all():
    """
    возвращает посты
    """
    return read_json('data/posts.json')


def get_posts_by_user(user_name):
    """
    Возвращает посты определенного пользователя.
    """
    error = True
    all_post = get_posts_all()
    user_post = []
    for post in all_post:
        if post["poster_name"] == user_name:
            user_post.append(post)
            error = False
    if error:
        raise ValueError(f'пользователь {user_name} не найден')
    return user_post


def get_comments_by_post_id(post_id):
    """
    Возвращает комментарии определенного поста.
    """
    all_comments = read_json('data/comments.json')
    comments_list = []

    error = True
    for comment in all_comments:
        if comment["post_id"] == post_id:
            comments_list.append(comment)
            error = False
    if error:
        raise ValueError(f'пост {post_id} отсутствует')
    else:
        return comments_list


def search_for_posts(query):
    """
    Возвращает список постов по ключевому слову
    """
    all_posts = get_posts_all()
    user_post = []
    for post in all_posts:
        if query in post["content"]:
            user_post.append(post)
    return user_post


def get_post_by_pk(pk):
    """
    Возвращает один пост по его идентификатору
    """
    all_post = get_posts_all()
    for post in all_post:
        if post["pk"] == pk:
            return post





