from django.shortcuts import render

def calendar(request):
    return render(request, 'general/change_list.html')
