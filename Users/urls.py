from django.urls import path, include
from .views import home, StudentSignUpView, TeacherSignUpView, login
#from .views import 
urlpatterns = [
    path('', home, name='home'),
    path('teach/', TeacherSignUpView.as_view(), name='teach_signup'),
    path('student/', StudentSignUpView.as_view(), name='student_signup'),
    path('login/', login, name='login_page'),
]