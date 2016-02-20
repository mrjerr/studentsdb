from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students_list(request):
    students = (
        dict(
            id=1,
            first_name="Иван",
            last_name="Петров",
            ticket=235,
            image='img/me.jpeg'),
        dict(
            id=2,
            first_name="Петр",
            last_name="Иванов",
            ticket=236,
            image='img/piv.png')
    )
    return render(request, 'students/students_list.html', {'students':students})

def students_add(request):
    return HttpResponse('<h1>Student add form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student {}</h1>'.format(sid))

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student {}</h1>'.format(sid))

#Views for Group
def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')

def groups_add(request):
    return HttpResponse('<h1>Group add form</h1>')

def groups_edit(request, sid):
    return HttpResponse('<h1>Edit Group {}</h1>'.format(sid))

def groups_delete(request, sid):
    return HttpResponse('<h1>Delete Group {}</h1>'.format(sid))
