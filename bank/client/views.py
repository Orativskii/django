from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["Name"]
            surname = userform.cleaned_data["Surname"]
            rez =name + " " + surname
            return HttpResponse("<h2>На ваше имя: {0} оформлено карту. Заберите карту в ближайшем отделении банка</h2>".format(rez))
    return render(request, "index.html", {"form": userform})