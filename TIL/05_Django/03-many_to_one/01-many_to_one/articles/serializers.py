# articles/serializers.py

from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer): # 직렬화
    class Meta:
        model = Article # 여기서 Article은 models.py에서 정의한 class임(title, content, ...)
        exclude = ('created_at', 'updated_at',) # 이 두개 빼고 가져옴


# 게시글 조회 할 때 해당 게시글의 댓글도 함께 조회
class ArticleSerializer(serializers.ModelSerializer):
    # class CommentDetailSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Comment
    #         fields = ('id', 'content',)   # 댓글의 id와 content만 보여준다.

    # read_only=True 옵션을 통해 해당 필드를 읽기 전용으로 설정할 수 있다.
    # comment_set = CommentDetailSerializer(many=True, read_only=True) # related_name을 통해 역참조
    # 댓글 갯수 표시
    # num_of_comments = serializers.SerializerMethodField()


    class Meta:
        model = Article
        fields = '__all__'
        # # fields = ('id', 'title',)
        # exclude = ('created_at', 'updated_at',)

    # def get_num_of_comments(self, obj):
    #     # 여기서 obj는 Serializer가 처리하는 Article 인스턴스
    #     # view에서 annotate 한 필드를 그대로 사용 가능
    #     return obj.num_of_comments


# 댓글 조회 시 게시글 정보도 함께 조회
class CommentSerializer(serializers.ModelSerializer):
    # 이 코멘트 시리얼라이저의 어떤 특정한 필드(article)를 다른 형태로 재정의
    # id랑 title을 보여주고 싶다!
        # 1. id랑 title만 보여주는 serializer를 따로 정의하기
            # 이 정의하는 serailizer는 이 클래스 안에서만 쓸 거 같으니까, 이 클래스 내에서 정의해버리자
        # 2. 이미 있는 serializer를 사용하기
    class ArticleForCommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'title')
    article = ArticleForCommentSerializer(read_only = True)

    class Meta:
        model = Comment
        # 사용자는 article, updated_at, created_at 이런거 볼 필요도, 입력할 필요도 없음. 따라서 fields에 content만 하면 됨
            # 참고 : tuple에 요소 1개일때, trailing comma 찍어야 함(안찍으면 그냥 소괄호됨)
        # fields = ('content',)
        # 위처럼 하면 댓글을 입력했을때, 자신이 입력한 댓글만 보여지게 됨
            # 나는 내가 입력한 댓글에 대한, 댓글이 참조하고 있는 article의 정보도 같이 보여지게 하고싶음
            # 근데, 내가 그 article의 정보를 댓글 쓸 때 같이 입력하긴 귀찮음
            # -> 일단 field에 다 가져오고, read_only_field
        fields = '__all__'
        # read_only_fields = ('article',)