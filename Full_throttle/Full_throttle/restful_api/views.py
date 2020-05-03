from django.shortcuts import render
import json

def home(request):

    #### READ FILE
    # Opening JSON file 
    with open('Test JSON.json') as f:   
        data = json.load(f) 
    print(data)
    
    return render(request, 'home.html', {
        'DATA': data['members'],
    })
