from django.shortcuts import render, get_object_or_404
from .models import SiteSetting, TeamMember, Match, ContactInfo, PageContent
from django.http import JsonResponse
from .models import ContactSubmission


def index(request):
    settings = SiteSetting.objects.first()
    team = TeamMember.objects.all()[:8]
    upcoming = Match.objects.all().order_by('date')[:5]
    contact = ContactInfo.objects.first()
    about = PageContent.objects.filter(slug='about').first()
    return render(request, 'core/index.html', {
        'settings': settings,
        'team': team,
        'upcoming': upcoming,
        'contact': contact,
        'about': about,
    })


def page(request, slug):
    settings = SiteSetting.objects.first()
    page = get_object_or_404(PageContent, slug=slug)
    return render(request, 'core/page.html', {'settings': settings, 'page': page})


def about(request):
    return page(request, 'about')


def matches(request):
    settings = SiteSetting.objects.first()
    upcoming = Match.objects.all().order_by('date')
    return render(request, 'core/matches.html', {'settings': settings, 'upcoming': upcoming})


def team(request):
    settings = SiteSetting.objects.first()
    team = TeamMember.objects.all()
    return render(request, 'core/team.html', {'settings': settings, 'team': team})


def contact(request):
    settings = SiteSetting.objects.first()
    contact = ContactInfo.objects.first()
    return render(request, 'core/contact.html', {'settings': settings, 'contact': contact})


def contact_submit(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    subject = request.POST.get('subject', '').strip()
    message = request.POST.get('message', '').strip()

    if not name or not email or not message:
        return JsonResponse({'success': False, 'message': 'Name, email and message are required.'}, status=400)

    try:
        sub = ContactSubmission.objects.create(name=name, email=email, subject=subject, message=message)
    except Exception as e:
        return JsonResponse({'success': False, 'message': 'Could not save submission.'}, status=500)

    return JsonResponse({'success': True, 'message': 'Thanks — your message has been received.'})
