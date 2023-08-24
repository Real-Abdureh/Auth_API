from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from API import views

urlpatterns = [
    #Auth Routes
    path("token/", views.MyTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("register/", views.RegisterView.as_view()),
    path("dashboard/", views.dashboard),

    #Todo's routes
    path("todo/<user_id>", views.TodoListView.as_view()),
    path("todo-detail/<user_id>/<todo_id>", views.TodoDetailView.as_view()),
    path("todo-completed/<user_id>/<todo_id>", views.TodoMarkAsComplted.as_view()),
    
]