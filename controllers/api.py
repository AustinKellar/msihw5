def get_posts():
    posts = db(db.post).select()
    return response.json(dict(posts=posts))
