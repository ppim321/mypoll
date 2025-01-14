# account/forms.py
## Form/ModelForm 클래스들을 정의
## - 입력 폼당 하나씩 생성. 보통 등록폼 용, 수정폼 두가지를 만든다.

# Form
# class MyForm(forms.Form): # 상속 받아서 만듦

# ModelForm
# class MyModelForm(forms.ModelForm): # 상속 받아서 만듦

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserChangeForm
# UserChangeForm - 사용자 등록/생성 폼
# UserChangeForm - 사용자 정보 수정 폼. 둘다 ModelForm

from .models import User
from django.contrib.auth.forms import UserCreationForm

# 사용자 가입(등록)시 사용할 Form을 구성 - UserCreationForm 상속(username, pw1, pw2) + 추가항목
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User    # User model의 Field를 이용해서 form field 를 구성.
        # fields = "__all__" # 모델의 모든 field들을 사용해서 form field구성
        fields = ['username', 'password1', 'password2', 'name', 'email', 'birthday', 'porfile_img']  # form field로 구성할 것들을 명시.
        # exclude = ["필드명"] # 지정한 필드명을 제외한 나머지 필드로 form필드를 구성함.
        # fields와 exclude는 같이 설정할 수 없다.

        # input type을 변경 -> Widget
        ### {"field이름":Widget객체}
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),  #<input type=date>
            # "name": forms.PasswordInput() 한글일때는 사용불가.

        }
    # ModelForm에서 기본 검증을 처리
    ## name: required
    ## email: required, email형식 체크
    ## birthday: 날짜 형식 체크
    
    # 사용자 정의 검증(Form을 만들경우 Form에서 작성.)
    #  - clean(), clean_검증필드명()
    ## name 은 두글자 이상 입력
    def clean_name(self):
        # self.cleaned_data: dict - 기본 검증을 통과한 요청 파라미터들.
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise forms.ValidationError("이름은 2글자 이상 입력하세요.")
        return name # 리턴해주는 값의 view가 사용하는 값.

# 회원정보 수정 Form 정의 - UserChangeForm(Username) 상속
class CustomUserChangeForm(UserChangeForm):

    password = None # password 변경 페이지 링크가 안나오도록함.
    class Meta:
        model = User
        fields = ['name', 'email', 'birthday', 'porfile_img']
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
        }

    # name Field 검증 메소드
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise forms.ValidationError("이름은 2글자 이상 입력하세요.")
        return name