from django.urls import path, include, re_path


urlpatterns = [

    path('api/v1/auth/', include('djoser.urls'), name='login'),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/', include('referral_app.api.router')),
    # path('', include('rest_framework.urls')),
]
