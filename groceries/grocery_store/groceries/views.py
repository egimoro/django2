from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  DeleteView)


from .models import Grocery_store, Groceries


class Grocery_storeList(ListView):
    model = Grocery_store
    template_name = 'groceries/index.html'

    def get_queryset(self):
        return Grocery_store.objects.order_by('-date_established')[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 


