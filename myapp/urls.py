from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/", views.home, name='home'),
    path("stud/", views.student_list, name='studlist'),
    path("stud/add/", views.add_student, name='add_student'),
    path("stud/edit/<int:pk>/", views.edit_student, name='edit_student'),
    path("stud/delete/<int:pk>/", views.delete_student, name='delete_student'),
    path("students/update/<int:pk>/", views.update_student, name='update_stud'),
    path("register/", views.register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path("home1/", views.home1, name='home'),
    path("home2/", views.reshome1, name='home'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)