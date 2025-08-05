from django.db import models

from django.db import models

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return self.name