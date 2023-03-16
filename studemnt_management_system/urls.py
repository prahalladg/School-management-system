from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
    path('school/', include('school.urls')),
    path('contactus/', include('contact.urls')),
    path('authenication/', include('authenticate_user.urls')),
    path('student/', include('student.urls')),
    path('studentmarks/', include('student_marks.urls')),
    path('studentattendance/', include('student_attendance.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)