from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Article

from django.core.paginator import paginator
# Create your views here.
def hello_word(request):
	return HttpResponse("hello word")



def article_content(request):
	article = Article.objects.all()[0]
	title = article.title
	brief_content = article.brief_content
	content = article.content
	article_id = article.article_id
	publish_date = article.publish_date
	return_str = 'titleL:%s,brief_content:%s,content:%s,article_id:%s,publish_date:%s' %(title,brief_content,content,article_id,publish_date)

	return HttpResponse(return_str)   




def get_index_page(request):
	page = request.GET.get('page')
	if page:
		page = int(page)
	else:
		page = 1
	print('page param:',page)

	all_article = Article.objects.all()
	return render(request,'blog/index.html',
			{
				'article_list':all_article

			}

		)


def get_detail_page(request,article_id):
	#指定每一个跳转的文章id,取出所有文章匹配id
	# all_article = Article.objects.all()
	# curr_article = None
	# for article in all_article:
	# 	if article.article_id == article_id:
	# 		curr_article = article
	# 		break


	#定义变量
	all_article = Article.objects.all()
	curr_article = None
	previous_index = 0
	next_index = 0
	previous_article = None
	next_article = None  
	#取出文章，enumerate迭代器enumerate(sequence, [start=0]) #sequence -- 一个序列、迭代器或其他支持迭代对象，start -- 下标起始位置。
	for index,article in enumerate(all_article):
		if index == 0:  						#第一篇文章等于0
			previous_index = 0					#第一篇文章的上一篇文章也不存在所以等于0
			next_index = index + 1				#当前文章的下一篇文章就等于index + 1

		elif index == len(all_article) - 1:		#如果index等于最后一篇文章的话，就等于index - 1
			previous_index = index - 1			
			next_index = index
		else:
			previous_index = index - 1			
			next_index = index + 1
		if article.article_id == article_id:
			curr_article = article
			previous_article = all_article[previous_index]  #把上一篇文章和下一篇文章都取出来
			next_article = all_article[next_index]
			break

	section_list = curr_article.content.split('\n')
	return render(request,'blog/detail.html',
		{
			'curr_article':curr_article,
			'section_list':section_list,
			'previous_article':previous_article,		#传递定义的变量
			'next_article':next_article
		}
	)

