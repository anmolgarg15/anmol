from django.shortcuts import render
from django.http import HttpResponse
from fileupload.forms import ProfileForm
from fileupload.models import Profile
def profile(request):
	return render(request,'profile.html')
def profilesave(request):
	saved=False
	if request.method=="POST":
		pf=ProfileForm(request.POST,request.FILES)
		if pf.is_valid():
			p=Profile()
			p.name=pf.cleaned_data["name"]
			p.picture=pf.cleaned_data["picture"]
			p.save()
			saved=True
		else:
			pf=ProfileForm()
		return render(request,'saved.html',locals())