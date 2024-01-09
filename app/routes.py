from app import app
from my_data.posts import car_data

@app.route("/")
def hello_world():
    first_name = "Steve"
    last_name = "Agboola"
    return f'Hello From: {first_name} {last_name}'

@app.route('/posts')
def get_posts():
    posts = car_data
    return posts

@app.route('/posts/<post_model>')
def get_post(post_model):
    posts = car_data
    for post in posts:
        if post['model'] == post_model:
            return post
    return {'error': f'Post with model {post_model} does not exist'}, 404