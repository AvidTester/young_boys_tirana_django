from django.core.management.base import BaseCommand
from core.models import SiteSetting, TeamMember, Match, ContactInfo, PageContent
from datetime import date, time

class Command(BaseCommand):
    help = 'Seed initial site data'

    def handle(self, *args, **options):
        if not SiteSetting.objects.exists():
            SiteSetting.objects.create(site_name='Young Boys Tirana', logo_url='img/logo/logo.jpg', tagline='Passion. Pride. Victory.')
            self.stdout.write(self.style.SUCCESS('Created SiteSetting'))

        if not ContactInfo.objects.exists():
            ContactInfo.objects.create(address='Tirana, Albania', phone='+355 69 XXX XXXX', email='info@youngboystirana.al')
            self.stdout.write(self.style.SUCCESS('Created ContactInfo'))

        if not TeamMember.objects.exists():
            TeamMember.objects.bulk_create([
                TeamMember(name='Erion Hoxha', role='Goalkeeper', number='1'),
                TeamMember(name='Ardit Berisha', role='Defender', number='4'),
                TeamMember(name='Kledis Muça', role='Midfielder', number='8'),
                TeamMember(name='Taulant Basha', role='Forward', number='10'),
            ])
            self.stdout.write(self.style.SUCCESS('Created TeamMembers'))

        if not Match.objects.exists():
            Match.objects.bulk_create([
                Match(opponent='FK Partizani', date=date(2025,1,15), time=time(18,0), location='Tirana Stadium', is_home=True, result='3-1'),
                Match(opponent='KF Tirana', date=date(2025,1,22), time=time(16,0), location='Selman Stërmasi', is_home=False, result='2-2'),
                Match(opponent='Vllaznia Shkodër', date=date(2025,1,29), time=time(17,0), location='Tirana Stadium', is_home=True, result='2-0'),
            ])
            self.stdout.write(self.style.SUCCESS('Created Matches'))

        if not PageContent.objects.filter(slug='about').exists():
            PageContent.objects.create(slug='about', title='About Young Boys', body='Young Boys Tirana FC was founded in 2025 with a vision to become a cornerstone of Albanian football.')
            self.stdout.write(self.style.SUCCESS('Created About page'))

        self.stdout.write(self.style.SUCCESS('Seed complete'))
