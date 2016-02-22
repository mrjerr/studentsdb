from django.shortcuts import render
from django.http import HttpResponse


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