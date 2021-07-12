from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ItensModel


class ItemListView(ListView):
    model = ItensModel
    template_name = 'loja/list.html'
    context_object_name = 'itens'
    paginate_by = 5

    # CASO PRECISE ADICIONAR PAGINADOR
    # def get_context_data(self, **kwargs: any) -> dict[str, any]:
    #     context = super(ItemListView, self).get_context_data(**kwargs)
    #     itens = self.get_queryset()
    #     page = self.request.GET.get('page')
    #     paginator = Paginator(itens, self.paginate_by)
    #     try:
    #         itens = paginator.page(page)
    #     except PageNotAnInteger:
    #         itens = paginator.page(1)
    #     except EmptyPage:
    #         itens = paginator.page(paginator.num_pages)
    #     context['itens'] = itens
    #     return context


@method_decorator(login_required(login_url='/user/login'), name='dispatch')
class ItemCreateView(CreateView):
    model = ItensModel
    template_name = 'loja/create.html'
    fields = ('nome', 'descricao', 'valor', 'quantidade')
    success_url = reverse_lazy('lista-itens')


class ItemDetailView(DetailView):
    model = ItensModel
    template_name = 'loja/detail.html'
    context_object_name = 'item'


@method_decorator(login_required(login_url='/user/login'), name='dispatch')
class ItemUpdateView(UpdateView):
    model = ItensModel
    template_name = 'loja/update.html'
    context_object_name = 'item'
    fields = ('nome', 'descricao', 'valor', 'quantidade')

    def get_success_url(self) -> str:
        return reverse_lazy('detalhe-itens', kwargs={'pk': self.object.id})


@method_decorator(login_required(login_url='/user/login'), name='dispatch')
class ItemDeleteView(DeleteView):
    model = ItensModel
    template_name = 'loja/delete.html'
    success_url = reverse_lazy('lista-itens')