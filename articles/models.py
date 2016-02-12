from django.db import models

# Create your models here.
class ArticleCategory(models.Model):
  name = models.CharField(max_length=200)
  alias = models.CharField(max_length=200)
  description = models.TextField()
  parent = models.ForeignKey("self", null=True, blank=True)

  def __str__(self):
    return self.name

class Article(models.Model):
  title = models.CharField(max_length=200)
  alias = models.CharField(max_length=200)
  category = models.ForeignKey(ArticleCategory,on_delete=models.CASCADE)
  intro = models.TextField()
  content = models.TextField()
  
  def __str__(self):
    return self.alias

