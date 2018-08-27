from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    # publish_time = models.DateField(auto_now=True)  # 创建时自动存储时间
    publish_time = models.DateField(null=True)  # 创建时自动存储时间

    def __str__(self):  # 显示类的实例对象打印出来的效果
        return self.title
