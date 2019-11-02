# visualisations URL Configuration

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # index pages
    path('respondent/home', views.user_home, name='user_home'),
    path('respondent/<int:user_id>/questionnaire/<str:questionnaire_name>', views.user_questionnaire, name='questionnaire'),
    path('respondent/<int:user_id>/visualisation/<str:questionnaire_name>', views.user_questionnaire_responses, name='questionnaire-responses'),
    path('researcher/home', views.researcher_home, name="researcher_home"),
    path('researcher/<int:user_id>/visualisation/<int:questionnaire_id>', views.researcher_questionnaire_data, name="research_q_data"),
    path('users', views.getUsers, name='users'),
]
