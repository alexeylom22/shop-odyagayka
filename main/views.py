from django.shortcuts import render
from .models import Items
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'main/home.html')

class create_item(LoginRequiredMixin, CreateView):
    model = Items
    template_name = 'main/create_item.html'

    fields = ['item', 'name', 'description', 'sizes', 'price', 'discount']

    def get_context_data(self, **kwards):
        ctx = super(create_item, self).get_context_data(**kwards)
        # ctx['item'].widget.attrs.update({'class': 'form-control'})
        ctx['item'] = 'Тип товару'
        ctx['name'] = 'Назва товару'
        ctx['description'] = 'Опис товару'
        ctx['sizes'] = 'Розміри (наприклад "S-3XL")'
        ctx['price'] = 'Ціна'
        ctx['discount'] = 'Знижка (якщо є)'
        return ctx


class ShowItemsView(ListView):
    model = Items
    template_name = 'main/items_page.html'
    context_object_name = 'items'
    ordering = ['-date']
    paginate_by = 24


    def get_context_data(self, **kwards):
        ctx = super(ShowItemsView, self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница'
        return ctx

class ItemsDetailView(DetailView):
    model = Items
    template_name = 'main/items_detail.html'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(ItemsDetailView, self).get_context_data(**kwargs)
        ctx['sizes'] = ''
        return ctx

class ItemsBuyDetailView(DetailView):
    model = Items
    template_name = 'main/items_buy.html'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(ItemsBuyDetailView, self).get_context_data(**kwargs)
        ctx['sizes'] = ''
        return ctx

class ItemsDeleteView(DeleteView):
    model = Items
    context_object_name = 'item'
    success_url = '/'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(ItemsDeleteView, self).get_context_data(**kwargs)
        return ctx