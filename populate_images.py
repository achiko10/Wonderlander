import os
import django
import requests
from django.core.files import File
from tempfile import NamedTemporaryFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Service, Chakra

def add_demo_images():
    # Placeholder images from Unsplash (Thematic)
    images = {
        'service': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=800',
        'chakra': 'https://images.unsplash.com/photo-1528319725582-ddc0b6a27636?auto=format&fit=crop&q=80&w=800'
    }

    # Update Services
    for service in Service.objects.all():
        if not service.image:
            r = requests.get(images['service'])
            if r.status_code == requests.codes.ok:
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(r.content)
                img_temp.flush()
                service.image.save(f"service_{service.id}.jpg", File(img_temp), save=True)

    # Update Chakras
    for chakra in Chakra.objects.all():
        if not chakra.image:
            r = requests.get(images['chakra'])
            if r.status_code == requests.codes.ok:
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(r.content)
                img_temp.flush()
                chakra.image.save(f"chakra_{chakra.id}.jpg", File(img_temp), save=True)

if __name__ == '__main__':
    add_demo_images()
