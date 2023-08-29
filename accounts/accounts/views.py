from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required


def accounts(request):
    return render(request, 'accounts/welcome.html',{'today': datetime.today()})

@login_required
def authorized(request):
    return render(request, 'accounts/authorized.html',{})