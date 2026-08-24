from django.shortcuts import render
from django.http import Http404
COURSES_DATA =[
{'id': 1, 'code': 'CN331', 'title': 'Software Engineering', 'credits':3, 'desc':
'Agile, Git, Django, and Testing'},
{'id': 2, 'code': 'CN311', 'title': 'Operating Systems', 'credits': 3, 'desc':
'Processes, Threads, and Memory'},
]
def course_list(request):
    return render(request, 'courses/list.html',{'courses':COURSES_DATA})\
    
def course_detail(request, id):
    course= next((item for item in COURSES_DATA if item['code']== id),None)
    if not course:
        raise Http404("Course Not Found")
    return render(request, 'courses/detail.html',{'course': course})