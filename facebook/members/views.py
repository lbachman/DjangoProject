from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# # get request
# def GetMembers(request):

#     mymembers = Member.objects.all()

#     # Pass the members to the template context
#     context = {
#         'members': mymembers,
#     }
#     # Render the template with the context
#     return render(request, 'members/index.html', context)


# get request 
# returns list of members
# http://localhost:8000/members/
def GetMembers(request):

    if request.method == 'GET':
        
        members = Member.objects.all()
        members_data = []
        for i in members:
            member_data = {
                'first name': i.firstname,
                'last name': i.lastname,
                'username': i.username
            }
            members_data.append(member_data)
                    
        return JsonResponse(members_data, safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)


# get request
# returns member by username
# http://localhost:8000/members/byusername/?username=mjohnson

def GetMemberByUserName(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        if username:
            try:
                member = Member.objects.get(username=username)
                member_data = {

                    'first name: ': member.firstname,
                    'last name: ': member.lastname,
                    'username': member.username
                }
                return JsonResponse(member_data)
            except Member.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
        else:
            return JsonResponse({'error': 'Username parameter is missing'}, status=400)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)


# post request
# adds a member and returns json response
# http://localhost:8000/members/add/
    
@csrf_exempt  # Add this decorator to exempt the view from CSRF protection    
def AddMember(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        
        # Validate the required fields
        required_fields = ['firstname', 'lastname', 'username']
        for field in required_fields:
            if field not in data:
                return JsonResponse({'error': f'Missing required field: {field}'}, status=400)
            
        try:
            member = Member.objects.create(
                firstname=data['firstname'],
                lastname=data['lastname'],
                username=data['username']
            )

            return JsonResponse({'success': 'User created successfully'}, status=201)
        except Exception as e:

            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Unsupported method'}, status=405)    