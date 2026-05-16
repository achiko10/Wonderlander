import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import ContactInfo, RetreatDay

def fill_defaults():
    # 1. Update ContactInfo
    contact = ContactInfo.objects.first()
    if contact:
        contact.bank_title_en = "Bank Details"
        contact.bank_recipient_label_en = "Recipient"
        contact.bank_recipient_name_en = "Guranda Lazarashvili"
        contact.save()
        print("Updated ContactInfo defaults.")

    # 2. Update RetreatDay dates
    # Mapping Georgian month abbreviations to English
    months_map = {
        'სექტ': 'SEP',
        'ოქტ': 'OCT',
        'ნოე': 'NOV',
        'დეკ': 'DEC',
        'იან': 'JAN',
        'თებ': 'FEB',
        'მარ': 'MAR',
        'აპრ': 'APR',
        'მაის': 'MAY',
        'ივნ': 'JUN',
        'ივლ': 'JUL',
        'აგვ': 'AUG',
    }
    
    days = RetreatDay.objects.all()
    for day in days:
        ge_label = day.date_label
        en_label = ge_label
        for ge_m, en_m in months_map.items():
            if ge_m in ge_label:
                en_label = ge_label.replace(ge_m, en_m)
                break
        
        day.date_label_en = en_label
        day.save()

if __name__ == "__main__":
    fill_defaults()
