from django import forms
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class LoginForm(forms.Form):
    uid = forms.CharField(label='用户名',
                          widget=forms.TextInput(
                              attrs={'class': 'form-control',
                                     'id': 'uid',
                                     'placeholder': '用户名登录'})
                          )

    pwd = forms.CharField(label='密码',
                          widget=forms.PasswordInput(
                              attrs={'class': 'form-control',
                                     'id': 'pwd',
                                     'placeholder': 'Password'})
                          )



@python_2_unicode_compatible
class RegisterForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'id': 'name',
               'placeholder': '请输入姓名'}))
    phone = forms.CharField(label='手机号', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'id': 'phone',
               'placeholder': '请输入手机号'}))

    password1 = forms.CharField(label='密码', widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'id': 'password1',
               'placeholder': '请输入密码不要包含非法字符'}))
    password2 = forms.CharField(label='与上同密码', widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'id': 'password1',
               'placeholder': '请再次输入密码'}))
    danwei = forms.CharField(label='单位', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'id': 'danwei',
               'placeholder': '请输入单位'}))
    zhiwu = forms.CharField(label='职务', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'id': 'zhiwu',
               'placeholder': '请输入职务'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'id': 'email',
               'placeholder': '请输入你的邮箱'}))



