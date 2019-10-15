
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Imaginary function to handle an uploaded file.


from django.http import HttpResponseRedirect


# Imaginary function to handle an uploaded file.

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
#from .forms import FileUploadModelForm


# model
from .models import Note

#
import markdown

# Upload File with ModelForm
# def model_form_upload(request):
#     if request.method == "POST":
#         form = FileUploadModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("/file/")
#     else:
#         form = FileUploadModelForm()
#
#     return render(request, 'notes/upload_form.html', {'form': form,
#                                                             'heading': 'Upload files with ModelForm'})


def notes_index(request):
    # notes_list = Note.objects.all()
    #Medical Physics
    mp500_list = Note.objects.filter(category='mp500').order_by('title')
    mp505_list = Note.objects.filter(category='mp505').order_by('title')
    mp530_list = Note.objects.filter(category='mp530').order_by('title')

    #Computal Tools
    django_list = Note.objects.filter(category='django').order_by('title')
    git_list = Note.objects.filter(category='git').order_by('title')
    mac_list = Note.objects.filter(category='mac').order_by('title')
    matlab_list = Note.objects.filter(category='matlab').order_by('title')
    mysql_list = Note.objects.filter(category='mysql').order_by('title')
    python_list = Note.objects.filter(category='python').order_by('title')
    shell_list = Note.objects.filter(category='shell').order_by('title')
    software_list = Note.objects.filter(category='software').order_by('title')

    context = {'mp500_list': mp500_list,
               'mp505_list': mp505_list,
               'mp530_list': mp530_list,

               'django_list': django_list,
               'git_list': git_list,
               'mac_list': mac_list,
               'matlab_list': matlab_list,
               'mysql_list': mysql_list,
               'python_list': python_list,
               'shell_list': shell_list,
               'software_list': software_list,
               }
    return render(request, 'notes/index.html', context=context)


def notes_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/notes_detail.html', {'note': note})


