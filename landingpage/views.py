from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    username = request.POST.get('usern')
    password = request.POST.get('passn')
    with open('data.txt', 'r') as f:
        r = f.readline()
        while r:
            r = f.readline()
            if r == "":
                break
            if username == r.split()[0]:
                return render(request, "failure.html")
                break
    if username != None and password != None:
        with open("data.txt",'a') as f:
            f.write(f"{username} {password}\n")
        return render(request, "success.html")
    return render(request, "index.html")