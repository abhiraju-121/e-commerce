from django.shortcuts import render
from gameapp.models import Product
from django.db.models import Q
# Create your views here.
def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contain=query) | Q(description__contain=query))
    return render(request,'search.html',{'qurey':query,'products':products})
