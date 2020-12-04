from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'articles'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:article_id>', views.detail, name = 'detail'),
	# path('image_upload', views.leave_comment, name = 'image_upload'), 
	path('<int:article_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
]
# if settings.DEBUG:
# 	urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
