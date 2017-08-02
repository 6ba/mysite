from django.shortcuts import render
from .forms import FormTest
from django.http import HttpResponse

# Create your views here.
def index(request):
    # form = FormTest(initial={'t1': 1, "t2": 2})initial={'DatabaseType':'oracle',)
    form = FormTest()
    if request.method == 'GET':

        return render(request, 'test_form.html', {
            'form': form,
        })

    if request.method == 'POST':
        form = FormTest(request.POST)
        # 探究搜索关键词为空的内容// 搜素全部为 .
        if form.is_valid():

            t2= form.cleaned_data['t2']
            t1 = form.cleaned_data['t1']
            return HttpResponse(str(t1)+","+str(t2))
    return render(request, 'test_form.html', {'form': form})