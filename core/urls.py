from django.urls import path,include
from .views import current_user, UserList,snippet_list

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('snippets/', snippet_list),
    
    # path('posting/',DataCreateView.as_view()),
]