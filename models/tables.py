import datetime

def get_user_email():
    return None if auth.user == None else auth.user.email

def get_current_time():
    return datetime.datetime.utcnow()

db.define_table('post',
                Field('post_author', default=get_user_email()),
                Field('post_content', 'text'),
                Field('post_date', 'datetime', default=get_current_time()),
                Field('post_location', 'integer')
                )
