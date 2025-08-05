from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import Studentform,RegisterForm
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentlist.html', {'students': students})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = Studentform(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('studlist')  # Fixed name
    else:
        form = Studentform(instance=student)
    return render(request, 'update_student.html', {'form': form})

def add_student(request):
    form = Studentform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('studlist')  # Fixed name
    return render(request, 'add_student.html', {'form': form})

def edit_student(request, pk):
    student_obj = get_object_or_404(Student, pk=pk)
    form = Studentform(request.POST or None, instance=student_obj)
    if form.is_valid():
        form.save()
        return redirect('studlist')  # Fixed name
    return render(request, 'edit_student.html', {'form': form})

def delete_student(request, pk):
    student_obj = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student_obj.delete()
        return redirect('studlist')  # Fixed name
    return render(request, 'delete_student.html', {'student': student_obj})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully registered!")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

from django.shortcuts import render

def home1(request):
    return render(request, 'home.html')

def reshome1(request):
    return render(request, 'reshome.html')