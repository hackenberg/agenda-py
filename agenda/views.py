from agenda.models import Course

from django.shortcuts import render_to_response, get_object_or_404

from django.template import RequestContext

def index(request):
    course_list = Course.objects.all()
    return render_to_response('agenda/index.html', {'course_list': course_list})

def detail(request, course_id):
    c = get_object_or_404(Course, pk=course_id)
    return render_to_response('agenda/detail.html', {'course': c},
                               context_instance=RequestContext(request))
