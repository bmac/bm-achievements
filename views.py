from django.shortcuts import render_to_response, get_object_or_404
from bm-achievements.models import Achievement
from django.template import RequestContext

def achievements_all(request):
    queryset = Achievement.objects.all().order_by("xp")
    return render_to_response("achievements/achievement_list.html", locals(),  context_instance=RequestContext(request))


def achievement(request, slug):
    achievement = get_object_or_404(Achievement, slug=slug)
    return render_to_response('achievements/achievement.html', locals(),  context_instance=RequestContext(request))
    
