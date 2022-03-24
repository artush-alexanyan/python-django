from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1 style='color: blue; text-align: center; margin-top: 50px;'>The page Women is "
                        "successfully got</h1>")


def django_page(request):
    a = 5
    if a > 4:
        return HttpResponse("<h1 style='color: green; text-align: center; margin-top: 50px;'>DJANGO</h1>")
    else:
        return HttpResponse("<h1 style='color: red; text-align: center; margin-top: 50px;'>A is smaller than 4</h1>")


def categories(request, cat_id):
    return HttpResponse(f"<h1 style='color: purple; text-align: center; margin-top: 50px;'>This is a categories page "
                        f"- NO: {cat_id}</h1>")


def archive(request, year):
    return HttpResponse(f"This is a archive of <b>{year}</b> year!")
