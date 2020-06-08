from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .forms import TutorialForm
from .models import Tutorial


def tutorialList(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/list.html', { 'tutorials' : tutorials})


def uploadTutorial(request):
    if request.method == 'POST':  
        form = TutorialForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('tutorial_list')
    else:
        form = TutorialForm()
    return render(request, 'tutorial/upload.html', {'form' : form})

def editTutorial(request,pk):
    tutorials = Tutorial.objects.get(id=pk)
    return render(request,'tutorial/update.html',{'t':tutorials})


def updateTutorial(request,pk):
    tutorials = Tutorial.objects.get(id=pk)
    form = TutorialForm(request.POST,request.FILES,instance=Tutorial)
    if form.is_valid():
        #form.feature_image = form.changed_data['feature_image']
        #form.attachment = form.changed_data['attachment']

        form.save()
        return HttpResponse('done')
    else:
        return HttpResponse('not done')
    #return render(request,'tutorial/update.html',{'t':tutorials})


def deleteTutorial(request, pk):
    if request.method == 'POST':
        tutorial = Tutorial.objects.get(pk=pk)
        tutorial.delete()
    return redirect('tutorial_list')
