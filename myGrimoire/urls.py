from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "main"

urlpatterns = [
    path("home/", views.homepage, name="homepage"),
    path('register/', views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("main/", views.mainpage, name="mainpage"),
    path("courses/", views.coursesPage, name="courses"),
    path("you/", views.youPage, name="you"),
    path("readings/", views.readingsPage, name="readings"),
    path("readings/all-tarot-cards", views.allCardsPage, name="allCards"),
    path("readings/all-tarot-cards/<str:id_tarotCard>", views.tarotCard),
    path("readings/spreads", views.spreadsPage, name="spreads"),
    path("main/my-grimoire", views.myGrimoirePage, name="myGrimoirePage"),
    path("courses/<str:id_course>", views.course),
    path("courses/<str:id_course>/start", views.coursestart),
    path("courses/<str:id_course>/quiz", views.courseQuiz),
    path("courses/<str:id_course>/quiz/results", views.courseQuizResults),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
