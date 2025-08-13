from rest_framework import serializers
from .models import Author

'''

'''


class AuthorSerializer(serializers.ModelSerializer):
    # Author 모델을 토대로, 필드를 정의하라고 했으니,
    # annotate로 추가한 필드는 Serailizer가 처리할 수 없음!
    ## book_count 필드 정의하기
        # 정의하는 방법 2가지
        # 하나는 내가 직접 source 찾아서 때려박기
    # book_count = serializers.IntegerField(source='book_set.count', read_only=True)
    book_count = serializers.SerializerMethodField()
    # SerializerMethodField로 할당할 값을 정의할 메서드는
    # 그 get_필드명
    def get_book_count(self, obj):
        '''
            obj : 이 시리얼라이저를 호출한 객체 (아마 author 일듯)
        '''
        return obj.book_count
    
    class Meta:
        model = Author
        fields = '__all__'