from django.shortcuts import render,redirect
from .forms import FunUploadForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Upload
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    context = {
      'wars' : Upload.objects.all()
    }
    print(wars)
    return render(request, 'fun/home.html', context)

class WarListView(ListView):
    model = Upload
    paginate_by = 1
    template_name = 'fun/home.html'
    context_object_name = 'wars'
    ordering = ['-date_posted']

def upload(request):
    if request.method == 'POST':
        #print(request.POST.get('your_video'))
        #print(request.POST.get('opponent_video'))
        #Upload.objects.create(your_name=request.POST.get('your_name'),
        #     opponent_name=request.POST.get('opponent_name'),
        #     your_video=request.POST.get('your_video'),
        #     opponent_video=request.POST.get('opponent_video'),
        #     creator=request.user
        #)
        form = FunUploadForm(request.POST, request.FILES, request.FILES)
        if form.is_valid():
            form.instance.creator = request.user
            form.save()

            messages.success(request, f'your video uploaded successfully')

    form = FunUploadForm()

    return render(request, 'fun/upload.html', {'form':form})

def add_like_your_video(request, query):
    uploads = Upload.objects.filter(id=query)
    likes = ''
    for upload in uploads:
        upload.your_video_likes += 1
        likes = upload.your_video_likes
        upload.save()
    data = {
      'likes':likes,
    }
    return JsonResponse(data);

def add_like_opponent_video(request, query):
    uploads = Upload.objects.filter(id=query)
    likes = ''
    for upload in uploads:
        upload.opponent_video_likes += 1
        likes = upload.opponent_video_likes
        upload.save()

    data = {
      'likes':likes,
    }
    return JsonResponse(data);

def detail(request, pk):
    uploads = Upload.objects.filter(pk=pk)
    title = ''
    for upload in uploads:
        title = upload.your_name + 'Vs' + upload.opponent_name
    return render(request, 'fun/detail.html', {'uploads':uploads, 'title':title})

class FunUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Upload
    fields = ['your_name', 'opponent_name', 'your_video', 'opponent_video']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        fun = self.get_object()
        if self.request.user == fun.creator:
            return True
        return False

class FunDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Upload
    success_url = '/'

    def test_func(self):
        fun = self.get_object()
        if self.request.user == fun.creator:
            return True
        return False

def fundetail(request, pk):
    return render(request, 'fun/fun_detail.html')

def yourUploads(request):
    wars = Upload.objects.filter(creator=request.user).order_by('-date_posted')
    paginator = Paginator(wars, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
      'wars':page_obj,
      'page_obj': page_obj
    }
    return render(request, 'fun/uploaded.html', context)
