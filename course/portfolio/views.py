from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render (request, 'index.html')

    my_content = {
       "my_text": "This is my design",
       "my number" : 1234,
       "my_list" : [123,12345, "ABC"]

      

    } 
