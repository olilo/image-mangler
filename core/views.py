# Create your views here.
from forms import UploadForm
from models import UploadedImage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = UploadedImage(name = form.cleaned_data['name'], file = form.cleaned_data['file'])
            image.save()
            return HttpResponseRedirect('/')
    else:
        form = UploadForm()

    return render(request, 'upload.html', {
        'form': form,
    })


def home(request):
    return render(request, 'home.html', {
        'image_list': UploadedImage.objects.all(),
    })
