from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from app.models import Todo, ContactUs
from django.views import View
from datetime import datetime
from django.utils import timezone
from .forms import UserRegistrationForm, UserProfileForm

# Create your views here.

#This is home page
class HomeView(View):
    def get(self, request):
        try:
            if request.user.is_anonymous:
                messages.warning(request, "Please Login to use website")
                return redirect('/login')
            else:
                allTodo = Todo.objects.filter(user=request.user)
                context = {'allTodo':allTodo}
            return render(request, "home.html", context)
        except Exception as err:
            print(err)

    def post(self, request):
        try:
            if request.method == "POST":
                user = request.user
                title = request.POST.get('title')
                desc = request.POST.get('desc')
                todo = Todo(user=user, title=title, desc=desc, date_created= datetime.today())
                todo.save()
                messages.success(request, str(user).capitalize() + " Your Todo Added Successfully!")
                return redirect('/')

            return render(request, "home.html")
        except Exception as err:
            print(err)



def loginUser(request):
    return render(request, "login.html")



class CustomerRegistrationView(View):
    def get(self, request):
        try:
            form = UserRegistrationForm()
            return render(request, 'signup.html', {'form':form})
        except Exception as err:
            print(err)


    def post(self, request):
        try:
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                messages.success(request, "Account Register Successfully!")
                form.save()
            return render(request, 'signup.html', {'form':form})
        except Exception as err:
            print(err)

def logoutUser(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('/login')


def about(request):
    try:
        if request.user.is_anonymous:
            messages.warning(request, "Please Login to use website")
            return redirect('/login')
        return render(request, "about.html")
    except Exception as err:
        print(err)

def deleteTodo(request, id):
    try:
        todo = Todo.objects.get(pk=id)
        todo.delete()
        messages.success(request, str(request.user).capitalize() + " Your Todo Deleted Successfully!")
        return redirect('/')
    except Exception as err:
        print(err)

class UpdateView(View):
    def get(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk, user = request.user)
            context = {'todo':todo}
            return render(request, "update.html", context)
        except:
            return render(request, "error_404.html")

    def post(self, request, pk):
        try:
            if request.method == "POST":
                user = request.user
                title = request.POST.get('title')
                desc = request.POST.get('desc')
                todo = Todo(pk=pk, user=user, title=title, desc=desc, date_created= timezone.now())
                todo.save()
                messages.success(request, str(user).capitalize() + " Your Todo Updated Successfully!")
                return redirect('/')
        except Exception as err:
            print(err)



class ProfileView(View):
    def get(self, request):
        try:
            form = UserProfileForm()
            context = {'form':form}
            return render(request, "contact.html", context)
        except Exception as err:
            print(err)


    def post(self, request):
        try:
            form = UserProfileForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                mobile_number = form.cleaned_data['mobile_number']
                hobbies = form.cleaned_data['hobbies'] 
                messege = form.cleaned_data['messege'] 
                reg = ContactUs(user=request.user, name=name, email=email, mobile_number=mobile_number, hobbies=hobbies, messege=messege, date_time=datetime.now())
                reg.save()
                messages.success(request, str(name).capitalize() + " Your Messege has been sent Successfully Our Admin-Kiran!")
                return redirect('/contact')

            return render(request, "contact.html", {'form':form})
        except Exception as err:
            print(err)
   


def error_404(request, exception):
        data = {}
        return render(request,'error_404.html', data)


def error_403(request,  exception):
        data = {}
        return render(request,'error_404.html', data)

def error_400(request,  exception):
        data = {}
        return render(request,'error_404.html', data)




def search(request):
    try:
        query = request.GET['query']
        allPostsTitle = Todo.objects.filter(user=request.user, title__icontains=query)
        allPostsContent = Todo.objects.filter(user=request.user, desc__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
            
        if allPosts.count() == 0:
            messages.warning(request, "No search results found. Please refine your query.")
        params = {'allPosts' : allPosts, 'query' : query}
        return render(request, "search.html", params)
    except Exception as err:
        print(err)
