from django.shortcuts import render
from django.views.generic import (FormView,TemplateView)
from myapp.models import Contact
from myapp.forms import ContactForm
from django.views import View
# Create your views here.
# class HomePage(TemplateView):
#     template_name = 'index.html'
# class HomePage(View):
#     def get(self,request):
#         form = ContactForm
#         context = {'form' : form}
#         return render(request,'index.html',context)
#     def post(self,request):
#         form = CarForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['name'])
#             form.save()
#         context = {'form' : form}
#         return render(request,'index.html',context)


def HomePage(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # return HomePage(request)
            # form = ContactForm()
        else:
            print('error')

    return render(request,'myapp/index.html',{'form':form})
