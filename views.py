from django.shortcuts import render_to_response, get_object_or_404
from bm-achievements.models import Achievement
from django.template import RequestContext

def achievements_all(request):

    return render_to_response("achievements/achievement_list.html", {
        "queryset" : Achievement.objects.all().order_by("xp")
    },  context_instance=RequestContext(request))


def achievement(request, slug):
    a = get_object_or_404(Achievement, slug=slug)
    
    return render_to_response('achievements/achievement.html', {'achievement': a},  context_instance=RequestContext(request))
    
