from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

def members(request):
    # Retrieve all members from the database
    mymembers = Member.objects.all()

    # Pass the members to the template context
    context = {
        'members': mymembers,
    }

    # Render the template with the context
    return render(request, 'members/index.html', context)