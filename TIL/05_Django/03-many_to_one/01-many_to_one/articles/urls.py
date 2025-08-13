from django.urls import path
from . import views

urlpatterns = [
    # 아래 path의 빈 란은, 121:8000/articles(현재파일경로)/ 이거 다음으로 온 거에 대해선 
    # 두 번째 매개변수에 해당하는 views의 class인 article_list로 처리하겠다
    path('', views.article_list),

    # articles/ 아래에 정수를 입력하면 그 정수를 views.py의 article_detail의 함수에서 지정한
    # 매개변수로 넘겨서 그 함수로 넘어가도록 하겠다.
    path('<int:article_pk>/', views.article_detail),

    # 위와 동일
    path('<int:article_pk>/comments/', views.comment_create),
    # path('comments/', views.comment_list),
    # path('comments/<int:comment_pk>/', views.comment_detail),
]