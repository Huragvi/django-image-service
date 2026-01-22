from django.shortcuts import render, redirect, get_object_or_404
from .models import Image

def upload_page(request):
    if request.method == "POST":
        file = request.FILES["file"]
        Image.objects.create(
            original_name=file.name,
            file=file,
            content_type=file.content_type,
            size=file.size
        )
        return redirect("/images/list/")
    return render(request, "images/upload.html")

def list_page(request):
    images = Image.objects.all()
    return render(request, "images/list.html", {"images": images})

def view_page(request, uuid):
    image = get_object_or_404(Image, uuid=uuid)
    return render(request, "images/view.html", {"image": image})

def delete_page(request, uuid):
    image = get_object_or_404(Image, uuid=uuid)
    if request.method == 'POST':
        image.delete()
        return redirect('image-list')
    return render(request, "images/delete_page.html", {'image': image})