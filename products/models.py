from django.db import models

# Create your models here.
class Product(models.Model):
  product_sku = models.CharField(max_length=50)
  product_type = models.CharField(max_length=2)
  desc = models.CharField(max_length=200)
  product_generation = models.IntegerField(default=0)
  is_pack = models.IntegerField(default=0)
  bundle = models.IntegerField(default=0)
  collection = models.IntegerField(default=0)

  def __str__(self):
    return self.product_sku+str(self.id)

class ProductsBundle(models.Model):
  protection = models.CharField(max_length=50)
  bundler_product = models.ForeignKey(Product,related_name='%(class)s_bundler_product_id',on_delete=models.CASCADE)
  product = models.ForeignKey(Product,related_name='%(class)s_product_id',on_delete=models.CASCADE)
  comment = models.CharField(max_length=50)

  def __str__(self):
    return str(self.bundler_product)+" - "+str(self.product)

