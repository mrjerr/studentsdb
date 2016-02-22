from django.shortcuts import render
from django.http import HttpResponse

#Views for Group
def groups_list(request):
    groups = (
        dict(
            id=1,
            name="ДЕ-42",
            leader=dict(id=1, name='Иванов Петр')
        ),
        dict(
            id=2,
            name="ДЕ-41",
            leader=dict(id=2, name='Петров Иван')
        )
    )
    return render(request, 'students/groups_list.html', {'groups':groups})

def groups_add(request):
    return HttpResponse('<h1>Group add form</h1>')

def groups_edit(request, sid):
    return HttpResponse('<h1>Edit Group {}</h1>'.format(sid))

def groups_delete(request, sid):
    return HttpResponse('<h1>Delete Group {}</h1>'.format(sid))