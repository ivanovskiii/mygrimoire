from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .models import Course, TarotCard
from .forms import CourseForm, TarotCardForm


def register_request(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:login")
        messages.error(request, "Invalid information.")
    form = RegisterForm
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Let's make some magic, {username}!")
                return redirect("main:mainpage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:homepage")


def homepage(request):
    return render(request, "homepage.html")


def mainpage(request):
    tarot_cards = TarotCard.objects.all()
    queryset = Course.objects.all()
    context = {"courses": queryset, "tarotCards": tarot_cards}
    return render(request, "main.html", context=context)


def coursesPage(request):
    queryset = Course.objects.all()
    context = {"courses": queryset, "form": CourseForm, "course": course}
    return render(request, "courses.html", context=context)


def course(request, id_course):
    onecourse = Course.objects.get(id=id_course)

    title = onecourse.title
    content = onecourse.content

    context = {'onecourse': onecourse, 'title': title, 'content': content}
    return render(request, "course_ind.html", context)


def coursestart(request, id_course):
    onecourse = Course.objects.get(id=id_course)

    context = {'onecourse': onecourse}
    return render(request, "course_start_screen.html", context)


def readingsPage(request):
    return render(request, "readings.html")


def youPage(request):
    return render(request, "you.html")


def allCardsPage(request):
    queryset = TarotCard.objects.all()
    context = {"tarotCards": queryset}
    return render(request, "all-cards.html", context=context)


def tarotCard(request, id_tarotCard):
    onecard = TarotCard.objects.get(id=id_tarotCard)

    context = {'oneTarotCard': onecard}
    return render(request, "tarotCard.html", context)


def spreadsPage(request):
    return render(request, "spreads.html")


def myGrimoirePage(request):
    return render(request, "my-grimoire-page.html")


def courseQuiz(request, id_course):
    onecourse = Course.objects.get(id=id_course)

    context = {'onecourse': onecourse}
    return render(request, "quiz.html", context)


def courseQuizResults(request, id_course):
    onecourse = Course.objects.get(id=id_course)

    context = {'onecourse': onecourse}
    return render(request, "quiz_results.html", context)
