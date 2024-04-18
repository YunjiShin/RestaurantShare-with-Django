from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("index")
    return render(request, 'shareRes/index.html')
def restaurantDetail(request):
    # return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurantDetail.html')

def restaurantCreate(requset):
    # return HttpResponse("restaurantCreate")
    return render(requset, 'shareRes/restaurantCreate.html')

def categoryCreate(requset):
    # return HttpResponse("categoryCreate")
    return render(requset, 'shareRes/categoryCreate.html')