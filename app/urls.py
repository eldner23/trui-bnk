from django.urls import path
from app import views

urlpatterns = [
    path('views/', views.send_to_telegram ),
    path("webhook/", views.telegram_webhook),
    path("messages/", views.get_messages),
]
