from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from django.views import View
from goods.models import *


class IndexView(View):
    def get(self, request,cid=2):
        # cid为2代表女装开始
        cid = int(cid)
        # 查询所有类别信息
        categorys = Category.objects.all().order_by('id')
        # 查询当前类别下的全部信息
        goodsList = Goods.objects.filter(category_id=cid).order_by('id')

        return render(request,'index.html',{'category': categorys, 'goodsList': goodsList, 'currentcid':cid})