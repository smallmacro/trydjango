from django.urls import path

from .views import (
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView
    )


app_name='courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('<int:id>/', CourseDetailView.as_view(),name='course-detail'),
    path('create/', CourseCreateView.as_view(),name='course-create'),
    path('<int:id>/update/', CourseUpdateView.as_view(),name='course-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='course-delete'),

]
