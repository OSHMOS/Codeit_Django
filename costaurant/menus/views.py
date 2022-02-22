from django.shortcuts import render
from datetime import datetime
from django.http import Http404  # 의도하지 않은 404에러 (장고에 들어있는 기능) 가져오기
from menus.models import Menu

# Create your views here.


def index(request):
    ctx = dict()
    today = datetime.today().date()
    # print(today) # 밑의 검은 화면(콘솔창)에 출력됨
    menus = Menu.objects.all()
    ctx["today"] = today
    ctx["menus"] = menus
    return render(request, 'menus/index.html', ctx)


def food_detail(request, pk):
    ctx = dict()
    menu = Menu.objects.get(id=pk)
    ctx["menu"] = menu
    return render(request, 'menus/detail.html', ctx)
