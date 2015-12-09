from django.shortcuts import render

# Create your views here.


def index(request):
    attendees = [
        'Kevin Donovan',
        'Rebecca Miller',
        'Jaime Bermudez',
        'Ethan Kiczek',
        'Colin Murtaugh',
        'Test Person',
        'Anthony Moulen',
        'Rose Nyameke',
        'Annie Rota',
        'David Heitmeyer',
        'Hiu Kei Chow',
        'Angry Panda',
        'Yoda',
        'Rose is the best.',
        'Alan','Randy',
        'Marlee'
    ]
    context = {
        'attendees': attendees
    }
    return render(request, 'deployment_demo/index.html', context)
