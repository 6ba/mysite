from django import forms

class FormTest(forms.Form):
    t1 = forms.ChoiceField(choices=[('1','sqlserver'),('2','oracle'),('3','oracle3')])
    t2 = forms.ChoiceField(choices=[('sqlserver','1'),('oracle','2')])