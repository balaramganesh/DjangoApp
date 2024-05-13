from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserInputForm

# Create your views here.from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello, world. You're at the home page. Welcome!")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def input_view(request) :
    if (request.method=='POST') :
        form = UserInputForm(request.POST)
        if form.is_valid() :
            # text_input = form.cleaned_data['text_input']
            # UserInput.objects.create(text_input=text_input)
            form.instance.save(using='sqlite3')
            return redirect('success_page')
    else :
        form = UserInputForm()

    return render(request,'input_form.html',{'form':form})

# def input_order(request) :
#     if (request.method=='POST') :
#         form = OrdersForm(request.POST)
#         if form.is_valid() :
#             # text_input = form.cleaned_data['text_input']
#             # UserInput.objects.create(text_input=text_input)
#             form.instance.save(using='mysql')
#             return redirect('success_page')
#     else :
#         form = OrdersForm()

#     return render(request,'input_form.html',{'form':form})

def success_page(request) :
    return render(request,'success_page.html')