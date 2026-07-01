import re
from django.db import migrations

def remove_emojis(apps, schema_editor):
    SiteSettings = apps.get_model('core', 'SiteSettings')
    Service = apps.get_model('core', 'Service')
    Chakra = apps.get_model('core', 'Chakra')
    Course = apps.get_model('core', 'Course')
    Retreat = apps.get_model('core', 'Retreat')
    ContactInfo = apps.get_model('core', 'ContactInfo')
    BotSettings = apps.get_model('core', 'BotSettings')

    emojis = ['❣️', '🔥', '✨', '🍷', '🌴', '🧩', '☀️', '🎓', '🧠', '🌿', '️', '⭐', '✅', '🎁', '🧘‍♀️', '🧘‍♂️', '💖', '💰', '📋', '📄', '🏷️', '🔗', '🔑', '👋', '🔘', '📅', '⚙️']
    
    def clean(text):
        if not text:
            return text
        for e in emojis:
            text = text.replace(e, '')
        return text.strip()

    models_to_clean = [SiteSettings, Service, Chakra, Course, Retreat, ContactInfo, BotSettings]
    for model_class in models_to_clean:
        for obj in model_class.objects.all():
            changed = False
            for field in obj._meta.fields:
                if field.get_internal_type() in ['CharField', 'TextField']:
                    val = getattr(obj, field.name)
                    if isinstance(val, str):
                        new_val = clean(val)
                        if new_val != val:
                            setattr(obj, field.name, new_val)
                            changed = True
            if changed:
                obj.save()

class Migration(migrations.Migration):
    dependencies = [
        ("core", "0019_alter_sitesettings_hero_btn1_en_and_more"),
    ]

    operations = [
        migrations.RunPython(remove_emojis),
    ]
