from django.shortcuts import render, redirect  # Added render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('home')  # You can define a 'home' route or change it
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})