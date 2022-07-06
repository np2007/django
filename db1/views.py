from django.shortcuts import render
from .models import Customer,CustomerForm

# Create your views here.
def show(request):
    if request.method=='POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            id=form.cleaned_data.get('id')
            name=form.cleaned_data.get('name')
            form.save()
    form=CustomerForm()
    return render(request,'info/information.html',{'form':form})

def display(request):
    data=Customer.objects.all()
    return render(request,'info/display.html',context={'data':data})