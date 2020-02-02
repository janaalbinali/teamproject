from django.shortcuts import render, redirect
from .models import Team, Member
from .forms import TeamForm, MemberForm


# Create your views here.

def team_list(request):
    teams = Team.objects.all()
    context ={
        "teams":teams
    }
    return render(request, "team_list.html", context)

def team_create(request):
    form = TeamForm()
    if request.method =="POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team-list')
    context = {
        "form":form
    }
    return render(request, 'create_team.html', context)
def member_list(request):
    members = Member.objects.all()
    context ={
        "members":members
    }
    return render(request, "member_list.html", context)

def member_create(request):
    form = MemberForm()
    if request.method =="POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member-list')
    context = {
        "form":form
    }
    return render(request, 'create_member.html', context)