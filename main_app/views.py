from dataclasses import fields
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View # <- View class to handle requests
from django.http import HttpResponse, HttpResponseRedirect # <- a class to handle sending a type of response
from .models import Panda, PandaToy, PandaSnack
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = 'home.html'

    # Here we are adding a method that will be ran when we are dealing with a GET request
    # def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        # Old GET req
        # return HttpResponse("Cats Home")

class About(TemplateView):
    template_name = 'about.html'
    # Old get req
    # def get(self, request):
    #     return HttpResponse("Cats About")
# class Panda:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

# pandas = [
#     Panda("Mau", 5, "Female"),
#     Panda("Garfield", 43, "Male"),
#     Panda("Meowth", 25, "Male"),
#     Panda("Salem", 500, "Male"),
# ]    
class PandaList(TemplateView):
    template_name = 'pandalist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["pandas"] = Panda.objects.filter(name__icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            context["pandas"] = Panda.objects.all()
            context['header'] = "Our Pandas" # this is where we add the key into our context object for the view to use
        return context
class Panda_Create(CreateView):
    model = Panda
    fields = ['name', 'img', 'age', 'gender', 'user', 'pandatoys', 'pandasnacks']
    template_name = 'panda_create.html'
    # success_url = "/pandas/"
    # def get_success_url(self):
    #     return reverse('panda_detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/pandas')

class Panda_Detail(DetailView):
    model = Panda
    template_name = 'panda_detail.html'

class Panda_Update(UpdateView):
    model = Panda
    fields = ['name', 'img', 'age', 'gender', 'pandatoys']
    template_name = 'panda_update.html'
    def get_success_url(self):
        return reverse('panda_detail', kwargs={'pk': self.object.pk})
    # success_url = "/pandas" 

class Panda_Delete(DeleteView):
    model = Panda
    template_name = 'panda_delete.html'
    success_url = '/pandas/'

# Profile for the user
def profile(request, username):
    user = User.objects.get(username=username)
    pandas = Panda.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'pandas': pandas}) 

# Panda toys

def pandatoys_index(request):
    pandatoys = PandaToy.objects.all()
    return render(request, 'pandatoy_index.html',{'pandatoys': pandatoys})

def pandatoys_show(request, pandatoy_id):
    pandatoy = PandaToy.objects.get(id=pandatoy_id)
    return render(request, 'pandatoy_show.html', {'pandatoy': pandatoy})

class PandaToyCreate(CreateView):
    model = PandaToy
    fields = '__all__'
    template_name = 'pandatoy_form.html'
    success_url = '/pandatoys/'

class PandaToyUpdate(UpdateView):
    model = PandaToy
    fields = ['name', 'color']
    template_name = 'pandatoy_update.html'
    success_url = '/pandatoys/'

class PandaToyDelete(DeleteView):
    model = PandaToy
    template_name = 'pandatoy_confirm_delete.html'
    success_url = '/pandatoys/'     

# Panda Snacks

def pandasnacks_index(request):
    pandasnacks = PandaSnack.objects.all()
    return render(request, 'pandasnack_index.html',{'pandasnacks': pandasnacks})

def pandasnacks_show(request, pandasnack_id):
    pandasnack = PandaSnack.objects.get(id=pandasnack_id)
    return render(request, 'pandasnack_show.html', {'pandasnack': pandasnack})

class PandaSnackCreate(CreateView):
    model = PandaSnack
    fields = '__all__'
    template_name = 'pandasnack_form.html'
    success_url = '/pandasnacks/'

class PandaSnackUpdate(UpdateView):
    model = PandaSnack
    fields = '__all__'
    template_name = 'pandasnack_update.html'
    success_url = '/pandasnacks/'

class PandaSnackDelete(DeleteView):
    model = PandaSnack
    template_name = 'pandasnack_confirm_delete.html'
    success_url = '/pandasnacks/'    
