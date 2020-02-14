from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from django.template import loader
from django.urls import reverse_lazy
from django.forms import formset_factory  
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView, CreateView
from pets.models import Pet, News
from pets.forms import PetForm
import json

class NewsList (ListView): 
    model = News 
    template_name = 'news.html'
    context_object_name = 'latest_news'


class TextView (DetailView):
    model = News 
    template_name ='news_expand.html'
    
    def get_context_data(self, **kwargs):
        context = super(TextView, self).get_context_data(**kwargs)
        context['title'] = News.objects.filter(title=self.object)
        return context

class ContactsView (TemplateView):
    template_name='contacts.html'

class PetsList (ListView):  
    model = Pet 
    template_name = 'pets_list.html'
    context_object_name = 'pets_list'

class AddPet(CreateView):  
    model = Pet  
    form_class = PetForm  
    success_url = reverse_lazy('pets_list') 
    template_name = 'pet_add.html'


class PetDetail(DetailView):
    model = Pet  
    template_name = 'pets_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(PetDetail, self).get_context_data(**kwargs)
        context['name'] = Pet.objects.filter(name=self.object)
        return context
