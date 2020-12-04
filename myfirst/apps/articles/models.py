import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
	article_title = models.CharField('Имя блога', max_length = 200)
	article_text = models.TextField('Текст блога')
	pub_date = models.DateTimeField('Дата публикации')

	def __str__(self):
		return self.article_title

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 1))

	class Meta:
		verbose_name = 'Блог'
		verbose_name_plural = 'Блоги'

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField('Имя автора', max_length = 50)
	comment_text = models.CharField('Текст комментария', max_length = 200)
	comment_image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'

# layout = Layout()
# layout.image = "path/st.jpg"
# layout.save()