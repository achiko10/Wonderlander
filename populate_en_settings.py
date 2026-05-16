# -*- coding: utf-8 -*-
import os, sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import SiteSettings

s = SiteSettings.objects.first()
if s:
    # Populate existing SiteSettings row with basic EN defaults if they are empty
    if not s.nav_home_en: s.nav_home_en = "Home"
    if not s.nav_course_en: s.nav_course_en = "Courses"
    if not s.nav_retreat_en: s.nav_retreat_en = "Retreats"
    if not s.nav_contact_en: s.nav_contact_en = "Contact"
    
    if not s.hero_badge_en: s.hero_badge_en = "✦ WONDERLANDER WELLNESS"
    if not s.hero_title_en: s.hero_title_en = "Harmonious Relationship With Yourself"
    if not s.hero_subtitle_en: s.hero_subtitle_en = "Hello. Thank you for your trust ☀️"
    if not s.hero_btn1_en: s.hero_btn1_en = "Book Now ❣️"
    if not s.hero_btn2_en: s.hero_btn2_en = "Services"
    if not s.hero_creds_en: s.hero_creds_en = "🎓 MD, 🧠 NLP, 🌿 Holistic, 🔥 Kundalini"
    
    if not s.stat1_label_en: s.stat1_label_en = "Faster Results"
    if not s.stat2_label_en: s.stat2_label_en = "Sessions to Goal"
    if not s.stat3_label_en: s.stat3_label_en = "Energy Centers"
    if not s.stat4_label_en: s.stat4_label_en = "Action Plan"
    
    if not s.intro_tags_en: s.intro_tags_en = "Psycho-somatics, NLP, Hypnotherapy, Kundalini, EFT, Art Therapy, Yoga, Meditation"
    
    if not s.services_title_en: s.services_title_en = "Investment In Yourself"
    if not s.chakras_title_en: s.chakras_title_en = "When Should You Contact Me?"
    if not s.about_title_en: s.about_title_en = "Guranda Lazarashvili"
    if not s.footer_copy_en: s.footer_copy_en = "© 2024 Wonderlander Wellness. All rights reserved."

    s.save()
    sys.stdout.buffer.write(b"Successfully populated EN defaults in SiteSettings!\n")
else:
    sys.stdout.buffer.write(b"No SiteSettings found to populate.\n")
