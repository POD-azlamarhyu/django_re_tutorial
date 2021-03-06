from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item
from .filters import ItemFilter
from .forms import ItemForm
# Create your views here.


class ItemFilterView(LoginRequiredMixin,FilterView):
    model=Item
    filterset_class=ItemFilter
    queryset=Item.objects.all().order_by('created_at')
    strict=False
    paginate_by=10

    def get(self,request,**kwargs):
        if request.GET:
            request.session['query'] = request.GET

        else:
            request.GET=request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key]=request.session['query'][key]
        
        return super().get(request,**kwargs)


class ItemDetailView(LoginRequiredMixin,DetailView):
    model=Item

class ItemCreateView(LoginRequiredMixin,CreateView):
    # def post(self,request,*args,**kwargs):
    #     form = ItemForm
    #     if form.is_valid():
    #         form.save()
    model=Item
    form_class=ItemForm
    success_url=reverse_lazy('index')

class ItemUpdateView(LoginRequiredMixin,UpdateView):
    model=Item
    form_class=ItemForm
    success_url=reverse_lazy('index')

class ItemDeleteView(LoginRequiredMixin,DeleteView):
    model=Item
    success_url=reverse_lazy('index')

