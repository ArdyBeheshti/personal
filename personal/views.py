from django.shortcuts import render

def post_list(request):
    return render(request, 'personal/post_list.html', {})
