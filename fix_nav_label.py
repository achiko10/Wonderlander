# -*- coding: utf-8 -*-
import os, sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import SiteSettings

s = SiteSettings.objects.first()
if s:
    # Save without printing Georgian
    s.nav_course_ge = '\u10d9\u10e3\u10e0\u10e1\u10d4\u10d1\u10d8'  # კურსები
    s.save()
    # Verify using ascii-safe repr
    val = repr(SiteSettings.objects.values_list('nav_course_ge', flat=True).first())
    sys.stdout.buffer.write(b"nav_course_ge = " + val.encode('utf-8') + b"\n")
    sys.stdout.buffer.write(b"Done OK\n")
else:
    sys.stdout.buffer.write(b"No SiteSettings found\n")
