from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def detail(request):
    return render(request, 'detail.html')
def price(request):
    return render(request, 'price.html')
def product(request):
    return render(request, 'product.html')
def service(request):
    return render(request, 'service.html')
def team (request):
    return render(request, 'team.html')
def testimonial(request):
    return render(request, 'testimonial.html')
