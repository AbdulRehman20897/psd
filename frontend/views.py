from django.shortcuts import render, redirect
import requests, json

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}


def psd_view(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'phone': request.POST.get('phone'),
            'email': request.POST.get('email'),
        }

        response = requests.post('http://localhost:8000/form/', data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            return redirect('psd')

    return render(request, "frontend/psd.html")