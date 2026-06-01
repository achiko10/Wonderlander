from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import SiteSettings, Service, Chakra, Course, Retreat, ContactInfo, Review
from .forms import LeadForm
import urllib.request
import urllib.parse
import json
import threading

BOT_TOKEN = "8901049445:AAGqF1zwGw99fFa4Dw-HDbcDx8_q_eO15yM"
ADMIN_CHAT_ID = 6404415447

def send_telegram_notification(lead):
    """საიტის ახალი განაცხადი → Telegram შეტყობინება ადმინს"""
    PURPOSE_LABELS = {
        'session': 'ინდივიდუალური სესია',
        'course': 'კურსები',
        'retreat': 'რიტრიტი',
        'mentoring': 'მენტორობა',
    }
    purpose_label = PURPOSE_LABELS.get(lead.purpose, lead.purpose)
    message_text = (
        f"🔔 <b>ახალი განაცხადი საიტიდან!</b>\n\n"
        f"👤 სახელი: <b>{lead.name}</b>\n"
        f"📱 ტელეფონი: <b>{lead.phone}</b>\n"
        f"📧 Email: {lead.email or '—'}\n"
        f"🎯 სერვისი: <b>{purpose_label}</b>\n"
        f"💬 შეტყობინება: {lead.message or '—'}"
    )
    def _send():
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            data = urllib.parse.urlencode({
                'chat_id': ADMIN_CHAT_ID,
                'text': message_text,
                'parse_mode': 'HTML'
            }).encode()
            req = urllib.request.Request(url, data=data)
            urllib.request.urlopen(req, timeout=5)
        except Exception as e:
            print(f"Telegram notification error: {e}")
    threading.Thread(target=_send, daemon=True).start()


def get_common_context(request):
    lang = request.session.get('lang', 'ge')
    try:
        contact = ContactInfo.objects.first()
    except ContactInfo.DoesNotExist:
        contact = None
    try:
        settings = SiteSettings.objects.first()
        if settings:
            # Pre-process lists for templates based on language
            if lang == 'en':
                settings.creds_list = [c.strip() for c in settings.hero_creds_en.split(",")] if settings.hero_creds_en else []
                settings.tags_list = [t.strip() for t in settings.intro_tags_en.split(",")] if settings.intro_tags_en else []
            else:
                settings.creds_list = [c.strip() for c in settings.hero_creds_ge.split(",")] if settings.hero_creds_ge else []
                settings.tags_list = [t.strip() for t in settings.intro_tags_ge.split(",")] if settings.intro_tags_ge else []
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
    courses = Course.objects.filter(is_active=True)
    context['courses'] = courses
    context['form'] = LeadForm(initial={'purpose': 'course'})
    return render(request, 'core/course.html', context)


def course_detail(request, pk):
    context = get_common_context(request)
    from django.shortcuts import get_object_or_404
    course_obj = get_object_or_404(Course, pk=pk, is_active=True)
    context['course'] = course_obj
    context['packages'] = course_obj.packages.all()
    context['form'] = LeadForm(initial={'purpose': 'course'})
    return render(request, 'core/course_detail.html', context)


def retreat_list(request):
    context = get_common_context(request)
    context['retreats'] = Retreat.objects.filter(is_active=True)
    context['form'] = LeadForm(initial={'purpose': 'retreat'})
    return render(request, 'core/retreat.html', context)


def retreat_detail(request, pk):
    context = get_common_context(request)
    from django.shortcuts import get_object_or_404
    retreat_obj = get_object_or_404(Retreat, pk=pk, is_active=True)
    context['retreat'] = retreat_obj
    context['days'] = retreat_obj.days.all()
    context['form'] = LeadForm(initial={'purpose': 'retreat'})
    return render(request, 'core/retreat_detail.html', context)


def contact(request):
    context = get_common_context(request)
    context['form'] = LeadForm()
    return render(request, 'core/contact.html', context)


def reviews(request):
    context = get_common_context(request)
    context['reviews'] = Review.objects.filter(is_active=True)
    return render(request, 'core/reviews.html', context)



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
        lead = form.save()
        send_telegram_notification(lead)
        if request.headers.get('HX-Request'):
            return render(request, 'core/partials/success_message.html', {})
        messages.success(request, 'გმადლობთ! მალე დაგიკავშირდებით. ✅')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    if request.headers.get('HX-Request'):
        return render(request, 'core/partials/form_errors.html', {'form': form})
    messages.error(request, 'შეავსეთ ყველა სავალდებულო ველი.')
    return redirect(request.META.get('HTTP_REFERER', '/'))
