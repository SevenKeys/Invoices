from django.conf.urls import url
from .views import UserList, UserDetail, UpdateUser, DeleteUser

urlpatterns = [
    url(r'^all/$', UserList.as_view(), name='users'),
    url(r'^user_detail/(?P<user_id>\d+)/$', UserDetail.as_view(), name='user_detail'),
    url(r'^edit_user/(?P<user_id>\d+)/$', UpdateUser.as_view(), name='edit_user'),
    url(r'^delete_user/(?P<user_id>\d+)/$', DeleteUser.as_view(), name='delete_user')
]
