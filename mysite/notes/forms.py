#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-12 17:17
# @Author  : Yijie Yuan
# @Site    : 
# @File    : forms.py
# @Software: PyCharm

# from django import forms
# from .models import File


# Model form
# class FileUploadModelForm(forms.ModelForm):
#     class Meta:
#         model = File
#         fields = ('file', )
#
#         widgets = {
#             'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
#         }
#
#     def clean_file(self):
#         file = self.cleaned_data['file']
#         ext = file.name.split('.')[-1].lower()
#         if ext not in ["jpg", "pdf", 'md', 'png', ]:
#             raise forms.ValidationError("Wrong file type!")
#         # return cleaned data is very important.
#         return file
