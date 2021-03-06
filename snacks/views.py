from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

class SnackListView(ListView):
    template_name = 'home.html'

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'