from django.shortcuts import render, redirect
from .models import CounterModel

# Create your views here.
def home(request):
    obj = CounterModel.objects.filter(id=1)[0]
    number = obj.number
    context ={
        'number': number,
    }
    return render(request, 'counterapp/index.html', context=context)

# Increment the number
def increment(request):
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = int(obj.number) + 1
    obj.save()
    return redirect('home')

# Decrement the number
def decrement(request):
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = int(obj.number) - 1
    obj.save()
    return redirect('home')

# Reset the number to zero
def reset(request):
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = 0
    obj.save()
    return redirect('home')