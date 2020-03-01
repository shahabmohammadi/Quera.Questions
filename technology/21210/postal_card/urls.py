from django.conf.urls import url

from postal_card import views

urlpatterns = [
    url('^$', views.introduce, name='introduce_company')
]