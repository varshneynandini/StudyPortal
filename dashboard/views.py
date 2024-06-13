from django.shortcuts import render
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def notes(request):
    form = NotesForm()
    # get all the notes of login user in notes object and pass this object using context to template file
    notes = Notes.objects.filter(user = request.user)
    context = {'notes':notes, 'form':form}
    return render(request, 'dashboard/notes.html', context)
