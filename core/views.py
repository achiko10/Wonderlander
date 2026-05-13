from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import SiteSettings, Service, Chakra, Course, Retreat, ContactInfo
from .forms import LeadForm


def get_common_context(request):
    lang = request.session.get('lang', 'ge')
    try:
        contact = ContactInfo.objects.first()
    except ContactInfo.DoesNotExist:
        contact = None
    try:
        settings = SiteSettings.objects.first()
    except SiteSettings.DoesNotExist:
        settings = None
    return {'lang': lang, 'contact': contact, 'site_settings': settings}


def set_language(request, lang):
    if lang in ['ge', 'en']:
        request.session['lang'] = lang
    return redirect(request.META.get('HTTP_REFERER', '/'))


def home(request):
    context = get_common_context(request)
    context['services'] = Service.objects.filter(is_active=True)
    context['chakras'] = Chakra.objects.all()
    context['form'] = LeadForm()
    return render(request, 'core/home.html', context)


def course(request):
    context = get_common_context(request)
    course_obj = Course.objects.filter(is_active=True).first()
    context['course'] = course_obj
    if course_obj:
        context['packages'] = course_obj.packages.all()
    context['form'] = LeadForm(initial={'purpose': 'course'})
    return render(request, 'core/course.html', context)


def retreat(request):
    context = get_common_context(request)
    retreat_obj = Retreat.objects.filter(is_active=True).first()
    context['retreat'] = retreat_obj
    if retreat_obj:
        context['days'] = retreat_obj.days.all()
    context['form'] = LeadForm(initial={'purpose': 'retreat'})
    return render(request, 'core/retreat.html', context)


def contact(request):
    context = get_common_context(request)
    context['form'] = LeadForm()
    return render(request, 'core/contact.html', context)


def service_detail(request, pk):
    context = get_common_context(request)
    from django.shortcuts import get_object_or_404
    context['service'] = get_object_or_404(Service, pk=pk)
    context['form'] = LeadForm(initial={'purpose': 'session'})
    return render(request, 'core/service_detail.html', context)


def chakra_detail(request, pk):
    context = get_common_context(request)
    from django.shortcuts import get_object_or_404
    context['chakra'] = get_object_or_404(Chakra, pk=pk)
    context['form'] = LeadForm(initial={'purpose': 'session'})
    return render(request, 'core/chakra_detail.html', context)


@require_POST
def submit_lead(request):
    form = LeadForm(request.POST)
    if form.is_valid():
        form.save()
        if request.headers.get('HX-Request'):
            return render(request, 'core/partials/success_message.html', {})
        messages.success(request, 'გმადლობთ! მალე დაგიკავშირდებით. ✅')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    if request.headers.get('HX-Request'):
        return render(request, 'core/partials/form_errors.html', {'form': form})
    messages.error(request, 'შეავსეთ ყველა სავალდებულო ველი.')
    return redirect(request.META.get('HTTP_REFERER', '/'))
