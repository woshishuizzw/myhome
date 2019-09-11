import json

from django.shortcuts import render

# Create your views here.
from App.models import Travel


def index(request):
    return render(request, "index.html")


def travellog(request):
    if request.method == "POST":
        data = request.POST
        province = list(data.keys())[0]
        note = list(data.values())[0].split('&')[0]
        trave = list(data.values())[0].split('&')[1]
        city = Travel.objects.filter(province=province)
        if city:
            id = city[0].id
            Travel.objects.filter(id=id).update(province=province, note=note, travel=trave)
        else:
            Travel.objects.create(province=province, note=note, travel=trave)

    Travels = Travel.objects.filter(travel=1)
    data = {}
    for travel in Travels:
        data[travel.province] = str(travel.ctime.date()) + travel.note

    Travels1 = Travel.objects.filter(travel=2)
    data1 = {}
    for tra1 in Travels1:
        data1[tra1.province] = str(tra1.ctime.date()) + tra1.note

    return render(request, 'travellog.html', {'data': json.dumps(data), 'data1': json.dumps(data1)})