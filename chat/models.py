from django.db import models
from django.contrib.auth.models import User


class DirectMessages(models.Model):
    from_user = models.ForeignKey(User, models.DO_NOTHING, db_column='from_user', related_name='from_user')
    to_user = models.ForeignKey(User, models.DO_NOTHING, db_column='to_user', related_name='to_user')
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class meta:
        db_table = 'direct_messages'


class Groups(models.Model):
    name = models.CharField(max_length=50)
    added_by = models.ForeignKey(User, models.DO_NOTHING, db_column='added_by', related_name='added_by')
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'channels'


class GroupMembers(models.Model):
    group = models.ForeignKey('Groups', models.DO_NOTHING, db_column='group')
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user')
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'group_members'


class GroupMessages(models.Model):
    group = models.ForeignKey('Groups', models.DO_NOTHING, db_column='group')
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user')
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
