from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# 외래키를 사용(참조)해서 N:1 관계 정의하기 (N=0일 수도 있음)
class Comment(models.Model):
    # Article class를 id를 기준으로 참조하는데, 
    # CASCADE : 내가 참조 중인 게시글이 삭제되면, 나도 삭제
        # class의 작성 순서 상관없게 Article클래스를 사용하기 위해 그냥 Article이 아닌,
        # 'articles.Article'(articles 아래의 Article 클래스 지명)로 바꿔서 쓰기
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
