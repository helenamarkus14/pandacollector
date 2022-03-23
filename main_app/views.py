from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from .models import Panda
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
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
    fields = ['name', 'img', 'age', 'gender']
    template_name = 'panda_create.html'
    # success_url = "/pandas/"
    def get_success_url(self):
        return reverse('panda_detail', kwargs={'pk': self.object.pk})

class Panda_Detail(DetailView):
    model = Panda
    template_name = "panda_detail.html"

class Panda_Update(UpdateView):
    model = Panda
    fields = ['name', 'img', 'age', 'gender']
    template_name = "panda_update.html"
    def get_success_url(self):
        return reverse('panda_detail', kwargs={'pk': self.object.pk})
    # success_url = "/pandas" 

class Panda_Delete(DeleteView):
    model = Panda
    template_name = "panda_delete.html"
    success_url = "/pandas/"