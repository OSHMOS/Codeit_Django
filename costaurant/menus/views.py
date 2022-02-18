from django.shortcuts import render
from datetime import datetime

# Create your views here.


def index(request):
    today = datetime.today().date()
    # print(today) # 밑의 검은 화면(콘솔창)에 출력됨
    ctx = {'today': today}
    return render(request, 'menus/index.html', ctx)


# def chicken(request):
#     return render(request, 'menus/chicken.html')


def food_detail(request, food):
    ctx = {'name': food}
    return render(request, 'menus/detail.html', ctx)
