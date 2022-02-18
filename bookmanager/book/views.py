from django.shortcuts import render

# Create your views here.

# 视图函数
# 参数1 接受请求 HttpRequest对象
# 必须返回 相应对象 数据


from django.http import HttpRequest
from django.http import HttpResponse

def index(request):

    # return HttpResponse('ok')
    # 渲染 参数1 。请求。 模板名称

    context = {
        'name' : '马上双11，点击有惊喜'
    }
    return render(request,'book/index.html',context=context)