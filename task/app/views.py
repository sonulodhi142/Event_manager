from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

# Create your views here.

from .models import Event, EventRegistration

def Home(req):
    return render(req, 'home.html')

def events(req):
    Events = Event.objects.all()
    return render(req, 'events.html', {'events': Events})

def proposal(req):
    if req.method == 'POST':
        event = req.POST.get('event')
        date = req.POST.get('date')
        venue = req.POST.get('venue')
        image = req.FILES.get('image')
        Event.objects.create(event=event, date=date, vanue=venue, image=image)
        return redirect('succes')
    return render(req, 'proposal.html')

def succes(req):
    return render(req, 'succes.html')



def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        event_name = request.POST.get('eventName')

        # Save data to the model
        student = EventRegistration.objects.create(name=name, email=email, event_name=event_name)
        student.save()
        return redirect('regsucces') 
    return render(request, 'register.html')

def regsucces(req):
    return render(req, 'regsucces.html')

def Delete(req, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    return redirect('events') 

def Edit_event(req, id):
    event = get_object_or_404(Event, id=id)
    if req.method == 'POST':
        event.event = req.POST.get("event")
        event.date = req.POST.get("date")
        event.vanue = req.POST.get("venue")
        event.image = req.FILES.get('image')
        event.save()
        return redirect('events')
    return render(req, 'proposal.html', {'event': event})



