from django.urls import path
from . import views

urlpatterns = [
    path('regist/requesters', views.regist_requesters),
    path('regist/requesters/add', views.requesters_add),
    path('regist/requesters/edit', views.requesters_edit),
    path('regist/requesters/del', views.requesters_del)

]
