# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test,Contact


# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test2 = Contact(name='mo',age='26',email='10@qq.com')
    test1.save()
    test2.save()
    return HttpResponse("<p>数据添加成功！</p>")