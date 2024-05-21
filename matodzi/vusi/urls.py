from django.urls import path
from .views import IndexView, inner_page_view, portfolio_details_view

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('inner-page/', inner_page_view, name='inner_page'),
    path('portfolio-details/', portfolio_details_view, name='portfolio_details'),

]