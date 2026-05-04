import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import SiteSettings, Service, Chakra, Course, CoursePackage, Retreat, RetreatDay, ContactInfo

def run():
    print("Populating ContactInfo...")
    if not ContactInfo.objects.exists():
        ContactInfo.objects.create(
            whatsapp="+995 597 71 84 67",
            telegram="wonderlanderr",
            instagram="wonderlanderwellness",
            email="dr.guranda8@gmail.com",
            bank_accounts_ge="TBC Bank: GE...\nBOG: GE...",
            bank_accounts_en="TBC Bank: GE...\nBOG: GE..."
        )

    print("Populating SiteSettings...")
    if not SiteSettings.objects.exists():
        SiteSettings.objects.create(
            site_title_ge="Wonderlander Wellness",
            site_title_en="Wonderlander Wellness",
            hero_title_ge="საკუთარ თავთან<br><em>ჰარმონიული</em> ურთიერთობა",
            hero_title_en="<em>Harmonious</em> Relationship<br>with Yourself",
            hero_subtitle_ge="გამარჯობა. პირველ რიგში, მადლობა ნდობისთვის ☀️\nერთადერთი ადამიანი, ვინც დაბადებიდან სიკვდილამდე შენთანაა — ეს შენი საკუთარი თავია 💆‍♀️",
            hero_subtitle_en="Hello. Thank you for your trust ☀️\nThe only person who is with you from birth to death is your own self 💆‍♀️",
            about_text_ge="სესიებს უძღვება გურანდა ლაზარაშვილი — დიპლომირებული მედიკოსი, ფსიქოლოგი, ჰიპნოთერაპევტი, NLP-თერაპევტი, ველნეს ქოუჩი, პიროვნული განვითარების მენტორი და კუნდალინი აქტივაციის ფასილიტატორი.",
            about_text_en="Sessions are led by Guranda Lazarashvili — certified medical doctor, psychologist, hypnotherapist, NLP therapist, wellness coach, personal development mentor and Kundalini Activation facilitator.",
            credentials_ge="დიპლომირებული მედიკოსი (MD)\nფსიქოლოგი & NLP-თერაპევტი\nჰიპნოთერაპევტი\nკუნდალინი აქტივაციის ფასილიტატორი",
            credentials_en="Certified Medical Doctor (MD)\nPsychologist & NLP Therapist\nHypnotherapist\nKundalini Activation Facilitator"
        )

    print("Populating Services...")
    if not Service.objects.exists():
        Service.objects.create(title_ge="ინდივიდუალური სესია", title_en="Individual Session", description_ge="ჰოლისტიკური სესია — ფსიქო-სომატიკა, NLP, ჰიპნოთერაპია. შედეგი 1-5 სესიაში.", description_en="Holistic session — psycho-somatics, NLP, hypnotherapy. Results in 1-5 sessions.", price="111€", duration="60 წთ", icon="💆‍♀️", order=1)
        Service.objects.create(title_ge="სრული პაკეტი — 5 სესია", title_en="Full Package — 5 Sessions", description_ge="5 კვირა, 5 სესია. ყველაზე ეფექტური გზა ღრმა ტრანსფორმაციისთვის.", description_en="5 weeks, 5 sessions. The most effective path to deep transformation.", price="455€", duration="დაზოგე 100€", icon="🔥", order=2)
        Service.objects.create(title_ge="კუნდალინი აქტივაცია", title_en="Kundalini Activation", description_ge="სასიცოცხლო ენერგიის გამოღვიძება. ონლაინ ან ოფლაინ.", description_en="Awakening life force energy. Online or offline.", price="222€ / 255€", duration="ონლ. / ოფლ.", icon="🌊", order=3)
        Service.objects.create(title_ge="1-თვიანი მენტორობა", title_en="1-Month Mentoring", description_ge="კვირაში 2 შეხვედრა + ყოველდღიური მხარდაჭერა. გარანტირებული შედეგი.", description_en="2 sessions/week + daily support. Guaranteed results.", price="1111€", duration="გარანტია", icon="🚀", order=4)

    print("Populating Chakras...")
    if not Chakra.objects.exists():
        chakras_data = [
            (1, "ფუძე", "Root", "უსაფრთხოება, სტაბილურობა", "Safety, Stability", "პანიკური შეტევები\nფობიები\nქრონიკული შიშები", "Panic attacks\nPhobias\nChronic fears", "#dc2626", "🔴"),
            (2, "საკრალური", "Sacral", "ემოციები, სიამოვნება", "Emotions, Pleasure", "მიჯაჭვულობები\nადიქციები\nემოციური ტრავმები", "Attachments\nAddictions\nEmotional trauma", "#ea580c", "🟠"),
            (3, "მზის წნული", "Solar Plexus", "პიროვნული ძალა", "Personal Power", "თვითშეფასება\nბრაზი\nმსხვერპლის მდგომარეობა", "Self-esteem\nAnger\nVictim mentality", "#ca8a04", "🟡"),
            (4, "გული", "Heart", "სიყვარული, კავშირი", "Love, Connection", "ტოქსიკური ურთიერთობები\nსიყვარულის შიში\nემოციური ტკივილი", "Toxic relationships\nFear of love\nEmotional pain", "#16a34a", "💚"),
            (5, "ყელი", "Throat", "გამოხატულობა", "Expression", "თვითგამოხატვა\n„არა\"-ს თქმა\nსაზღვრების დაცვა", "Self-expression\nSaying 'No'\nSetting boundaries", "#2563eb", "🔵"),
            (6, "მესამე თვალი", "Third Eye", "ინტუიცია", "Intuition", "დეპრესია\nმიმართულების დაკარგვა\nმენტალური ბარიერები", "Depression\nLoss of direction\nMental barriers", "#7c3aed", "🟣"),
            (7, "გვირგვინი", "Crown", "სულიერი კავშირი", "Spiritual Connection", "ეგზისტენციური კრიზისი\nიკიგაის ძიება\nშინაგანი სიმშვიდე", "Existential crisis\nFinding Ikigai\nInner peace", "#9333ea", "👑"),
        ]
        for num, n_ge, n_en, t_ge, t_en, c_ge, c_en, col, icon in chakras_data:
            Chakra.objects.create(number=num, name_ge=n_ge, name_en=n_en, theme_ge=t_ge, theme_en=t_en, conditions_ge=c_ge, conditions_en=c_en, color=col, icon=icon)

    print("Populating Retreat...")
    if not Retreat.objects.exists():
        r = Retreat.objects.create(
            title_ge="ტრანსფორმაციული მოგზაურობა", title_en="Transformational Journey",
            date_range="11-20 სექტემბერი", location_ge="ბალი", location_en="Bali",
            price="2555$", early_bird_price="2000$",
            description_ge="10 დღე ღმერთების კუნძულზე — გარეთ და შიგნით მოგზაურობა",
            description_en="10 days on the Island of Gods — a journey outward and inward",
            includes_ge="სასტუმროში განთავსება\nორჯერადი ჯანსაღი კვება\nყოველდღიური ვორქშოფები\nიოგა და მედიტაცია\nკუნდალინის 4 სესია",
            includes_en="Hotel accommodation\nTwice-daily meals\nDaily workshops\nYoga & meditation\n4 Kundalini sessions"
        )
        days = [
            (1, "11 სექ", "ადაპტაცია, გაცნობის საკრალური წრე", "Adaptation, Sacred circle"),
            (2, "12 სექ", "ფუძის ჩაკრა — სადჰუს დაფა", "Root Chakra — Sadhu board"),
            (3, "13 სექ", "საკრალური ჩაკრა — ექსტაზური ცეკვა", "Sacral Chakra — Ecstatic dance")
        ]
        for d_n, d_l, t_ge, t_en in days:
            RetreatDay.objects.create(retreat=r, day_number=d_n, date_label=d_l, title_ge=t_ge, title_en=t_en, content_ge=t_ge, content_en=t_en)

    print("Populating Course...")
    if not Course.objects.exists():
        c = Course.objects.create(
            title_ge="ფემინური სიმდიდრე", title_en="Feminine Wealth",
            subtitle_ge="5-კვირიანი ონლაინ ტრანსფორმაცია", subtitle_en="5-week online transformation",
            description_ge="გაიღვიძე შენი ქალური ენერგია და მიიზიდე სიუხვე.", description_en="Awaken your feminine energy and attract abundance.",
            what_you_learn_ge="ენერგიის მართვა\nფინანსური ბლოკების მოხსნა", what_you_learn_en="Energy management\nRemoving financial blocks",
            bonuses_ge="პირადი კონსულტაცია", bonuses_en="Personal consultation"
        )
        CoursePackage.objects.create(course=c, name_ge="სტანდარტული", name_en="Standard", price="222$", features_ge="ყველა მოდული\nსაერთო ჩატი", features_en="All modules\nGeneral chat", order=1)
        CoursePackage.objects.create(course=c, name_ge="VIP", name_en="VIP", price="555$", features_ge="სტანდარტული + პირადი შეხვედრები", features_en="Standard + 1on1 meetings", order=2, is_featured=True)

    print("Done!")

if __name__ == '__main__':
    run()
