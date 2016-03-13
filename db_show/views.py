from django.shortcuts import render

from db_show.models import Group,Student,College


def prin(request):
    groups_list = []
    students_list = []
    list_college = {}

    colleges = College.objects.filter()

    group = Group.objects.filter(id_college=colleges)

    # students = Student.objects.filter(id_group=group)
    students = Student.objects.filter().all()


    for college in colleges:
        group = Group.objects.filter(id_college=college)

        list_college[college] = Student.objects.filter(id_group=group)



    dict_val = {'students': students}
    # dict_val = {'colleges': list_college, "groups": groups_list, "students": students_list}

    return render(request,'student.html',dict_val)
# Create your views here.
