from peewee import *
from datetime import date

db = MySQLDatabase("spider",host="47.114.188.250",port=3307,user="root",password="changchang00")



class BaseModel(Model):
    class Meta:
        database = db # This model uses the "people.db" database.

class Topic(BaseModel):
    title=CharField()
    content=TextField(default="")
    id=IntegerField(primary_key=True)
    author = CharField()
    create_time=DateTimeField()
    answer_nums=IntegerField(default=0)
    click_nums=IntegerField(default=0)
    parised_nums=IntegerField(default=0)
    jtl=FloatField(default=0.0)
    score=IntegerField(default=0)
    status=CharField()



class Answer(BaseModel):
    topic_id=IntegerField()
    author=CharField()
    content=TextField(default="")
    create_time=DateTimeField()
    parised_nums=IntegerField(default=0) #点赞数

class Author(BaseModel):
    name=CharField()
    id=IntegerField(primary_key=True)
    click_nums=IntegerField(default=0) #访问数
    original_nums=IntegerField(default=0) #原创数
    forward_nums=IntegerField(default=0) #转发数
    rate=IntegerField(default=-1) #排名
    answer_nums=IntegerField(default=0) #评论数
    parised_nums=IntegerField(default=0) #获赞数
    desc=TextField(null=True) #描述
    industry=CharField(null=True) #行业
    location=CharField(null=True) #地点
    follower_nums=IntegerField(default=0) #粉丝数
    following_nums=IntegerField(default=0) #关注数



if __name__=="__main__":
    # grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
    # herb = Person.create(name='Herb', birthday=date(1950, 5, 5))
    db.create_tables([Topic,Answer,Author])