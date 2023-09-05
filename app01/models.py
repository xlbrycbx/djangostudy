from django.db import models

# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=32)
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    name = models.CharField(max_length=16,verbose_name='姓名')
    password = models.CharField(max_length=64,verbose_name='密码')
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='账户余额',default=0)
    create_time = models.DateField(verbose_name='创建日期')

    depart=models.ForeignKey(to='Department',to_field='id',null=True,blank=True,on_delete=models.SET_NULL,
                             verbose_name='部门')
    gender_choices = (
        (1,'男'),(0,'女')
    )
    gender = models.SmallIntegerField(choices=gender_choices,verbose_name='性别')

class PrettyNum(models.Model):
    mobileNo = models.CharField(max_length=11,verbose_name='phone number')
    price = models.IntegerField(verbose_name='price',default=0)
    level_choices = (
        (1,'level 1'),
        (2, 'level 2'),
        (3, 'level 3'),
        (4, 'level 4')
    )
    level = models.SmallIntegerField(verbose_name='chocie',choices=level_choices,default=1)

    status_choices = (
        (1, 'occupied'),
        (2, 'unoccupied')
    )
    status = models.SmallIntegerField(verbose_name='status',choices=status_choices,default=2)