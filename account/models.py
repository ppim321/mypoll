from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import forms

## 확장 User모델
# - AbstracUser로 구현: 기본 User(Username, password) 에 필드 들을 추가하는 방식
# - AbstracUser 상속. 필드들 정의(Username, password 빼고 정의)
class User(AbstractUser):
    # Field들 정의 - table컬럼
    name = models.CharField(
        verbose_name='이름',   # Form관련 설정(label) - Form의 ModelForm을 만들경우, form관련설정을 Model에 한다.
        max_length=50         # varchar(50)
    )
    email = models.EmailField(  # EmailField : varvhar(100) -> 값이 이메일 형식인지 (@가 있는지)를 검증.
        verbose_name='Email', 
        max_length=100,
    )
    birthday = models.DateField(
        verbose_name='생일',
        null=True, # Null 허용 (default: False - Not null)
        blank=True # Form - 필수가 아니다.  (default: False - required)
    )
    porfile_img = models.ImageField(
        verbose_name='프로필 사진',
        upload_to="images/%Y/%m/%d",    # 저장경로(media/지정한 경로)
        null=True,
        blank=True
    ) # 추가 -> python manage.py makemigrations, migrate
    
    def __str__(self):
        return f"uself.name: {self.username}, name: {self.name}"
    