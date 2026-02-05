from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.index, name='main'),
    # path('login/', views.login_data, name='login'),
    path('show/', views.show, name="show"),
    path('video/<int:id>/', views.video_detail, name='video_detail'),
    path('contact/',views.contact ,name='contact'),
    path('xnavp/' , views.nav ,name='nav'),
    path('features/',views.features , name='features'),
    path('courses/',views.courses ,name='courses'),
    path('aboute/' ,views.aboute ,name='aboute'),
    path('lfooter/' ,views.footer ,name='footer'),
    path('notes/',views.note ,name='notes'),
    path('logout/',views.out ,name='logout'),
    path('register/', views.register_view ,name='register'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('profile/success/', views.profile_success, name='profile_success'),
    path('profile/view/', views.view_profile, name='view_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('policy/' , views.policy , name='policy'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('result/', views.quiz_result, name='quiz_result'),
    path('certificate/', views.generate_certificate, name='generate_certificate'),
    path('certificate/' ,views.certificate_view ,name='viewc'),
    path('exam/' ,views.exam_list , name='exam'),
    path('aboute/' ,views.users , name='aboute')



 ] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)