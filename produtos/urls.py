from django.urls import path
from .views import IndexListView,CriarProdutoView,EditarProdutoView,DeleteProdutoView

urlpatterns = [
    path('',IndexListView.as_view(),name='index'),
    path('add/',CriarProdutoView.as_view(),name='add_produto'),
    path('<int:pk>/editar/',EditarProdutoView.as_view(),name='editar_produto'),
    path('<int:pk>/deletar/',DeleteProdutoView.as_view(),name='del_produto'),
]
