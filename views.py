from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def home(request):
    all_inks = InkColor.objects.all().order_by('series', 'pantone')
    all_series = Series.objects.all()
    context = {
        'all_inks': all_inks,
        'all_series': all_series,
    }
    return render(request, 'inkbook/home.html', context)