from django.shortcuts import render
from django.http import HttpResponse
from random import randrange

#Views for Group
def journal_list(request):
    journal_data = (
        dict(
            id=1,
            name="Иванов Петр",
            journal=[randrange(0,2) for i in range(1,32)]
        ),
        dict(
            id=2,
            name="Петров Андрей",
            journal=[randrange(0,2) for i in range(1,32)]
        )
    )
    journal_th = ['#', 'Студент'] + [i for i in range(1, 32)]
    return render(request, 'students/journal.html', {'th':journal_th, 'journal': journal_data})
    return render(request, 'students/groups_list.html', {'groups':journal})