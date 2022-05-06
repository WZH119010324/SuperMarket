from re import A
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

# def index(request):
#     return HttpResponse("Index here!")

# def user_list(request):
#     # Find user_list.html from template folder under app directory
#     # (Find through all templates folders of all apps in the order of app installation)
#     return render(request, "user_list.html")

# def user_add(request):
#     return HttpResponse("Add user here!")

# def something(request):
#     # request is an object encapsulating all the request information send by user though browser
    
#     # get the request method: GET/POST...
#     print(request.method)

#     # get parameter transferred by url: /something/?n1=123&n2=999
#     print(request.GET) 

#     # get data from request body
#     print(request.POST)

#     # response: return the string to the requestor
#     # return HttpResponse("return value")

#     # response: read html content, and render it and return the string to the user browser 
#     # return render(request, "something.html")

#     # respond: redirect
#     return redirect("https://www.baidu.com")

# def orm(request):
#     # insertion
#     Address.objects.create(PostalCode = 42420, Segment = "Consumer")

#     # deletion
#     Address.objects.filter(id = 1).delete()
#     Address.objects.all().delete()

#     # seach -> QuerySet([object,object,object...])
#     data_list = Address.objects.all()
#     for obj in data_list:
#         print(obj.id, obj.PostalCode, obj.Segment)
    
#     row_object = Address.objects.filter(id = 1).first()

#     # updation
#     Address.objects.all().update(Segment = "hello")
#     Address.objects.filter(id = 1).update(Segment = "hello")
#     return HttpResponse("success")

from app.models import Customer, Product, Order, Address, customer_postal

def load(request):
    # data entry
    print('data entry...')
    data = open('app/static/dataset/Superstore.csv','r', encoding='unicode_escape')
    line = data.readline()
    OrderIDIndex = 1
    OrderDateIndex = 2
    ShipDateIndex = 3
    ShipModeIndex = 4
    CustomerIDIndex = 5
    CustomerNameIndex = 6
    SegmentIndex = 7
    CountryIndex = 8
    CityIndex = 9
    StateIndex = 10
    PostalCodeIndex = 11
    RegionIndex = 12
    ProductIDIndex = 13
    CategoryIndex = 14
    SubCategoryIndex = 15
    ProductNameIndex = 16
    SalesIndex = 17
    QuantityIndex = 18
    DiscountIndex = 19
    ProfitIndex = 20
    while True:
        line = data.readline()
        if line:
            l = line.split(',')
            if l[-1][-1] == '\n':
                l[-1] = l[-1][:-1]
            if len(l) != 21:
                continue
            try: 
                Customer.objects.create(CustomerID = l[CustomerIDIndex], CustomerName = l[CustomerNameIndex])
            except:
                pass
            try:
                Product.objects.create(ProductID = l[ProductIDIndex], Category = l[CategoryIndex], SubCategory = l[SubCategoryIndex], ProductName = l[ProductNameIndex])
            except:
                pass
            try:
                ODate = l[OrderDateIndex].split('/')
                odate = ODate[2] + '-' + ODate[0] + '-' + ODate[1]
                SDate = l[ShipDateIndex].split('/')
                sdate = SDate[2] + '-' + SDate[0] + '-' + SDate[1]
                Customer_object = Customer.objects.filter(CustomerID = l[CustomerIDIndex]).first()
                Product_object = Product.objects.filter(ProductID = l[ProductIDIndex]).first()
                Order.objects.create(OrderID = l[OrderIDIndex], CustomerID = Customer_object, ProductID = Product_object, OrderDate = odate, ShipDate = sdate, ShipMode = l[ShipModeIndex], Sales = l[SalesIndex], Quantity = l[QuantityIndex], Discount = l[DiscountIndex], Profit = l[ProfitIndex])
            except:
                pass
            try:
                Address.objects.create(PostalCode = l[PostalCodeIndex], Segment = l[SegmentIndex], Country = l[CountryIndex], City = l[CityIndex], State = l[StateIndex], Region = l[RegionIndex])
            except:
                pass
            try:
                Customer_object = Customer.objects.filter(CustomerID = l[CustomerIDIndex]).first()
                Address_object = Address.objects.filter(PostalCode = l[PostalCodeIndex]).first()
                customer_postal.objects.create(CustomerID = Customer_object, PostalCode = Address_object)
            except:
                pass
        else:
            break
    print('finish!')
    # DataList = Address.objects.all()
    # return render(request, "data.html", {"data_list": DataList})
    return HttpResponse("The data has been loaded successfully. Please check the database.")