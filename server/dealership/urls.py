from django.urls import path
from . import views

urlpatterns = [
    # Auth endpoints
    path('login/', views.login_view, name='api_login'),
    path('logout/', views.logout_view, name='api_logout'),
    path('register/', views.register_view, name='api_register'),
    path('check_auth/', views.check_auth, name='check_auth'),
    # Car makes
    path('get_all_car_makes/', views.get_all_car_makes, name='car_makes'),
    # Dealers
    path('get_dealers/', views.get_all_dealers, name='all_dealers'),
    path('get_dealer_by_id/', views.get_dealer_by_id, name='dealer_by_id'),
    path('get_dealers_by_state/', views.get_dealers_by_state, name='dealers_by_state'),
    # Reviews
    path('get_dealer_reviews/', views.get_dealer_reviews, name='dealer_reviews'),
    path('post_review/', views.post_review, name='post_review'),
    # Sentiment
    path('analyze_review/', views.analyze_review_api, name='analyze_review'),
]