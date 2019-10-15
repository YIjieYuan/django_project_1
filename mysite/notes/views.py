
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
    notes_list = Note.objects.all()
    django_list = Note.objects.filter(category='django')
    mp500_list = Note.objects.filter(category='mp500')
    mp530_list = Note.objects.filter(category='mp505')
    mp530_list = Note.objects.filter(category='mp530')

    context = {'notes_list': notes_list,'django_list': django_list, 'mp530_list': mp530_list}
    return render(request, 'notes/index.html', context=context)


def notes_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/notes_detail.html', {'note': note})


