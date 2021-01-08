from django.urls import path,include
from . import views
from .views import WarListView,FunUpdateView,FunDeleteView

urlpatterns = [
    path('',WarListView.as_view(), name='home'),
    path('uploaded/',views.yourUploads, name='uploaded'),
    path('upload/', views.upload, name='upload'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', FunUpdateView.as_view(), name='fun-update'),
    path('<int:pk>/delete/', FunDeleteView.as_view(), name='fun-delete'),
    path('your-likes/<int:query>', views.add_like_your_video, name='videoLike'),
    path('opponent-likes/<int:query>', views.add_like_opponent_video, name='opponentLike')
]
