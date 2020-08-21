from django.shortcuts import render
def articleList(request): 
    #   return HttpResponse('homepage')
    return render(request, 'article/articleList.html')