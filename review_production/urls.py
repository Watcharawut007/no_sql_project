from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views


app_name = 'review_production'
urlpatterns = [
    path("api/products/", views.product_list),
    path("api/products/<str:product_id>", views.product_detail),
    path("api/products/<str:product_id>/reviews", views.product_reviews),

    path("api/reviews/", views.review_list),
    path("api/reviews/<str:review_id>", views.review_detail),

    path("home/",views.successlogin),
    path("api/search", views.search),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path("logout/", LogoutView.as_view(next_page='/login'), name="logout"),
]