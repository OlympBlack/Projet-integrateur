# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Friendship(models.Model):
    liker = models.OneToOneField('ZzUsers', models.DO_NOTHING, db_column='liker', primary_key=True)  # The composite primary key (liker, liked, lik) found, that is not supported. The first column is selected.
    liked = models.ForeignKey('ZzUsers', models.DO_NOTHING, db_column='liked', related_name='friendship_liked_set')
    lik = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'friendship'
        unique_together = (('liker', 'liked', 'lik'), ('liker', 'liked', 'lik'),)


class ZzDiscussions(models.Model):
    last_message = models.ForeignKey('ZzMessages', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_discussions'


class ZzHobbys(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'zz_hobbys'


class ZzLangages(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'zz_langages'


class ZzLocations(models.Model):
    user = models.ForeignKey('ZzUsers', models.DO_NOTHING)
    longitude = models.FloatField()
    latitude = models.FloatField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'zz_locations'


class ZzMedias(models.Model):
    path = models.CharField(unique=True, max_length=255)
    type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_medias'


class ZzMessages(models.Model):
    content = models.TextField()
    media = models.ForeignKey(ZzMedias, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ZzUsers', models.DO_NOTHING)
    discussion = models.ForeignKey(ZzDiscussions, models.DO_NOTHING)
    message = models.ForeignKey('self', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'zz_messages'


class ZzUsers(models.Model):
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    pseudo = models.CharField(unique=True, max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    last_connect = models.DateTimeField()
    nom = models.CharField(max_length=255, blank=True, null=True)
    prenom = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField()
    bio = models.TextField(blank=True, null=True)
    sex = models.CharField(max_length=22, blank=True, null=True)
    plage = models.CharField(max_length=2, blank=True, null=True)
    astre = models.CharField(max_length=10, blank=True, null=True)
    religion = models.CharField(max_length=10, blank=True, null=True)
    hobby = models.JSONField(blank=True, null=True)
    pref = models.JSONField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_users'


class ZzUsersDiscussions(models.Model):
    user = models.OneToOneField(ZzUsers, models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, discussion_id) found, that is not supported. The first column is selected.
    discussion = models.ForeignKey(ZzDiscussions, models.DO_NOTHING)
    status = models.IntegerField()
    lastdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_users_discussions'
        unique_together = (('user', 'discussion'), ('user', 'discussion'),)


class ZzUsersLangages(models.Model):
    user = models.OneToOneField(ZzUsers, models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, langage_id, type) found, that is not supported. The first column is selected.
    langage = models.ForeignKey(ZzLangages, models.DO_NOTHING)
    type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'zz_users_langages'
        unique_together = (('user', 'langage', 'type'), ('user', 'langage', 'type'),)


class ZzUsersMedias(models.Model):
    user = models.OneToOneField(ZzUsers, models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, media_id) found, that is not supported. The first column is selected.
    media = models.ForeignKey(ZzMedias, models.DO_NOTHING)
    principal = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_users_medias'
        unique_together = (('user', 'media'), ('user', 'media'),)
