from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count
from django.shortcuts import render
from .models import Author
from .serializers import AuthorSerializer

# Create your views here.
@api_view(['GET'])
def author_detail(request, author_pk):
    # 저자 한명에 대한 상세 정보를 반환할 것
        # 직렬화 필요 -> Seraiilizer 정의하러 가자.
    author = Author.objects.get(pk=author_pk)
    # book_count라고 하는 새로운 필드를 만들건데
    # 거기에, 나를 참조하고 있는 book들의 총 수 (집계 함수)
    author = Author.objects.annotate(book_count = Count('book')).get(pk=author_pk)
    print(author.book_count)
    # 나를 참조중인 N들을 불러오려면?
    # 역참조 매니저를 통해 어떠한 정보를 얻을 수 있음
    # print(author_pk, author.name, len(author.book_set.all()))
    serializers = AuthorSerializer(author)
    return Response(serializers.data)

