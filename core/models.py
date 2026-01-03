from django.db import models


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, default='Young Boys Tirana')
    logo_url = models.CharField(max_length=500, blank=True, default='assets/img/logo/logo.jpg')
    tagline = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.site_name


class TeamMember(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120, blank=True)
    number = models.CharField(max_length=10, blank=True)
    photo_url = models.CharField(max_length=500, blank=True, default='assets/img/logo/logo.jpg')

    def __str__(self):
        return f"{self.name} ({self.role})"


class Match(models.Model):
    opponent = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    is_home = models.BooleanField(default=True)
    result = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.opponent} on {self.date}"


class ContactInfo(models.Model):
    address = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.email or self.phone or 'Contact'


class PageContent(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.slug


class ContactSubmission(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} <{self.email}> ({self.created_at:%Y-%m-%d})"
