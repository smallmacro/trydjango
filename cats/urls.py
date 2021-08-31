
from django.urls import path
from cats.views import cat_list_view, cat_create_view,dynamic_lookup_view,cat_delete_view,cat_update_view


app_name = 'cats'
urlpatterns = [
    path('', cat_list_view, name='cat_list'),
    path('create/', cat_create_view),
    path('<int:id>/', dynamic_lookup_view,name='cat_detail'),
    path('<int:id>/update/', cat_update_view,name='cat_update'),
    path('<int:id>/delete/', cat_delete_view, name='cat_delete'),

]
