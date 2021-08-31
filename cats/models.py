from django.db import models
from django.urls import reverse

# Create your models here.
class Cat(models.Model):
    # null 参数只影响数据库的存储，null=True 表示将空值储存为NULL，默认为False.一般惯例是字符串使用空字符串。
    #  blank=True 与验证相关表示允许表单可以为空,默认是False
    #  choices 选项
    ORANGE = 'OG'
    WHITE = 'WH'
    BLACK = 'BK'
    CATS_COLOR = [
    (ORANGE, 'Orange'),
    (WHITE, 'white'),
    (BLACK, 'black')
    ]
    name = models.CharField(max_length=120)
    age = models.DecimalField(max_digits=5,decimal_places=2)
    color = models.CharField(
        max_length = 2,
        choices = CATS_COLOR,
        default= WHITE
        )
    description = models.TextField(blank=False) #blank=False  means required,
    location = models.TextField(blank=True)
    owner =   models.TextField(default='Welcome our new  family member')

    def get_absolute_url(self):
        # print(reverse('cats:cat_detail'), kwargs={"id":self.id})
        return  reverse("cats:cat_detail", kwargs={"id":self.id})            # f"/cats/{self.id}"