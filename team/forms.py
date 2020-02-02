from django import forms
from .models import Team, Member

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'