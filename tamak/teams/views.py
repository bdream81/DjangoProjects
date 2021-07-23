from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView
from .models import Team

class TeamCreateView(CreateView):
    template_name='teams/team_list.html'
    model = Team
    fields = [       
        'user',
        'positions' ,
        'educations',
        'experience',
        'companies',
        'date_created'  
        ]

    

    def get_context_data(self, **kwargs):
        form = Team.objects.all
        kwargs['form'] = form
        return super().get_context_data(**kwargs)

    
        

        


        
    