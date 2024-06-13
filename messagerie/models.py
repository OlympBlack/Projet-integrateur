from django.db import models

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
    longitude = models.FloatField()
    latitude = models.FloatField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    hobby = models.JSONField(blank=True, null=True)
    pref = models.JSONField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_users'

class Friendship(models.Model):
    liker = models.OneToOneField('ZzUsers', models.DO_NOTHING, db_column='liker', primary_key=True)  # The composite primary key (liker, liked, lik) found, that is not supported. The first column is selected.
    liked = models.ForeignKey('ZzUsers', models.DO_NOTHING, db_column='liked', related_name='friendship_liked_set')
    lik = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'friendship'
        unique_together = (('liker', 'liked', 'lik'), ('liker', 'liked', 'lik'),)

class ZzMedias(models.Model):
    path = models.CharField(unique=True, max_length=255)
    type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_medias'

class ZzDiscussions(models.Model):
    last_message = models.ForeignKey('ZzMessages', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_discussions'
        
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

class ZzUsersDiscussions(models.Model):
    user = models.OneToOneField(ZzUsers, models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, discussion_id) found, that is not supported. The first column is selected.
    discussion = models.ForeignKey(ZzDiscussions, models.DO_NOTHING)
    status = models.IntegerField()
    lastdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_users_discussions'
        unique_together = (('user', 'discussion'), ('user', 'discussion'),)

class ZzUsersMedias(models.Model):
    user = models.OneToOneField(ZzUsers, models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, media_id) found, that is not supported. The first column is selected.
    media = models.ForeignKey(ZzMedias, models.DO_NOTHING)
    principal = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz_users_medias'
        unique_together = (('user', 'media'), ('user', 'media'),)
