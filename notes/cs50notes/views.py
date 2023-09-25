from django.http import JsonResponse
from django.shortcuts import render
from .models import Course, LectureNote
from django.shortcuts import render, get_object_or_404
from django.contrib import messages




def home(request):
    return render(request, 'home.html')
    

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})
    
    
    
def lecture_note_list(request, course_id):
    # First, retrieve the course using get_object_or_404
    course = get_object_or_404(Course, pk=course_id)
    
    # Then, filter lecture notes based on the retrieved course
    notes = LectureNote.objects.filter(category_id=course_id)

    return render(request, 'course-notes.html', {'course': course, 'notes': notes})
    
    
 
    
    
def lecture_note_detail(request, course_id, lecture_note_id):
    # Retrieve the lecture note using get_object_or_404
    note = get_object_or_404(LectureNote, pk=lecture_note_id)

    # Retrieve the associated course
    course = get_object_or_404(Course, pk=course_id)

    return render(request, 'lecture_note_detail.html', {'note': note, 'course': course})
    
  
  
# Get all the notes related to this course 
def course_notes(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    notes = LectureNote.objects.filter(category_id=course_id)
    
    print(notes)
    return render(request, 'course-notes.html', {'course': course, 'notes': notes})   