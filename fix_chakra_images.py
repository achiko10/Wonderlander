import os
import django
import requests
from django.core.files import File
from tempfile import NamedTemporaryFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Chakra

def add_chakra_images():
    # Reliable placeholder source
    image_url = 'https://picsum.photos/800/600'

    for chakra in Chakra.objects.all():
        print(f"Processing chakra {chakra.number}...")
        try:
            # Added headers to look like a browser
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(image_url, headers=headers, timeout=15)
            if r.status_code == 200:
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(r.content)
                img_temp.flush()
                chakra.image.save(f"chakra_final_{chakra.id}.jpg", File(img_temp), save=True)
                print(f"Success for chakra {chakra.number}")
            else:
                print(f"Failed with status {r.status_code} for chakra {chakra.number}")
        except Exception as e:
            print(f"Error for chakra {chakra.number}: {str(e)}")

if __name__ == '__main__':
    add_chakra_images()
