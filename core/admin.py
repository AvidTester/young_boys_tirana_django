from django.contrib import admin
from .models import SiteSetting, TeamMember, Match, ContactInfo, PageContent


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'logo_url')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'number')


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('opponent', 'date', 'time', 'location', 'is_home', 'result')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'address')


@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')
