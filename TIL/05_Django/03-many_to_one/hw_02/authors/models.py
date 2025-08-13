from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)

    # print 방법 바꾸는법 (허균이 object가 아니라 허균으로 보이게)
    def __str__(self):
        return self.name