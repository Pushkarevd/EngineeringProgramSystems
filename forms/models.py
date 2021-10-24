from django.db import models
from django.contrib.auth.models import User


class Form(models.Model):
    class PollChoice(models.IntegerChoices):
        BEST = 5
        GOOD = 4
        SATISFACTORILY = 3
        BAD = 2
        VERY_BAD = 1
        TERRIBLE = 0

    # User that complete this form
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)

    # Timestamp of creation
    created_on = models.DateTimeField(auto_now_add=True)

    # Form with choices from 0 to 5
    uni_course = models.IntegerField(choices=PollChoice.choices)
    soft_course = models.IntegerField(choices=PollChoice.choices)
    online_course = models.IntegerField(choices=PollChoice.choices)
    difficulty_of_courses = models.IntegerField(choices=PollChoice.choices)

    # Form with Text input
    hardest_teacher = models.CharField(max_length=20)
    self_opinion = models.CharField(max_length=350, default=None, null=True)
