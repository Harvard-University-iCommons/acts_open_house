from django.shortcuts import render

# Create your views here.


def index(request):
    attendees = [
        'Colin Murtaugh',
    ]
    context = {
        'attendees': attendees
    }
    return render(request, 'deployment_demo/index.html', context)
