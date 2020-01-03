from django.db import models

# Create your models here.
class Article(models.Model):
	#文章的唯一id
	article_id = models.AutoField(primary_key=True)
	#文章标题
	title = models.TextField()
	#文章的摘要
	brief_content = models.TextField()
	#文章的主要内容  
	content = models.TextField()
	#文章的发布日期
	publish_date = models.DateTimeField(auto_now=True)


	#文章article的，分辨出那一篇文章是那一篇 
	def  __str__(self):
		return self.title