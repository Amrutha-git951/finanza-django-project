from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def service(request):
    return render(request, 'core/service.html')

def team(request):
    return render(request, 'core/team.html')

def feature(request):
    return render(request, 'core/feature.html')

def mycv(request):
    return render(request, 'core/mycv.html')

def project(request):
    return render(request, 'core/project.html')

def testimonial(request):
    return render(request, 'core/testimonial.html')
def error_404(request):
    return render(request, 'core/404.html')



