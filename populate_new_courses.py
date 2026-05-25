import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Course, CoursePackage

# Check existing courses
existing = Course.objects.all()
print("Existing courses count:", existing.count())

# 1. იკიგაი
ikigai, created = Course.objects.get_or_create(
    title_ge="იკიგაი — ცხოვრების აზრი",
    title_en="Ikigai — Purpose of Life",
    defaults={
        'subtitle_ge': "აღმოაჩინე შენი გატაცება, მისია და მოწოდება",
        'subtitle_en': "Discover your passion, mission, and vocation",
        'description_ge': "ეს კურსი დაგეხმარება იპოვო ბალანსი შენს საყვარელ საქმეს, პროფესიასა და ფინანსურ კეთილდღეობას შორის.\n\nგაიგე რა გინდა რეალურად ცხოვრებაში.",
        'description_en': "This course helps you find balance between what you love, your profession, and financial well-being.",
        'what_you_learn_ge': "იაპონური ფილოსოფია იკიგაი\nმიზნების დასახვა და მიღწევა\nმოტივაციის პოვნა ყოველდღიურად\nშენი ძლიერი მხარეების აღმოჩენა",
        'what_you_learn_en': "Japanese Ikigai philosophy\nGoal setting and achievement\nFinding daily motivation\nDiscovering your strengths",
        'bonuses_ge': "1:1 კონსულტაცია ქოუჩთან\nსამუშაო რვეული (PDF Workbook)\nდახურული მასტერმაინდ ჯგუფი",
        'bonuses_en': "1:1 coaching session\nPDF Workbook\nPrivate mastermind group",
        'packages_title_ge': "აირჩიე შენი ტრანსფორმაციის გზა",
        'packages_title_en': "Choose your transformation path",
        'total_value_ge': "900 ₾",
        'total_value_en': "900 ₾",
        'is_active': True
    }
)

if created:
    print("Created Ikigai course")
    # Add packages
    CoursePackage.objects.create(
        course=ikigai,
        name_ge="სტანდარტული",
        name_en="Standard",
        price="290 ₾",
        features_ge="სრული ლექციები\nწვდომა მასალებზე 3 თვე\nჯგუფური ჩატი",
        features_en="Full lectures\n3 months access\nGroup chat"
    )
    CoursePackage.objects.create(
        course=ikigai,
        name_ge="პრემიუმი",
        name_en="Premium",
        price="490 ₾",
        features_ge="სრული ლექციები\nსამუდამო წვდომა\n1 პირადი სესია გურანდასთან",
        features_en="Full lectures\nLifetime access\n1 private session with Guranda",
        is_featured=True
    )
else:
    print("Ikigai already exists")

# 2. თვითსიყვარული
selflove, created = Course.objects.get_or_create(
    title_ge="თვითსიყვარული და საზღვრები",
    title_en="Self-Love and Boundaries",
    defaults={
        'subtitle_ge': "ისწავლე საკუთარი თავის მიღება და ჯანსაღი საზღვრების დაწესება",
        'subtitle_en': "Learn self-acceptance and establishing healthy boundaries",
        'description_ge': "ღრმა თერაპიული კურსი, რომელიც დაგეხმარება გათავისუფლდე სხვისი აზრებისგან, აღადგინო თვითშეფასება და შეიყვარო საკუთარი თავი უპირობოდ.",
        'description_en': "Deep therapeutic course that helps you release others' opinions, rebuild self-esteem, and love yourself unconditionally.",
        'what_you_learn_ge': "თვითმიმღებლობა და კრიტიკისგან გათავისუფლება\nროგორ ვთქვათ 'არა' დანაშაულის გრძნობის გარეშე\nსხეულის სიყვარული და მიღება\nემოციური ინტელექტი",
        'what_you_learn_en': "Self-acceptance and freedom from inner critic\nHow to say 'No' without guilt\nBody image and love\nEmotional intelligence",
        'bonuses_ge': "მედიტაციების ნაკრები\nყოველკვირეული პრაქტიკული დავალებები\nმუდმივი მხარდაჭერა ჩატში",
        'bonuses_en': "Meditation audio pack\nWeekly practical tasks\nChat support group",
        'packages_title_ge': "აირჩიე პაკეტი",
        'packages_title_en': "Choose package",
        'total_value_ge': "850 ₾",
        'total_value_en': "850 ₾",
        'is_active': True
    }
)

if created:
    print("Created Self-Love course")
    # Add packages
    CoursePackage.objects.create(
        course=selflove,
        name_ge="ბაზისური",
        name_en="Basic",
        price="190 ₾",
        features_ge="ვიდეო გაკვეთილები\nპრაქტიკული სავარჯიშოები",
        features_en="Video lessons\nPractical exercises"
    )
    CoursePackage.objects.create(
        course=selflove,
        name_ge="ინტენსივი",
        name_en="Intensiv",
        price="350 ₾",
        features_ge="ვიდეო გაკვეთილები\nპრაქტიკული სავარჯიშოები\nლაივ შეხვედრები კითხვა-პასუხით",
        features_en="Video lessons\nPractical exercises\nLive Q&A sessions",
        is_featured=True
    )
else:
    print("Self-Love already exists")
