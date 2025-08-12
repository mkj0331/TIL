
'''
문제
Django REST Framework를 사용하여 SNS 게시글을 관리하는 API를 구현하시오.
게시글 모델은 아래 내용을 참고하며, ModelSerializer를 사용하여 Serializer를 정의하시오.
Post 모델 : SNS의 게시글을 저장하기 위해 정의된 데이터베이스 모델로, 다음과 같은 필드로 구성된다.
    title: 게시글의 제목을 저장하는 필드입니다. 최대 100자의 문자열을 저장할 수 있다.
    content: 게시글의 내용을 저장하는 필드입니다. 긴 텍스트를 저장할 수 있다.
    created_at: 게시글이 생성된 시간을 저장하는 필드다. 자동으로 현재 시간이 설정되며, 수정할 수 없다.
    updated_at: 게시글이 마지막으로 수정된 시간을 저장하는 필드다. 자동으로 현재 시간이 설정되며, 게시글이 수정될 때마다 갱신된다.

요구사항
새로운 가상 환경을 생성하고, 가상 환경을 활성화하시오.
활성화된 가상환경에서 제공된 requirements.txt를 활용하여 패키지들을 설치하시오.
Django 프로젝트와 posts 앱을 생성하고 필요한 설정을 작성하시오.
게시글 모델을 정의하고, 마이그레이션을 수행하시오.
ModelSerializer를 사용하여 게시글 모델의 시리얼라이저 클래스를 작성하시오.
'''

from rest_framework import serializers
from .models import Post

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
