from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

import random

from inventions.models import Invention, Inventor, Category, Nation


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_inventions = Invention.objects.all().count()
    inventions = Invention.objects.order_by('-date_of_invention')

    inventions_to_random = list(Invention.objects.all())
    random_invention = random.choice(inventions_to_random)

    context = {
        'num_inventions': num_inventions,
        'inventions': inventions,
        'random_invention': random_invention
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


# def list(request):
#     """
#     View function for home page of site.
#     """
#     # Render the HTML template index.html
#     return render(
#         request,
#         'list.html',
#     )

class InventionListView(ListView):
    model = Invention

    context_object_name = 'inventions_list'   # your own name for the list as a template variable
    template_name = 'invention/list.html'  # Specify your own template name/location
    paginate_by = 6

    def get_queryset(self):
        if 'category_name' in self.kwargs:
            return Invention.objects.filter(category__name=self.kwargs['category_name']).all() # Get 5 books containing the title war
        else:
            return Invention.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['num_inventions'] = len(self.get_queryset())
        if 'category_name' in self.kwargs:
            context['view_title'] = f"Kategorie: {self.kwargs['category_name']}"
            context['view_head'] = f"Kategorie vynálezu: {self.kwargs['category_name']}"
        else:
            context['view_title'] = 'Vynálezy'
            context['view_head'] = 'Přehled vynálezů'
        return context


class InventionDetailView(DetailView):
    model = Invention

    context_object_name = 'invention_detail'   # your own name for the list as a template variable
    template_name = 'invention/detail.html'  # Specify your own template name/location
