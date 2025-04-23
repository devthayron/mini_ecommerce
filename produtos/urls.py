from django.urls import path
from .views import IndexListView,CriarProdutoView,EditarProdutoView,DeleteProdutoView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',IndexListView.as_view(),name='index'),
    path('add/',CriarProdutoView.as_view(),name='add_produto'),
    path('<int:pk>/editar/',EditarProdutoView.as_view(),name='editar_produto'),
    path('<int:pk>/deletar/',DeleteProdutoView.as_view(),name='del_produto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
