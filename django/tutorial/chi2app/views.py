from django.shortcuts import render

# Create your views here.
from re import A
from django.http import HttpResponse
from django.shortcuts import render
from .model_pandas import cart
from .model_pandas import login
from .model_pandas import survey

#페이지처리 라이브러리1
from django.core.paginator import Paginator 

def view_Test(request):
    
    return render(
        request,
        'cart/survey.html',
        {'msg' 'ok'}
        
    )

def view_DB_Test(request):

    df = survey.getDBTest()
        
    context = {'msg' : df}
    
    return render(
        request,
        'cart/survey.html',
        context
    )
    
    
#설문 전체 조회하기
def view_Survey_List(request) :
    
    df = survey.getSurveyList()
    
    # return HttpResponse(df.to_html())
    context = {'df' : df.to_html()}
    
    return render(
        request,
        'cart/list.html',
        context
    )
#설문 참여하기
def view_Servey(request) :
    
    
    return render(
        request,
        'cart/survey.html',
        {}
    )

    
def CreateTable(request):
    
    survey.createTableSurvey()
    
    return HttpResponse('Create OK...')

#설문 데이터 입력 테스트
def set_Survey_Insert_test(request) :
    
    pgender = '여'
    page = 20
    pco_survey = '스타벅스'
    
    survey.setSurveyInsert(pgender,page,pco_survey)
    return HttpResponse('Insert OK')
    
    
def set_Survey_Insert(request) :
    
    pgender = request.POST.get('gender')
    page = request.POST.get('age')
    pco_survey = request.POST.get('co_survey')
    
    rs = survey.setSurveyInsert(pgender,page,pco_survey)
    
    msg =''
    if rs == 'ok' :
        msg='''<script>
            alert('입력성공!!')
            location.href = '/chi2/survey_list/'
            </script>'''
    return HttpResponse(msg)


def survey_Analysis(request) :
    #설문 데이터 조회하기
    df = survey.getSurveyList()
    
    #설문 분석하기(함수로 처리)
    #rs_df : 분석에 사용된 컬럼 추가된 최종본
    #rs_ct :교차표(crossTable) 데이터
    #rs_msg : 해석 결과
    rs_df, rs_ct, rs_msg = get_Analysis(df)


    #시각화 및 저장하기(함수로 처리)
    view_Visualization(rs_df)
    
    context = {
        #교차표를 html로 전환하여 키 생성
        'crossTab' : rs_ct.to_html(),
        
        #해석내용
        'results' : rs_msg}
    return render(request,
                'cart/analysis.html',
                context
                
    )
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

#설문 분석하기
def get_Analysis(df):    
    #성별을 숫자로...
    df['genNum'] = df['gender'].apply(lambda g:1 if g=='남' else 2)
    
    #커피숍 이름을 숫자로
    df['coNum'] = df['co_survey'].apply(lambda c:1 if c == '스타벅스' \
                    else 2 if c == '커피빈' \
                    else 3 if c == '이디아' else 4)

    #교차표(빈도표) 생성하기
    crossTab = pd.crosstab(index = df['gender'], columns = df['co_survey'])

    #검증하기 (표 값은 4개가 나오는데 값을 안받고 싶으면 변수명을 '_'로 한다.)
    chi, pv, _, _ = stats.chi2_contingency(crossTab)

# 검증결과
    results = ''
    if pv > 0.05 :
        results ='p-value 값이 유의 수준<b>{:.3f} > 0.05</b> 이므로, '\
            '<br>성별에 따라 선호하는 커피브랜드에는 ' \
                '<b>차이가 없다.(귀무가설 채택)</b>'.format(pv)
    else:
        results ='p-value 값이 유의 수준<b>{:.3f} <= 0.05</b> 이므로, '\
            '<br>성별에 따라 선호하는 커피브랜드에는 ' \
                '<b>차이가 없다.(e대립가설 채택)</b>'.format(pv)
    return df, crossTab, results
def view_Visualization(df):
    
    plt.rc('font', family ='Malgun Gothic')
    
    plt.figure(figsize = (18,18))
    #fig객체얻기 gcf =>figure와 같음
    fig = plt.gcf()
    # 그룹화 하기
    gen_group = df['co_survey'].groupby(df['coNum']).count()
    #그룹에 인덱스에 이름 정의하기
    gen_group.index = ['스타벅스','커피빈','이디아','탐앤탐스']
    
    #막대그래프 그리기
    gen_group.plot.bar(color = ['red','green','blue','orange'],
                       width = 0.3)
    #제목 정의
    plt.title('커피샵 별 선호도', fontsize=40)
    plt.xlabel('커피샵', fontsize =30)
    plt.ylabel('선호도 건수', fontsize =30)
    #x축 y축에 들어가는 값들에 대한 폰트 사이즈 조정
    #rotation : 기울기 각도..
    plt.xticks(fontsize=20, rotation =70)
    plt.yticks(fontsize=20) 
    
    #그래프 저장하기
    fig.savefig('chi2app/static/frontendapp/images/chi2.png')

    
# Create your views here.
def view_Cart_List(request):
    
    df = cart.getCartList()
    
    context = {'df' : df}
    
    return render(
        request,
        'cart/cart_list.html',
        context
    )
    
def view_Cart(request):
    
    pcart_no = request.GET['pcart_no']
    pcart_prod = request.GET['pcart_prod']
    
    df_dict = cart.getCart(pcart_no, pcart_prod)
    
    # return HttpResponse(df_dict)
    
    return render(
        request,
        'cart/cart.html',
        df_dict
    )
#입력 폼(form)
def view_Cart_Insert(request):
    pcart_member = 'e001'
    pcart_prod = 'P102000001'
    return render(
        request,
        'cart/cart_insert_form.html',
        {'pcart_member':pcart_member,
         'pcart_prod':pcart_prod}
    )
    
def set_Cart_Insert(request):
    pcart_member = request.POST['pcart_member']
    pcart_prod = request.POST['pcart_prod']
    cart_qty = request.POST['cart_qty']
    
    msg = cart.setCartInsert(pcart_member, pcart_prod, cart_qty)
    
    pageControl = ''
    
    if msg == 'Y' :
        pageControl = '''<script>
                            alert('입력 되었습니다!!')
                            location.href='/db/cart_list_dict/'
                            </script>
        '''
    else :
        pageControl = '''<script>
                            alert('입력 실패!!')
                            history.go(-1)
                        </script>
        '''
    
    return HttpResponse(pageControl)
    # return render(
   
def testDict(request):
    context = {'dt' : [{'no1' : 1, 'no2' : 2, 'no3' : 3},
                       {'no1' : 4, 'no2' : 5, 'no3' : 6}]}
    # return HttpResponse(context)
    return render(
        request,
        'cart/testdict.html',
        context
    )
    
def view_Cart_List_dict(request):
    
    df_list = cart.getDictType_Cart()

    context = {'df_list' : df_list}
    
    return render(
        request,
        'cart/cart_list_dict.html',
        context
    )
    
def set_Cart_Delete(request):
    
    pcart_no = request.GET['pcart_no']
    pcart_prod = request.GET['pcart_prod']
    
    
    msg = cart.setCartDelete(pcart_no, pcart_prod)
    
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
    # pcart_no = request.GET['pcart_no']
    # pcart_prod = request.GET['pcart_prod']
    
    # msg = cart.setCartDelete(pcart_no, pcart_prod)
    
    # return render(
    #     request,
    #     'cart/cart_delete.html',
    #     {'msg' : msg}
    # )

# 업데이트할 내용 보여주기    
def view_Cart_Update(request):
    
    pcart_no = request.GET['pcart_no']
    pcart_prod = request.GET['pcart_prod']
    
    df_dict = cart.getCart(pcart_no, pcart_prod)
    
    # msg = cart.setCartDelete(cart_no, cart_prod)
    
    # context = {'pcart_no' : pcart_no, 
    #            'pcart_prod' : pcart_prod}
    
    df_dict['pcart_no'] = pcart_no
    df_dict['pcart_prod'] = pcart_prod
    
    return render(
        request,
        'cart/cart_update_form.html',
        df_dict
    )

# 수정처리
def set_Cart_Update(request):
    pcart_no = request.POST['pcart_no']
    pcart_prod = request.POST['pcart_prod']
    cart_qty = request.POST['cart_qty']
    
    msg = cart.setCartUpdate(pcart_no, pcart_prod, cart_qty)
    
    pageControl = ''
    
    if msg == 'Y' :
        pageControl = '''<script>
                            alert('수정 되었습니다!!')
                            location.href='/db/cart_list_dict/'
                            </script>
        '''
    else :
        pageControl = '''<script>
                            alert('수정 실패!!')
                            history.go(-1)
                        </script>
        '''
    
    return HttpResponse(pageControl)
    # return render(
    #     request,
    #     'cart/cart_update.html',
    #     {'msg' : msg}
    # )
#로그인 화면
def login_form(request):
     return render(
        request,
        'cart/login/login_form.html',
        {}
     )
     
def getlogin(request) :
    try:
        pmem_id = request.POST['mem_id']
        pmem_pass = request.POST['mem_pass']
        
    except:
        context = '''<script>
                        alert('직접 접근 하시면 안됩니다..@@ 로그인 페이지로 ')
                        location.href = '/oracle/login_form'
                    </script>'''
        return HttpResponse(context)
    #아이디 패스워드 확인 모델 호출(한건 조회)
    df_dict = login.getLogin(pmem_id,pmem_pass)
    
    
    #실패한 경우
    if df_dict['rs'] =='no' :
        context = '''<script>
                        alert('아이디 또는 패스워드를 확인하여 주세요!')
                        history.go(-1)
                    </script> '''
        return HttpResponse(context)
    
    # Session 처리 (회원 정보를 서버에 저장해 놓고 있는 상태)
    # -로그아웃 하기 전까지 회원 정보는 어느 페이지를 가든 살아 있습니다.
    # - request.session[]을 통해서 사용합니다.
    # - session에 저장되는 값들은 딕셔너리 형태로 저장됨..
    
    # sesstion 등록하기
    request.session['sMem_id'] = pmem_id
    request.session['sMem_name'] =df_dict['mem_name']
    
    #세션에 저장된 값 불러오기
    if request.session.get('sMem_id') :
        #세션에 값이 있는 경우..
        df_dict['sMem_id'] = request.session['sMem_id']
        df_dict['sMem_name'] = request.session['sMem_name']
    
    else :
        #세션에 값이 없는 경우
        df_dict['sMem_id'] = None
    df_dict['pmem_id'] = pmem_id
    df_dict['pmem_pass'] = pmem_pass
    
    
    return render(
        request,
        'cart/login/login_form.html',
        df_dict
     )
def set_Logout(request):
    #세션 정보 확인하기
    if request.session.get('sMem_id') :
        #세션정보 삭제하기
        request.session.flush()
        
        context = '''<script>
                        alert('로그아웃 되었습니다.')
                        location.href = '/db/login_form/'
                    </script>'''
        return HttpResponse(context)
    
    else :
        context = '''<script>
                            alert('직접 접근 하시면 안됩니다..@@ 로그인 페이지로 이동.')
                            location.href = '/db/login_login/'
                        </script>'''
      
#주문내역 전체조회 페이지처리                  
def view_Cart_List_Page(request) :
    #page_contrl/cart_list_page.html
##페이지 처리 시작 >>>
        
    try :
        now_page = request.GET.get('page')
        now_page = int(now_page)    
    
    except :
        now_page = 1
##페이지 처리 끝<<<<      

    
#모델 조회
    df_list = cart.getDictType_Cart()

#페이지 처리 시작>>>
#-첫번째 값은 모델 조회한 데이터
#-두번째 값은 한페이지에 보여줄 행의 갯수
    p = Paginator(df_list, 10)
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
        'cart/page_control/cart_list_page.html',
        context
    )
    
def sample_01(request):
    return render(
        request,
        'frontendapp/01_sample.html',
        {}
    )
    
def index_01(request):
    return render(
        request,
        'frontendapp/01_index.html',
        {}
    )
    
def index_02(request):
    return render(
        request,
        'frontendapp/02_index_css.html',
        {}
    )
    
def index_03(request):
    return render(
        request,
        'frontendapp/03_index_css.html',
        {}
    )
    
def index_04(request):
    return render(
        request,
        'frontendapp/04_index_css.html',
        {}
    )
    
def index_05(request):
    return render(
        request,
        'frontendapp/05_index_css.html',
        {}
    )
    
def index_06(request):
    return render(
        request,
        'frontendapp/06_index_css.html',
        {}
    )
    
