from django.conf.urls import url
from . import views
# regExp ^houssam , houssam$ , '^$'
# (tuple) [list] {'key':'value'} li = {3,4,2} set
app_name = 'home'
urlpatterns = [
    url(r'^$',views.home,name='home'),

]