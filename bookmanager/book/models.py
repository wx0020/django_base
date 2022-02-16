from django.db import models

# Create your models here.

# 模型类 需要继承
# 自动生成id属性
# 添加其他字段
# 字段名 = modes.类型(选项)
class BookInfo(models.Model):
    # id
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + self.book.name