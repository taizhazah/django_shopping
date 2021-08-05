from django.db import models

# Create your models here.


# 类别
class Category(models.Model):
    cname = models.CharField(max_length=10)

    def __str__(self):
        return self.cname


#商品
class Goods(models.Model):
    gname = models.CharField(max_length=100)
    gdesc = models.CharField(max_length=100)
    oldprice = models.DecimalField(max_digits=5,decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.gname


# 商品详情名称
class GoodsDetailName(models.Model):
    gdname = models.CharField(max_length=30)

    def __str__(self):
        return self.gdname


# 详情
class GoodsDetail(models.Model):
    # 上传的图片，设置为空，地址自动拼接
    gdurl = models.ImageField(upload_to='')
    # 外键商品详情名字
    gdname = models.ForeignKey(GoodsDetailName, on_delete=models.CASCADE)
    # 外键商品
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)


# 尺寸表
class Size(models.Model):
    sname = models.CharField(max_length=10)

    def __str__(self):
        return self.sname


# 小图颜色
class Color(models.Model):
    colorname = models.CharField(max_length=10)
    colorurl = models.ImageField(upload_to='color/')

    def __str__(self):
        return self.colorname


# 库存
class Inventory(models.Model):
    count = models.PositiveIntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

