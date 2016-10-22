from app.auth.models import User
from app import db


def generate_username(first, last):
    user_name = last[:5] + first[0]
    user_count = User.query.filter(User.username.like('%' + user_name + '%')).count()

    "%02d" % (user_count,)

    if user_count == 0:
        user_count += 1

    return last[:5] + first[0] + "%02d" % (user_count,)
