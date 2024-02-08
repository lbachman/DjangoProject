from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from django.http import JsonResponse


# get request
def GetMembers(request):

    mymembers = Member.objects.all()

    # Pass the members to the template context
    context = {
        'members': mymembers,
    }
    # Render the template with the context
    return render(request, 'members/index.html', context)

from django.contrib.auth.models import User
from django.http import JsonResponse

def GetMemberByUserName(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        if username:
            try:
                user = User.objects.get(username=username)
                user_data = {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    # Add more fields as needed
                }
                return JsonResponse(user_data)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
        else:
            return JsonResponse({'error': 'Username parameter is missing'}, status=400)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
