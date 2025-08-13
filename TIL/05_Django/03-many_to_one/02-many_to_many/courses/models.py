from django.db import models
from teachers.models import Teacher


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    main_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    # ManyToManyField : 강의와 강사의 foreign키들을 저장해주는 테이블을 알아서 만들어줌
    # assistant_teachers = models.ManyToManyField(Teacher)
    
    # related_name : dust=50; dust=60 방지하기 위해 역참조 이름을 변경 <- 권장
    assistant_teachers = models.ManyToManyField(Teacher, related_name="assistant_courses")
    
    # through='CourseInfo'를 통해 중개모델인 CourseInfo를 통해 다 대 다 관계를 실현하겠다. <- 필수는 아님
        # 대신 중개모델을 아래처럼 따로 지정해줘야 함 
    # assistant_teachers = models.ManyToManyField(Teacher, related_name="assistant_courses", through='CourseInfo')


# 참조 : Through 참고  
# N:M 관계에서 추가적인 정보를 저장하고 싶은 경우에는 중개 모델을 사용할 수 있음 !
# 이 경우에는 중개 모델을 정의하고 through 옵션에 중개 모델을 지정하면 됨
# 중개모델에는 반드시 관계 설정을 원하는 두 모델을 ForeignKey로 지정해야 함 !
# class CourseInfo(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Course 모델과의 관계
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Teacher 모델과의 관계
#     max_student = models.PositiveIntegerField(default=20)
#     is_nessary = models.BooleanField(default=False)
    
#     class Meta:
#         unique_together = ('course', 'teacher')
