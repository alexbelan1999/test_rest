from django.urls import path
from .views import UsersView, AccountsView, TransfersView, StoreView
app_name = "users"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('users/', UsersView.as_view()),
    path('users/<int:pk>', UsersView.as_view()),
    path('accounts/', AccountsView.as_view()),
    path('accounts/<int:pk>', AccountsView.as_view()),
    path('transfers/', TransfersView.as_view()),
    path('transfers/<int:pk>', TransfersView.as_view()),
    path('store/', StoreView.as_view()),
    path('store/<int:pk>', StoreView.as_view())

]