from django.shortcuts import render
from datetime import datetime
from django.http import Http404  # 의도하지 않은 404에러 (장고에 들어있는 기능) 가져오기

# Create your views here.


def index(request):
    today = datetime.today().date()
    # print(today) # 밑의 검은 화면(콘솔창)에 출력됨
    ctx = {'today': today}
    return render(request, 'menus/index.html', ctx)


# def chicken(request):
#     return render(request, 'menus/chicken.html')


def food_detail(request, food):
    ctx = dict()
    if food == "chicken":
        ctx["name"] = "코딩에 빠진 닭"
        ctx["description"] = "주머니가 가벼운 당신의 마음까지 생각한 가격 !"
        ctx["price"] = 10000
        ctx["img_path"] = "menus/images/chicken.jpg"
    else:
        raise Http404("당신이 찾고 싶은 음식은 우리 메뉴에 없어요!")
    return render(request, 'menus/detail.html', ctx)
