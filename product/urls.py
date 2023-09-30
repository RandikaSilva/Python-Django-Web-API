from django.urls import path
from .views import ProductList, ProductDetailView

urlpatterns = [
    path("", ProductList.as_view()),
    path("<int:id>", ProductDetailView.as_view()),
]
