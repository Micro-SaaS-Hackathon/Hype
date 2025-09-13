from django.shortcuts import render
from utils import analyse as anl
from app.models import UserStatistic

def index(request):
    return render(request, "index.html")

def team(request):
    return render(request, "kamanda.html")

def register(request):
    return render(request, "register.html")

def statistics(request, category):

    json_data_path = f"static/datas/json_datas/{category}.json"

    with open(json_data_path, "r", encoding="utf-8") as f:
        csv_data = f.read()

    data_path = f"/static/datas/csv_datas/{category}.csv"
    
    context = {
        "data_path": data_path,
        "category": category
    }
    return render(request, "statistika.html", context)

def news(request):
    return render(request, "xeberler.html")

def about(request):
    return render(request, "haqqimizda.html")

def login(request):
    return render(request, "daxil.html")

def analyse(request, category):
    user = request.POST.get("user")
    region = request.POST.get("region")
    sahe = request.POST.get("sahe")
    torpaq = request.POST.get("torpaq")
    qiymet = request.POST.get("qiymet")
    iqlim = request.POST.get("iqlim")
    
    # anl.analyse(category, sahe, torpaq, qiymet, iqlim)

    UserStatistic.objects.create(
        user = user,
        region = region,
        field = sahe,
        soil_type = torpaq,
        avarage_price = qiymet,
        climate_class = iqlim
    )

    context = {
        "category": category
    }
    
    return render(request, "analiz.html", context)