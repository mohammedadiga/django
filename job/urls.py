
from django.urls import include, path
from . import views



urlpatterns = [
    path('',views.jop_list),
    path('<int:id>',views.jop_detail)
]
