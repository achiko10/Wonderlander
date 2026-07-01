import os
import django

# Setup Django environment if run standalone
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wonderlander.settings')
django.setup()

from core.models import SiteSettings, Service, Chakra, Course, Retreat, ContactInfo, BotSettings

def clean_text(text):
    if not text:
        return text
    emojis = ['❣️', '🔥', '✨', '🍷', '🌴', '🧩', '☀️', '🎓', '🧠', '🌿', '️', '⭐', '✅', '🎁', '🧘‍♀️', '🧘‍♂️', '💖', '💰', '📋', '📄', '🏷️', '🔗', '🔑', '👋', '🔘', '📅', '⚙️']
    for e in emojis:
        text = text.replace(e, '')
    return text.strip()

def clean_model(model_class):
    count = 0
    for obj in model_class.objects.all():
        changed = False
        for field in obj._meta.fields:
            if field.get_internal_type() in ['CharField', 'TextField']:
                val = getattr(obj, field.name)
                if isinstance(val, str):
                    new_val = clean_text(val)
                    if new_val != val:
                        setattr(obj, field.name, new_val)
                        changed = True
        if changed:
            obj.save()
            count += 1
    print(f"Cleaned {count} objects in {model_class.__name__}")

def run():
    print("Starting emoji cleanup...")
    clean_model(SiteSettings)
    clean_model(Service)
    clean_model(Chakra)
    clean_model(Course)
    clean_model(Retreat)
    clean_model(ContactInfo)
    clean_model(BotSettings)
    print("Done!")

if __name__ == '__main__':
    run()
