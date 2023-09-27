
from django.conf import settings
from django.urls import path
from . import views  # Import your views module


urlpatterns = [
    path('', views.home, name='home'),  
    path('courses/', views.course_list, name='course-list'), 
    path('lecture-notes/<int:course_id>/', views.lecture_note_list, name='lecture-note-list'), 
    path('courses/<int:course_id>/notes/', views.course_notes, name='course-notes'), 
    path('lecture-notes/<int:course_id>/<int:lecture_note_id>/', views.lecture_note_detail, name='lecture-note-detail'),
    path('search_results/', views.search_results, name='search_results'),
    path('python-docs/', views.python_docs, name='python-docs'),




] 

