from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from .models import Course, LectureNote
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from bs4 import BeautifulSoup





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
    
    
    
def search_results(request):
    # Get the search query from the GET request
    query = request.GET.get('query', '')

    search_results = LectureNote.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'query': query, 'search_results': search_results})


def python_docs(request):
    urls = [
        "https://docs.python.org/3/glossary.html#glossary",
        "https://docs.python.org/3/tutorial/index.html",
        "https://docs.python.org/3/tutorial/introduction.html",
        "https://docs.python.org/3/tutorial/controlflow.html",
        "https://docs.python.org/3/tutorial/datastructures.html",
    ]
    
    all_code_snippets = []
    for url in urls:
        # Send a GET request to the current URL
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, "html.parser")
            
            # h_code_blocks = soup.find_all("h1")
            
            # span_code_blocks = soup.find_all("span")


            # # Find all code block elements in pre tags
            # pre_code_blocks = soup.find_all("pre")

            # # Find all code block elements in p tags
            # p_code_blocks = soup.find_all("p")
            
            # dd_code_blocks = soup.find_all("dd", id="term-annotation")


            # Find all code block elements in  tags
            section_code_blocks = soup.find_all("section")

            # Extract code snippets from all found tags ( h_code_blocks +  span_code_blocks + p_code_blocks  + dd_code_blocks + pre_code_blocks + )
            code_snippets = []

            for code_block in  section_code_blocks:
                code_text = code_block.get_text()
                code_snippets.append(code_text)

            # Append the code snippets for this route to the overall list
            all_code_snippets.extend(code_snippets)

     

        # Pass the code snippets to the template
        return render(request, 'python-docs.html', {'code_snippets': all_code_snippets})

    else:
        return HttpResponse("Failed to retrieve the documentation. Status code: " + str(response.status_code))