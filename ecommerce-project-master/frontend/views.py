from django.shortcuts import render
from .models import Item
from django.views.generic import View, DetailView, ListView
# Create your views here.

# function based view
# def home(request):
#     context = {
#         'items': Item.objects.all()

#     }

#     # django get all items and push it into the home.html file
#     return render(request, 'home.html', context=context)

# class based view
class HomeView(ListView):
    model = Item
    paginate_by = 12 # how many items per page
    template_name = 'home.html'

class ProductDetailView(DetailView):
    model = Item
    template_name = 'detail.html'