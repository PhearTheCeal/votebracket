from django.template import RequestContext, loader
from django.http import HttpResponse

from bracket.models import Tournament, Match

def index(request):
    return HttpResponse("This is the index")

def tournament(request, tournament_id):
    match_list = Match.objects.filter(tournament=tournament_id)
    template = loader.get_template('tournament.html')
    context = RequestContext(request, {
        'match_list' : match_list,    
    })
    return HttpResponse(template.render(context))

