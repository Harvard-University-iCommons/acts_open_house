from django.shortcuts import render

# Create your views here.


def index(request):
    attendees = [
        'Jaime Bermudez',
        'Ethan Kiczek',
        'Colin Murtaugh',
        'Test Person',
        'Anthony Moulen',
        'Rose Nyameke'
    ]
    context = {
        'attendees': attendees
    }
    return render(request, 'deployment_demo/index.html', context)
