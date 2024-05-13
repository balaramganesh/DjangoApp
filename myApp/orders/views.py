from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .forms import OrdersForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the orders index.")

def input_order(request) :
    if (request.method=='POST') :
        form = OrdersForm(request.POST)
        if form.is_valid() :
            # text_input = form.cleaned_data['text_input']
            # UserInput.objects.create(text_input=text_input)
            form.instance.save(using='mysql')
            # return redirect('success_page')
            return render(request,'order_result.html',{'form':form})
    else :
        form = OrdersForm()

    return render(request,'input_form.html',{'form':form})

def success_page(request) :
    return render(request,'success_page.html')