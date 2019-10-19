
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
from operator import itemgetter


def notes_index(request):
    note_set = Note.objects.all().order_by('title')

    category_set = []
    for note in note_set:
        if note.category not in category_set:
            category_set.append(note.category)
    category_set.sort(key=str.lower)

    sup_category_set = []
    sup_category_number = 1
    for note in note_set:
        category_list = []
        category_number = 1
        if note.sup_category not in [item['name'] for item in sup_category_set]:
            for note_sup in Note.objects.filter(sup_category=note.sup_category):
                note_list = []
                if note_sup.category not in [item['name'] for item in category_list]:
                    for note_cat in Note.objects.filter(category=note_sup.category).order_by('-pub_date')[:5]:
                        note_list.append({'title': note_cat.title,
                                          'category': note_cat.category,
                                          'slug': note_cat.slug})

                    category_list.append({'id': category_number,
                                          'name': note_sup.category,
                                          'note_list': note_list})
                    category_number += 1
            category_list.sort(key=itemgetter('id'))
            sup_category_set.append({'id': sup_category_number,
                                     'name': note.sup_category,
                                     'category_list': category_list})
            sup_category_number += 1
    sup_category_set.sort(key=itemgetter('id'))

    print(sup_category_set)

    context = {}
    for category in category_set:
        context[category] = Note.objects.filter(category=category).order_by('-pub_date')[:5]
    context['category_set'] = category_set
    context['sup_category_set'] = sup_category_set

    return render(request, 'notes/index.html', context=context)


def notes_list(request, category):
    note_set = Note.objects.filter(category=category).order_by('title')
    sub_category_set = []
    for note in note_set:
        if note.sub_category not in sub_category_set:
            sub_category_set.append(note.sub_category)
    sub_category_set.sort(key=str.lower)
    return render(request, 'notes/list.html', {'note_list': note_set,
                                               'sub_category_set': sub_category_set,
                                               })


def notes_detail(request, category, notes_slug):
    note = get_object_or_404(Note, category=category, slug=notes_slug)
    return render(request, 'notes/detail.html', {'note': note})


