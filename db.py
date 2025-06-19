from peewee import *

db = SqliteDatabase('videos.db')  

class Video(Model):
    id = AutoField()
    title = CharField()
    thumbnail_path = CharField(null=True)
    video_path = CharField(unique=True)

    class Meta:
        database = db  # This model uses the "videos.db" database.