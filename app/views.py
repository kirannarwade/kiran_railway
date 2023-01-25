from django.shortcuts import render, redirect
from .models import Todo, Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.

def home(request):
    all_todos = Todo.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        todo = Todo(title=title, desc=desc, date_time=datetime.now())
        todo.save()
        messages.success(request, 'New Todo Added Successfully!')
        return redirect('/')
    return render(request, 'home.html', {'all_todos':all_todos})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        messege = request.POST.get('messege')
        contact = Contact(name=name, email=email, phone=phone, messege=messege)
        contact.save()
        messages.success(request, f'{name.capitalize()} Your Messege has been sent Successfully!')
        return redirect('/contact')
    return render(request, 'contact.html')

def update_todo(request, pk):
    get_todo_id = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        todo = Todo(pk=pk, title=title, desc=desc, date_time=datetime.now())
        todo.save()
        messages.success(request, 'Your Todo Updated Successfully!')
        return redirect('/')
    return render(request, 'update.html', {'get_todo_id':get_todo_id})

def delete_todo(request, pk):
    get_todo_id = Todo.objects.get(pk=pk)
    get_todo_id.delete()
    messages.success(request, 'Todo Deleted Successfully!')
    return redirect('/')

