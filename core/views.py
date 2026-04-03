from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .forms import EnquiryForm
from .models import Enquiry, Coach, GalleryImage

def home(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your enquiry has been received. We will contact you soon!')
            return redirect('home')
    else:
        form = EnquiryForm()
    
    return render(request, 'home.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def gallery(request):
    images = GalleryImage.objects.all().order_by('-created_at')
    return render(request, 'gallery.html', {'images': images})

def coaches(request):
    coaches_list = Coach.objects.all().order_by('name')
    return render(request, 'coaches.html', {'coaches': coaches_list})

@staff_member_required
def enquiry_dashboard(request):
    enquiries = Enquiry.objects.all().order_by('-created_at')
    coaches_count = Coach.objects.count()
    images_count = GalleryImage.objects.count()
    return render(request, 'admin_panel.html', {
        'enquiries': enquiries,
        'coaches_count': coaches_count,
        'images_count': images_count,
        'active_tab': 'enquiries'
    })
