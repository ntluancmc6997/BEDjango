from django.urls import path
from . import views

urlpatterns = [
    path('regist/requesters', views.regist_requesters),
    path('request/add', views.add_request),
    path('request/update', views.update_request),
    path('request/delete', views.delete_request)
]
