from django.http import Http404
from django.shortcuts import render

from bracket.models import Match

def index(request):
    return render(request, "index.html", {}) 

def tournament(request, tournament_id):
    match_list = Match.objects.filter(tournament=tournament_id)
    if len(match_list) == 0:
        raise Http404
    context = {'match_list' : match_list}
    return render(request, 'tournament.html', context)

