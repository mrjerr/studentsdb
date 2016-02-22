# #url for students application
# from django.conf.urls import url
# from students.views import groups, students, journal

# urlpatterns = [
#     #Students urls
#     url(r'^$', students.students_list, name='home'),
#     url(r'^students/add/$', students.students_add, name='students_add'),
#     url(r'^students/(?P<sid>\d+)/edit/$', students.students_edit, name='students_edit'),
#     url(r'^students/(?P<sid>\d+)/delete/$', students.students_delete, name='students_delete'),
#     #Groups urls
#     url(r'^groups/$', groups.groups_list, name='groups'),
#     url(r'^groups/add/$', groups.groups_add, name='groups_add'),
#     url(r'^groups/(?P<sid>\d+)/edit/$', groups.groups_edit, name='groups_edit'),
#     url(r'^groups/(?P<sid>\d+)/delete/$', groups.groups_delete, name='groups_delete'),
    
#     #Journal
#     url(r'^journal/$', journal.journal_list, name='journal_list'),
#     ##
# ]