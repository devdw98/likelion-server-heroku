from django.urls import include, path

urlpatterns = [
    path('users/',include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/',include('rest_auth.registration.urls')),#회원가입을 위한 라이브러리 >> url연결만 해주면 됨
]
