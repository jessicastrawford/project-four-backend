from django.urls import path
from .views import DesignListView, DesignDetailView, CommentListView, CommentDetailView

urlpatterns = [
    path('', DesignListView.as_view()),
    path('<int:pk>', DesignDetailView.as_view()),
    path('<int:design_pk>/comments/', CommentListView.as_view()),
    path('<int:design_pk>/comments/<int:comment_pk>', CommentDetailView.as_view())
]
