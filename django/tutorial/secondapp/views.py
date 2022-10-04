from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from .model_panda import lprod as lp

# Create your views here.
def main(request):
    return HttpResponse('<u>Main</u>')

def insert(request):
    Course(name='데이터 분석', cnt='30').save()
    Course(name='데이터 수집', cnt='20').save()
    Course(name='웹개발', cnt='25').save()
    Course(name='인공지능', cnt='20').save()

    return HttpResponse('데이터 입력 완료')

def show(request):
    data = Course.objects.all()
    msg = ''
    
    for dt in data:
        msg += dt.name + ' ' + str(dt.cnt) + '<br>'
    
    return HttpResponse(msg)

def oneshow(request):
    data = Course.objects.get(pk=1)
    
    return HttpResponse(data.name + ' ' + str(data.cnt))
    
def show2(request):
    data = Course.objects.all()
    
    return render(
        request,
        'secondapp/show2.html',
        {'data' : data}
    )
    
def view_Lprod_List(request):
    df_list = lp.getLprodList()

    context = {'df_list' : df_list}
    
    return render(
        request,
        'html/lprod_list.html',
        context
    )

def view_Lprod(request):
    
    lprod_gu = request.GET['lprod_gu']
    
    df_dict = lp.getLprod(lprod_gu)
    
    return render(
        request,
        'html/lprod.html',
        df_dict
    )