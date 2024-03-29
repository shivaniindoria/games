import random
from django.shortcuts import render
from .forms import Form

def GuessWord(request):
    submitted = False
    name = None
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            submitted = True
            # Do something with the data, like saving to a database
    else:
        form = Form()
    return render(request, 'index.html',{'name':name,'form': form,'submitted':submitted} )
    # return render(request,'index.html')
