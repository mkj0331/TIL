from rest_framework.decorators import api_view
from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
# urls.py에서 주소창 마지막에 articles 이후로 비어있으면 이 클래스로 넘어오도록 설정해놓음
def article_list(request): 
    if request.method == 'GET':
        articles = Article.objects.all() # 내 DB에 있을 전체 게시물 정보를 가져옴
        serializer = ArticleListSerializer(articles, many=True)  #
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data) # GET할 때는 키워드 인자로 받을 필요 없음
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
# urls.py에서 주소창 마지막에 정수를 입력하면 그 정수를 밑의 매개변수인 
# article_pk로 적용한 아래 클래스로 넘어오도록 설정해놓음
def article_detail(request, article_pk):

    # 아래의 object는 게시글들에 대한 정보를 가져오는 매니저
        # 역참조 : 나를 참조하고 있는 데이터를 가져오는 매니저
            # 역참조 이름 : 댓글 클래스 명의 소문자 + _set ('comment_set')
            # 이건 당연히 댓글에 의해 참조당하는 게시글의 입장에서 자신을 참조하는 댓글을 가져올 때 사용하는 것
    article = Article.objects.get(pk=article_pk)
   

    if request.method == 'GET': # 조회할거야
        serializer = ArticleSerializer(article) 
        # 알았어, 지금 위에서 받아온 매개변수 인자에 해당하는 Article 클래스 내에 있는 데이터를 
        # 너가 쓰기 좋게 직렬화해서 가져올게
        return Response(serializer.data) # 가져온거 반환할게
    
    elif request.method == 'DELETE': # 삭제할거야
        article.delete() # 삭제? 삭제는 굳이 직렬화할 필요 없지? 그냥 바로 삭제할게
        return Response(status=status.HTTP_204_NO_CONTENT)  # 삭제 완료됐다는 것만 반환할게
    
    elif request.method == 'PUT':  # 수정할거야
        # 조회해온 데이터(article)를 저쪽에서 받아온 데이터로 수정해서 직렬화 할게
        # 그래서 인자 두개 필수! 이전에 조회했던 데이터와, request에서 받아온 대체(수정)할 데이터
        serializer = ArticleSerializer(article, data=request.data)
        # 가져온게 유효하면
        if serializer.is_valid(raise_exception=True):
            serializer.save() # 수정한 걸로 DB에 새로 저장할게
            return Response(serializer.data) # 수정된 결과 반환할게

# 댓글 생성
@api_view(['POST'])
def comment_create(request, article_pk):
    # 게시글을 하나 지정해서, 그곳에 댓글을 생성한다.
    article = Article.objects.get(pk=article_pk)
    # 댓글 생성은, 사용자가 보낸 댓글의 content 정보를 저장한다.
        # 사용자가 요청보낸 정보를 토대로 직렬화
    serializer = CommentSerializer(data=request.data)
    # 유효성을 검사한다.
        # 유효하지 못한 경우, 예외 상황을 알아서 발생시켜라
    if serializer.is_valid(raise_exception=True):
        # DB에 반영한다.
            # 저장하려고 할 때, article 정보가 누락되지 않도록 article = article 입력
        serializer.save(article = article)
        # 완성된 댓글 정보를 사용자에게 반환한다.(JSON)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 모든 댓글 조회
@api_view(['GET'])
def comment_list(request):
   pass

# 댓글 pk 값으로 조회, 삭제, 수정
@api_view(['GET'])
def comment_detail(request, comment_pk):
    pass
   

