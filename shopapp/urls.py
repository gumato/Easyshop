from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search/', views.search, name='search_category'),
    url(r'signup/', views.Signup, name="signup"),
    url(r'^categories/(\d+)/$',views.categories,name='categories'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)