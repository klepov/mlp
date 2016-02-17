from django.db import models
from django.db.models import Model


class College(models.Model):
    name_college = models.CharField(max_length=30)

    def __str__(self):
        return self.name_college


class Group(models.Model):
    name_group = models.CharField(max_length=30)
    id_college = models.ForeignKey(College)

    def __str__(self):
        return self.name_group

class Student(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    birthday = models.DateField(max_length=30)
    id_group = models.ForeignKey(Group)

    @property
    def get_fio(self):
        return self.last_name + " " + self.first_name +" "+ self.second_name
    def __str__(self):
        return self.get_fio

