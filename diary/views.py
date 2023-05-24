from django.shortcuts import render, redirect
from .models import Diary
from .forms import DiaryForm
# Create your views here.

def diary_list(request):
    diarys = Diary.objects.all().order_by('created')
    return render(request, 'diary/diary_list.html', {'diarys':diarys})

def diary_detail(request, pk):
    diary = Diary.objects.get(id=pk)
    return render(request, 'diary/diary_detail.html', {'diary':diary})

def diary_post(request): 
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.save()
            return redirect('diary_list')
    else:
        form = DiaryForm()
    return render(request, 'diary/diary_post.html', {'form': form})

def diary_edit(request, pk):
    diary = Diary.objects.get(id=pk)
    if request.method == "POST":
        form = DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.save()
            return redirect('diary_list')
    else:
        form = DiaryForm(instance=diary)
    return render(request, 'diary/diary_post.html', {'form': form})

def diary_delete(request, pk):
    diary = Diary.objects.get(id=pk)
    diary.delete()
    return redirect('diary_list')
    