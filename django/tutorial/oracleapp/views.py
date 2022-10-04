from django.http import HttpResponse
from django.shortcuts import render
from .model_pandas import member as mem
from django.core.paginator import Paginator

# Create your views here.
# 테스트
def test(request):
    return HttpResponse('테스트')

def test2(request):
    test = '오라클 연결 테스트'
    return render(
        request,
        'oracleapp/test.html',
        {'test' : test}
    )
    
# 회원전체 조회
def view_Member_List(request):
    
    df = mem.getMemberList()

    # return HttpResponse(df)

    context = {'df' : df}

    return render(
        request,
        'oracleapp/member_list.html',
        context
    )
    
# 회원 상세조회
def view_Member(request):
    
    mem_id = request.GET['mem_id']
    
    df_dict = mem.getMember(mem_id)
    
    # context = {'df' : df_dict}
    
    return render(
        request,
        'oracleapp/member.html',
        df_dict
    )
    
# 회원 전체조회(딕셔너리 형태)
def view_Member_ListDict(request):
    df_list = mem.getMemberListDict()

    context = {'df_list' : df_list}
    
    return render(
        request,
        'oracleapp/member_list_dict.html',
        context
    )
    
def set_Member_Delete(request):
    
    pcart_no = request.GET['pcart_no']
    pcart_prod = request.GET['pcart_prod']
    
    
    msg = mem.setCartDelete(pcart_no, pcart_prod)
    
    pageControl = ''
    
    if msg == 'Y' :
        pageControl = '''<script>
                            alert('삭제 되었습니다!!')
                            location.href='/db/cart_list_dict/'
                            </script>
        '''
    else :
        pageControl = '''<script>
                            alert('삭제 실패!!')
                            history.go(-1)
                        </script>
        '''
    
    return HttpResponse(pageControl)    
    
    
    
def Member_List_Page(request) :
    #page_contrl/cart_list_page.html
##페이지 처리 시작 >>>
        
    try :
        now_page = request.GET.get('page')
        now_page = int(now_page)    
    
    except :
        now_page = 1
##페이지 처리 끝<<<<      

    
#모델 조회
    df_list = mem.getDictType_Member()

#페이지 처리 시작>>>
#-첫번째 값은 모델 조회한 데이터
#-두번째 값은 한페이지에 보여줄 행의 갯수
    p = Paginator(df_list, 4)
#페이지 처리 끝>>>

    info = p.get_page(now_page)
    # 시작페이지 번호
    start_page = (now_page - 1) // 10  * 10  + 1
    # 마지막페이지 번호
    end_page = start_page +9 
    #p.num_page:전체 페이지 수
    #end_page : 계산에 의한 페이지 수(10 단위 계산)
    #전체 페이지 수보다 크다면,
    #전체 페이지 수로 변경
    if end_page > p.num_pages:
        end_page = p.num_pages
    
    #이전 페이지 가기
    is_prev = False
    # 다음 페이지 가기
    is_next = False
        
    #이전 /다음 체크하기
    if start_page > 1 :
        is_prev = True
    
    if end_page < p.num_pages :
        is_next = True
    


    # context = {'df_list' : df_list}
    context = {'info' :info ,
               'page_range' :range(start_page, end_page +1) ,
               'is_prev' :is_prev ,
               'is_next' :is_next ,
               'start_page' :start_page ,
               'end_page' :end_page }
    
    return render(
        request,
        'oracleapp/member_list_page.html',
        context
    )