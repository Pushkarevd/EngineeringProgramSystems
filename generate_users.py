import random
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from forms.models import Form


def generate_users():

    teachers = [
        'Клеменков',
        'Штенников',
        'Лисицина',
        'Балакшин'
    ]
    user_sample = "test"
    user_mail_sample = "@mail.ru"

    password = 'Neverno1trol'

    # Create 1000 users
    for i in range(1000):
        user = User.objects.filter(username=f'test{i + 5}')
        form = Form.objects.create(
            author=user.get(),
            created_on=datetime.now() + timedelta(days=random.randint(-20, 20)),
            uni_course=random.randint(0, 5),
            soft_course=random.randint(0, 5),
            online_course=random.randint(0, 5),
            difficulty_of_courses=random.randint(1, 5),
            hardest_teacher=random.choice(teachers),
            self_opinion=""
        )

        print(f'Form {i + 5} is created')