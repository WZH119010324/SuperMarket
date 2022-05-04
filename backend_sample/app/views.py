from re import A
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    return HttpResponse("Index here!")

def user_list(request):
    # Find user_list.html from template folder under app directory
    # (Find through all templates folders of all apps in the order of app installation)
    return render(request, "user_list.html")

def user_add(request):
    return HttpResponse("Add user here!")

def something(request):
    # request is an object encapsulating all the request information send by user though browser
    
    # get the request method: GET/POST...
    print(request.method)

    # get parameter transferred by url: /something/?n1=123&n2=999
    print(request.GET) 

    # get data from request body
    print(request.POST)

    # response: return the string to the requestor
    # return HttpResponse("return value")

    # response: read html content, and render it and return the string to the user browser 
    # return render(request, "something.html")

    # respond: redirect
    return redirect("https://www.baidu.com")

from app.models import Address

def orm(request):
    # insertion
    Address.objects.create(PostalCode = 42420, Segment = "Consumer")

    # deletion
    Address.objects.filter(id = 1).delete()
    Address.objects.all().delete()

    # seach -> QuerySet([object,object,object...])
    data_list = Address.objects.all()
    for obj in data_list:
        print(obj.id, obj.PostalCode, obj.Segment)
    
    row_object = Address.objects.filter(id = 1).first()

    # updation
    Address.objects.all().update(Segment = "hello")
    Address.objects.filter(id = 1).update(Segment = "hello")
    return HttpResponse("success")

def load(request):
    # data entry
    print('data entry...')
    data = open('app/static/dataset/Superstore.csv','r', encoding='unicode_escape')
    line = data.readline()
    # print(line)
    title = line.split(',')
    title[-1] = title[-1][:-1]  # exclude the \n
    # print(title)
    PostalCodeIndex = title.index('Postal Code')
    # print(PostalCodeIndex)
    SegmentIndex = title.index('Segment')
    # print(SegmentIndex)
    CountryIndex = title.index('Country')
    # print(CountryIndex)
    CityIndex = title.index('City')
    # print(CityIndex)
    StateIndex = title.index('State')
    # print(StateIndex)
    RegionIndex = title.index('Region')
    # print(RegionIndex)
    while True:
        line = data.readline()
        if line:
            l = line.split(',')
            if l[-1][-1] == '\n':
                l[-1] = l[-1][:-1]
            # print(l)
            Address.objects.create(PostalCode = l[PostalCodeIndex], Segment = l[SegmentIndex], Country = l[CountryIndex], City = l[CityIndex], State = l[StateIndex], Region = l[RegionIndex])
        else:
            break
    print('finish!')
    DataList = Address.objects.all()
    return render(request, "data.html", {"data_list": DataList})