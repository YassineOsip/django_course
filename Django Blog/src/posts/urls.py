from django.conf.urls import url
from . import views
from django.conf.urls.static import static
# regExp ^houssam , houssam$ , '^$'
# (tuple) [list] {'key':'value'} li = {3,4,2} set
app_name = 'posts'
urlpatterns = [
    url(r'^$',views.posts, name="posts"),

] 