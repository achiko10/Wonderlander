from django.db import models


class SiteSettings(models.Model):
    # Global & Navbar
    site_title_ge = models.CharField(max_length=255, default="Wonderlander Wellness")
    site_title_en = models.CharField(max_length=255, default="Wonderlander Wellness")
    navbar_cta_ge = models.CharField(max_length=50, default="ჩაწერა", verbose_name="ნავბარის ღილაკი (GE)")
    navbar_cta_en = models.CharField(max_length=50, default="Book Now", verbose_name="ნავბარის ღილაკი (EN)")
    nav_home_ge = models.CharField(max_length=50, default="მთავარი")
    nav_home_en = models.CharField(max_length=50, default="Home", blank=True)
    nav_course_ge = models.CharField(max_length=50, default="კურსები")
    nav_course_en = models.CharField(max_length=50, default="Courses", blank=True)
    nav_retreat_ge = models.CharField(max_length=50, default="ბალი")
    nav_retreat_en = models.CharField(max_length=50, default="Retreats", blank=True)
    nav_contact_ge = models.CharField(max_length=50, default="კონტაქტი")
    nav_contact_en = models.CharField(max_length=50, default="Contact", blank=True)
    nav_review_ge = models.CharField(max_length=50, default="უკუკავშირი")
    nav_review_en = models.CharField(max_length=50, default="Reviews", blank=True)
    
    # Hero Section
    hero_badge_ge = models.CharField(max_length=100, default="✦ WONDERLANDER WELLNESS")
    hero_badge_en = models.CharField(max_length=100, default="✦ WONDERLANDER WELLNESS", blank=True)
    hero_title_ge = models.TextField(default="საკუთარ თავთან ჰარმონიული ურთიერთობა")
    hero_title_en = models.TextField(default="Harmonious Relationship With Yourself", blank=True)
    hero_subtitle_ge = models.TextField(default="გამარჯობა. მადლობა ნდობისთვის ☀️")
    hero_subtitle_en = models.TextField(default="Hello. Thank you for your trust ☀️", blank=True)
    hero_btn1_ge = models.CharField(max_length=50, default="ჩაწერა")
    hero_btn1_en = models.CharField(max_length=50, default="Book Now", blank=True)
    hero_btn2_ge = models.CharField(max_length=50, default="სერვისები")
    hero_btn2_en = models.CharField(max_length=50, default="Services", blank=True)
    hero_creds_ge = models.CharField(max_length=255, default="🎓 MD, 🧠 NLP, 🌿 Holistic, 🔥 Kundalini", help_text="მძიმით გამოყოფილი")
    hero_creds_en = models.CharField(max_length=255, default="🎓 MD, 🧠 NLP, 🌿 Holistic, 🔥 Kundalini", blank=True)
    hero_image = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name="მთავარი (Hero) ფოტო")
    
    # Intro Statistics (4 slots)
    stat1_num = models.CharField(max_length=20, default="10x")
    stat1_label_ge = models.CharField(max_length=100, default="უფრო სწრაფი შედეგი")
    stat1_label_en = models.CharField(max_length=100, default="Faster Results", blank=True)
    stat2_num = models.CharField(max_length=20, default="1-5")
    stat2_label_ge = models.CharField(max_length=100, default="სესია მიზნისთვის")
    stat2_label_en = models.CharField(max_length=100, default="Sessions for Goal", blank=True)
    stat3_num = models.CharField(max_length=20, default="7")
    stat3_label_ge = models.CharField(max_length=100, default="ენერგეტ. ცენტრი")
    stat3_label_en = models.CharField(max_length=100, default="Energy Centers", blank=True)
    stat4_num = models.CharField(max_length=20, default="💎")
    stat4_label_ge = models.CharField(max_length=100, default="სამოქმ. გეგმა")
    stat4_label_en = models.CharField(max_length=100, default="Action Plan", blank=True)
    
    # Tags
    intro_tags_ge = models.TextField(default="ფსიქო-სომატიკა, NLP, ჰიპნოთერაპია, კუნდალინი, EFT, არტ თერაპია, იოგა, მედიტაცია")
    intro_tags_en = models.TextField(default="Psycho-somatics, NLP, Hypnotherapy, Kundalini, EFT, Art Therapy, Yoga, Meditation", blank=True)

    # Section Titles
    services_title_ge = models.CharField(max_length=255, default="ინვესტიცია საკუთარ თავში")
    services_title_en = models.CharField(max_length=255, default="Investment In Yourself", blank=True)
    chakras_title_ge = models.CharField(max_length=255, default="რა მდგომარეობის დროს მომმართოთ?")
    chakras_title_en = models.CharField(max_length=255, default="When Should You Contact Me?", blank=True)
    about_title_ge = models.CharField(max_length=255, default="გურანდა ლაზარაშვილი")
    about_title_en = models.CharField(max_length=255, default="Guranda Lazarashvili", blank=True)
    reviews_title_ge = models.CharField(max_length=255, default="რას ამბობენ ჩვენზე")
    reviews_title_en = models.CharField(max_length=255, default="What They Say", blank=True)
    reviews_empty_text_ge = models.CharField(max_length=255, default="უკუკავშირები ჯერ არ დამატებულა.")
    reviews_empty_text_en = models.CharField(max_length=255, default="No reviews added yet.", blank=True)
    
    # About Section
    about_text_ge = models.TextField(verbose_name="ჩემს შესახებ (GE)", blank=True)
    about_text_en = models.TextField(verbose_name="About Me (EN)", blank=True)
    about_image = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name="პროფილის (About) ფოტო")
    
    # Footer
    footer_copy_ge = models.CharField(max_length=255, default="© 2026 Wonderlander Wellness. ყველა უფლება დაცულია.")
    footer_copy_en = models.CharField(max_length=255, default="© 2026 Wonderlander Wellness. All rights reserved.", blank=True)

    # UI Labels (Buttons, Headings, Small Text)
    label_details_ge = models.CharField(max_length=50, default="დეტალურად →", verbose_name="ღილაკი 'დეტალურად' (GE)")
    label_details_en = models.CharField(max_length=50, default="Details →", verbose_name="Button 'Details' (EN)")
    
    label_popular_ge = models.CharField(max_length=50, default="პოპულარული", verbose_name="ბეიჯი 'პოპულარული' (GE)")
    label_popular_en = models.CharField(max_length=50, default="Popular", verbose_name="Badge 'Popular' (EN)")
    
    label_save_ge = models.CharField(max_length=50, default="დაზოგე", verbose_name="ტექსტი 'დაზოგე' (GE)")
    label_save_en = models.CharField(max_length=50, default="Save", verbose_name="Text 'Save' (EN)")
    
    label_book_session_ge = models.CharField(max_length=100, default="დაჯავშნე სესია", verbose_name="სათაური 'დაჯავშნე სესია' (GE)")
    label_book_session_en = models.CharField(max_length=100, default="Book a Session", verbose_name="Title 'Book a Session' (EN)")
    
    label_our_courses_ge = models.CharField(max_length=100, default="ჩვენი კურსები", verbose_name="სათაური 'ჩვენი კურსები' (GE)")
    label_our_courses_en = models.CharField(max_length=100, default="Our Courses", verbose_name="Title 'Our Courses' (EN)")
    
    label_choose_course_ge = models.CharField(max_length=255, default="აირჩიეთ თქვენთვის შესაფერი კურსი", verbose_name="ქვესათაური 'აირჩიეთ კურსი' (GE)")
    label_choose_course_en = models.CharField(max_length=255, default="Choose the course that's right for you", verbose_name="Subtitle 'Choose Course' (EN)")
    
    label_course_ge = models.CharField(max_length=50, default="კურსი", verbose_name="ბეიჯი 'კურსი' (GE)")
    label_course_en = models.CharField(max_length=50, default="Course", verbose_name="Badge 'Course' (EN)")
    
    label_you_feel_ge = models.CharField(max_length=100, default="შენ გრძნობ...", verbose_name="სათაური 'შენ გრძნობ' (GE)")
    label_you_feel_en = models.CharField(max_length=100, default="You feel...", verbose_name="Title 'You feel' (EN)")
    
    label_what_learn_ge = models.CharField(max_length=100, default="რას ისწავლი?", verbose_name="სათაური 'რას ისწავლი' (GE)")
    label_what_learn_en = models.CharField(max_length=100, default="What You'll Learn", verbose_name="Title 'What You'll Learn' (EN)")
    
    label_total_value_ge = models.CharField(max_length=100, default="ჯამური ღირებულება", verbose_name="ტექსტი 'ჯამური ღირებულება' (GE)")
    label_total_value_en = models.CharField(max_length=100, default="Total Value", verbose_name="Text 'Total Value' (EN)")
    
    label_guarantee_ge = models.CharField(max_length=100, default="110% თანხის დაბრუნების გარანტია", verbose_name="გარანტიის ტექსტი (GE)")
    label_guarantee_en = models.CharField(max_length=100, default="110% Money-back Guarantee", verbose_name="Guarantee Text (EN)")
    
    label_let_start_ge = models.CharField(max_length=50, default="დავიწყოთ", verbose_name="ღილაკი 'დავიწყოთ' (GE)")
    label_let_start_en = models.CharField(max_length=50, default="Let's Start", verbose_name="Button 'Let's Start' (EN)")
    
    label_booking_ge = models.CharField(max_length=50, default="დაჯავშნა", verbose_name="სათაური 'დაჯავშნა' (GE)")
    label_booking_en = models.CharField(max_length=50, default="Booking", verbose_name="Title 'Booking' (EN)")
    
    label_submit_app_ge = models.CharField(max_length=100, default="განაცხადის გაგზავნა", verbose_name="ღილაკი 'განაცხადის გაგზავნა' (GE)")
    label_submit_app_en = models.CharField(max_length=100, default="Submit Application", verbose_name="Button 'Submit' (EN)")
    
    label_included_ge = models.CharField(max_length=100, default="ღირებულებაში შედის", verbose_name="სათაური 'ღირებულებაში შედის' (GE)")
    label_included_en = models.CharField(max_length=100, default="What's Included", verbose_name="Title 'What's Included' (EN)")
    label_program_ge = models.CharField(max_length=100, default="პროგრამა", verbose_name="სათაური 'პროგრამა' (GE)")
    label_program_en = models.CharField(max_length=100, default="Program", verbose_name="Title 'Program' (EN)")
    label_early_bird_ge = models.CharField(max_length=50, default="Early Bird", verbose_name="სათაური 'Early Bird' (GE)")
    label_early_bird_en = models.CharField(max_length=50, default="Early Bird", verbose_name="Title 'Early Bird' (EN)")
    label_regular_price_ge = models.CharField(max_length=50, default="რეგულარული", verbose_name="სათაური 'რეგულარული ფასი' (GE)")
    label_regular_price_en = models.CharField(max_length=50, default="Regular", verbose_name="Title 'Regular Price' (EN)")
    label_energy_centers_ge = models.CharField(max_length=100, default="ენერგეტიკული ცენტრები", verbose_name="ბეიჯი 'ენერგეტიკული ცენტრები' (GE)")
    label_energy_centers_en = models.CharField(max_length=100, default="Energy Centers", verbose_name="Badge 'Energy Centers' (EN)")
    label_choose_chakra_ge = models.CharField(max_length=255, default="დააჭირეთ ჩაკრას, რომელშიც პრობლემას გრძნობთ", verbose_name="ქვესათაური 'აირჩიეთ ჩაკრა' (GE)")
    label_choose_chakra_en = models.CharField(max_length=255, default="Click on the chakra where you feel the issue", verbose_name="Subtitle 'Choose Chakra' (EN)")
    
    # New labels & text
    label_enroll_ge = models.CharField(max_length=100, default="ჩაწერა", verbose_name="ღილაკი 'ჩაწერა' (კურსებზე) (GE)")
    label_enroll_en = models.CharField(max_length=100, default="Enroll", verbose_name="Button 'Enroll' (on courses) (EN)")
    label_book_ge = models.CharField(max_length=100, default="დაჯავშნა", verbose_name="ღილაკი 'დაჯავშნა' (რიტრიტებზე) (GE)")
    label_book_en = models.CharField(max_length=100, default="Book", verbose_name="Button 'Book' (on retreats) (EN)")
    label_select_ge = models.CharField(max_length=100, default="არჩევა", verbose_name="ღილაკი 'არჩევა' (პაკეტებზე) (GE)")
    label_select_en = models.CharField(max_length=100, default="Select", verbose_name="Button 'Select' (on packages) (EN)")
    label_bonuses_ge = models.CharField(max_length=100, default="ბონუსები", verbose_name="სათაური 'ბონუსები' (GE)")
    label_bonuses_en = models.CharField(max_length=100, default="Bonuses", verbose_name="Title 'Bonuses' (EN)")
    label_whatsapp_btn_ge = models.CharField(max_length=100, default="WhatsApp-ზე დაწერა", verbose_name="ღილაკი 'WhatsApp' (GE)")
    label_whatsapp_btn_en = models.CharField(max_length=100, default="Message on WhatsApp", verbose_name="Button 'WhatsApp' (EN)")
    
    home_cta_title_ge = models.CharField(max_length=255, default="მზად ხარ ტრანსფორმაციისთვის?", verbose_name="ქოლ-თუ-ექშენ სათაური (GE)")
    home_cta_title_en = models.CharField(max_length=255, default="Ready for Transformation?", verbose_name="Call-to-Action Title (EN)")
    home_cta_text_ge = models.TextField(default="პირველი ნაბიჯი — ეს სესია. შედეგი 1-5 შეხვედრაში.", verbose_name="ქოლ-თუ-ექშენ ტექსტი (GE)")
    home_cta_text_en = models.TextField(default="The first step is a session. Results in 1-5 meetings.", verbose_name="Call-to-Action Text (EN)")
    
    home_why_title_ge = models.CharField(max_length=255, default="რატომ ჩემთან?", verbose_name="სექცია 'რატომ ჩემთან' სათაური (GE)")
    home_why_title_en = models.CharField(max_length=255, default="Why Work with Me?", verbose_name="Section 'Why Work with Me' Title (EN)")
    home_why_text1_ge = models.TextField(default="სტანდარტული ფსიქოთერაპიისგან განსხვავებით, შედეგებს ვიღებთ 10ჯერ უფრო სწრაფად. პრობლემათა უმრავლესობის გადაჭრა/მიზნების მიღწევა ხდება 1-5 სესიაში 🤗", verbose_name="რატომ ჩემთან - ტექსტი 1 (GE)")
    home_why_text1_en = models.TextField(default="Unlike standard psychotherapy, we achieve results 10x faster. Most problems are resolved/goals achieved in 1-5 sessions 🤗", verbose_name="Why Work with Me - Text 1 (EN)")
    home_why_text2_ge = models.TextField(default="სესიაზე დამღლელი საუბრების მაგივრად, ვიყენებთ უნიკალურ მეთოდოლოგიას — ფსიქო-სომატიკა, NLP, ჰიპნოთერაპია, კუნდალინი აქტივაცია, EFT, არტ თერაპია.", verbose_name="რატომ ჩემთან - ტექსტი 2 (GE)")
    home_why_text2_en = models.TextField(default="Instead of exhausting conversations, we use unique methodology — Psycho-somatics, NLP, Hypnotherapy, Kundalini Activation, EFT, Art Therapy.", verbose_name="Why Work with Me - Text 2 (EN)")




    class Meta:
        verbose_name = "საიტის პარამეტრები"
        verbose_name_plural = "საიტის პარამეტრები"

    def __str__(self):
        return "საიტის პარამეტრები"


class Service(models.Model):
    title_ge = models.CharField(max_length=255, verbose_name="სათაური (GE)")
    title_en = models.CharField(max_length=255, verbose_name="Title (EN)")
    short_description_ge = models.CharField(max_length=300, blank=True, verbose_name="მოკლე აღწერა - კარტზე (GE)", help_text="1-2 წინადადება. ჩამოთვლის გვერდზე გამოჩნდება. ცარიელი = ავტო-შემოკლება.")
    short_description_en = models.CharField(max_length=300, blank=True, verbose_name="Short Description - on card (EN)", help_text="1-2 sentences shown on listing. Empty = auto-truncated.")
    description_ge = models.TextField(verbose_name="სრული აღწერა - დეტალებზე (GE)")
    description_en = models.TextField(verbose_name="Full Description - on detail page (EN)")
    price = models.CharField(max_length=100, verbose_name="ფასი/ინვესტიცია")
    duration = models.CharField(max_length=100, blank=True, null=True, verbose_name="ხანგრძლივობა")
    icon = models.CharField(max_length=10, default="", blank=True, null=True, verbose_name="იკონი (emoji)")
    is_active = models.BooleanField(default=True, verbose_name="აქტიური")
    order = models.PositiveIntegerField(default=0, verbose_name="თანმიმდევრობა")
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name="ფოტო")

    class Meta:
        ordering = ['order']
        verbose_name = "სერვისი"
        verbose_name_plural = "სერვისები"

    def __str__(self):
        return self.title_ge


class Chakra(models.Model):
    number = models.PositiveIntegerField(verbose_name="ნომერი")
    name_ge = models.CharField(max_length=255, verbose_name="სახელი (GE)")
    name_en = models.CharField(max_length=255, verbose_name="Name (EN)")
    theme_ge = models.CharField(max_length=255, verbose_name="თემა (GE)")
    theme_en = models.CharField(max_length=255, verbose_name="Theme (EN)")
    conditions_ge = models.TextField(verbose_name="მდგომარეობები (GE)")
    conditions_en = models.TextField(verbose_name="Conditions (EN)")
    color = models.CharField(max_length=20, default="#e91e63", verbose_name="ფერი")
    icon = models.CharField(max_length=10, default="", blank=True, null=True, verbose_name="იკონი")
    image = models.ImageField(upload_to='chakras/', blank=True, null=True, verbose_name="ფოტო")
    description_ge = models.TextField(blank=True, null=True, verbose_name="აღწერა (GE)")
    description_en = models.TextField(blank=True, null=True, verbose_name="Description (EN)")

    class Meta:
        ordering = ['number']
        verbose_name = "ჩაკრა"
        verbose_name_plural = "ჩაკრები"

    def __str__(self):
        return f"{self.number}. {self.name_ge}"


class Course(models.Model):
    title_ge = models.CharField(max_length=255, verbose_name="სათაური (GE)")
    title_en = models.CharField(max_length=255, verbose_name="Title (EN)")
    subtitle_ge = models.CharField(max_length=500, blank=True, verbose_name="ქვეტექსტი (GE)")
    subtitle_en = models.CharField(max_length=500, blank=True, verbose_name="Subtitle (EN)")
    description_ge = models.TextField(verbose_name="აღწერა (GE)")
    description_en = models.TextField(verbose_name="Description (EN)")
    what_you_learn_ge = models.TextField(blank=True, verbose_name="რას ისწავლი (GE)")
    what_you_learn_en = models.TextField(blank=True, verbose_name="What You'll Learn (EN)")
    bonuses_ge = models.TextField(blank=True, verbose_name="ბონუსები (GE)")
    bonuses_en = models.TextField(blank=True, verbose_name="Bonuses (EN)")
    packages_title_ge = models.CharField(max_length=255, default="აირჩიე შენი პაკეტი", verbose_name="პაკეტების სექციის სათაური (GE)")
    packages_title_en = models.CharField(max_length=255, default="Choose Your Package", verbose_name="Packages Section Title (EN)")
    total_value_ge = models.CharField(max_length=100, default="2688 ₾", verbose_name="ჯამური ღირებულება (GE)")
    total_value_en = models.CharField(max_length=100, default="2688 ₾", verbose_name="Total Value (EN)")
    discount_code = models.CharField(max_length=50, default="888", verbose_name="ფასდაკლების კოდი")
    bank_accounts = models.TextField(blank=True, verbose_name="საბანკო ანგარიშები")
    registration_form_url = models.URLField(blank=True, verbose_name="გარე ფორმის ბმული")
    is_active = models.BooleanField(default=True, verbose_name="აქტიური")
    image = models.ImageField(upload_to='courses/', blank=True, null=True, verbose_name="ფოტო")

    class Meta:
        verbose_name = "კურსი"
        verbose_name_plural = "კურსები"

    def __str__(self):
        return self.title_ge


class CoursePackage(models.Model):
    course = models.ForeignKey(Course, related_name='packages', on_delete=models.CASCADE)
    name_ge = models.CharField(max_length=100, verbose_name="სახელი (GE)")
    name_en = models.CharField(max_length=100, verbose_name="Name (EN)")
    price = models.CharField(max_length=100, verbose_name="ფასი")
    features_ge = models.TextField(verbose_name="შეიცავს (GE)")
    features_en = models.TextField(verbose_name="Includes (EN)")
    is_featured = models.BooleanField(default=False, verbose_name="გამოსაყოფი")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "კურსის პაკეტი"
        verbose_name_plural = "კურსის პაკეტები"

    def __str__(self):
        return f"{self.course.title_ge} - {self.name_ge}"


class Retreat(models.Model):
    title_ge = models.CharField(max_length=255, verbose_name="სათაური (GE)")
    title_en = models.CharField(max_length=255, verbose_name="Title (EN)")
    date_range_ge = models.CharField(max_length=255, verbose_name="თარიღი (GE)", default="")
    date_range_en = models.CharField(max_length=255, verbose_name="Date (EN)", blank=True)
    location_ge = models.CharField(max_length=255, verbose_name="ადგილი (GE)")
    location_en = models.CharField(max_length=255, verbose_name="Location (EN)")
    price = models.CharField(max_length=100, verbose_name="ფასი")
    early_bird_price = models.CharField(max_length=100, blank=True, verbose_name="Early Bird ფასი")
    description_ge = models.TextField(verbose_name="აღწერა (GE)")
    description_en = models.TextField(verbose_name="Description (EN)")
    includes_ge = models.TextField(blank=True, verbose_name="ფასში შედის (GE)")
    includes_en = models.TextField(blank=True, verbose_name="Included (EN)")
    bank_accounts = models.TextField(blank=True, verbose_name="საბანკო ანგარიშები")
    is_active = models.BooleanField(default=True, verbose_name="აქტიური")
    image = models.ImageField(upload_to='retreats/', blank=True, null=True, verbose_name="ფოტო")
    disclaimer_ge = models.CharField(max_length=255, blank=True, default="* ფასში არ შედის ავიაბილეთები", verbose_name="შენიშვნა (GE)")
    disclaimer_en = models.CharField(max_length=255, blank=True, default="* Price excludes flight tickets", verbose_name="Disclaimer (EN)")

    class Meta:
        verbose_name = "რიტრიტი / მოგზაურობა"
        verbose_name_plural = "რიტრიტები / მოგზაურობები"

    def __str__(self):
        return self.title_ge


class RetreatDay(models.Model):
    retreat = models.ForeignKey(Retreat, related_name='days', on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField(verbose_name="დღე №")
    date_label = models.CharField(max_length=100, verbose_name="თარიღი (მაგ: 11 სექტემბერი)")
    date_label_en = models.CharField(max_length=100, blank=True, verbose_name="Date Label (EN) (e.g. 11 Sep)")
    title_ge = models.CharField(max_length=255, verbose_name="სათაური (GE)")
    title_en = models.CharField(max_length=255, verbose_name="Title (EN)")
    content_ge = models.TextField(verbose_name="პროგრამა (GE)")
    content_en = models.TextField(verbose_name="Program (EN)")

    class Meta:
        ordering = ['day_number']
        verbose_name = "პროგრამის დღე"
        verbose_name_plural = "პროგრამის დღეები"

    def __str__(self):
        return f"დღე {self.day_number}: {self.title_ge}"


class ContactInfo(models.Model):
    whatsapp = models.CharField(max_length=50, default="+995 597 71 84 67", verbose_name="WhatsApp")
    telegram = models.CharField(max_length=100, default="@wonderlanderr", verbose_name="Telegram")
    instagram = models.CharField(max_length=100, default="wonderlanderwellness", verbose_name="Instagram")
    email = models.EmailField(default="dr.guranda8@gmail.com", verbose_name="Email")
    
    # Bank Labels (Dynamic)
    bank_title_ge = models.CharField(max_length=100, default="საბანკო რეკვიზიტები", verbose_name="ბანკის სათაური (GE)")
    bank_title_en = models.CharField(max_length=100, default="Bank Details", verbose_name="Bank Title (EN)")
    bank_recipient_label_ge = models.CharField(max_length=100, default="მიმღები", verbose_name="მიმღების ლეიბლი (GE)")
    bank_recipient_label_en = models.CharField(max_length=100, default="Recipient", verbose_name="Recipient Label (EN)")
    bank_recipient_name = models.CharField(max_length=255, default="გურანდა ლაზარაშვილი", verbose_name="მიმღების სახელი (GE)")
    bank_recipient_name_en = models.CharField(max_length=255, default="Guranda Lazarashvili", verbose_name="Recipient Name (EN)")
    bank_iban_label = models.CharField(max_length=50, default="IBAN", verbose_name="IBAN ლეიბლი")
    bank_swift_label = models.CharField(max_length=50, default="SWIFT", verbose_name="SWIFT ლეიბლი")
    
    bank_accounts_ge = models.TextField(verbose_name="საბანკო რეკვიზიტები (GE)", blank=True)
    bank_accounts_en = models.TextField(verbose_name="Bank Details (EN)", blank=True)

    class Meta:
        verbose_name = "საკონტაქტო ინფორმაცია"
        verbose_name_plural = "საკონტაქტო ინფორმაცია"

    def __str__(self):
        return "საიტის კონტაქტები"


class Lead(models.Model):
    PURPOSE_CHOICES = [
        ('session', 'ინდივიდუალური სესია / Individual Session'),
        ('course', 'კურსები / Courses'),
        ('retreat', 'ბალის რიტრიტი / Bali Retreat'),
        ('mentoring', 'მენტორობა / Mentoring'),
    ]
    name = models.CharField(max_length=255, verbose_name="სახელი, გვარი")
    phone = models.CharField(max_length=50, verbose_name="ტელ. ნომერი")
    email = models.EmailField(blank=True, verbose_name="Email")
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES, verbose_name="სერვისი")
    message = models.TextField(blank=True, verbose_name="შეტყობინება")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="გამოგზავნილია")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "რეგისტრაცია"
        verbose_name_plural = "რეგისტრაციები"

    def __str__(self):
        return f"{self.name} - {self.get_purpose_display()}"


class Review(models.Model):
    name_ge = models.CharField(max_length=100, verbose_name="სახელი (GE)")
    name_en = models.CharField(max_length=100, verbose_name="Name (EN)", blank=True)
    text_ge = models.TextField(verbose_name="ტექსტი (GE)")
    text_en = models.TextField(verbose_name="Text (EN)", blank=True)
    rating = models.PositiveIntegerField(default=5, verbose_name="შეფასება (1-5)")
    image = models.ImageField(upload_to='reviews/', blank=True, null=True, verbose_name="ფოტო")
    is_active = models.BooleanField(default=True, verbose_name="აქტიური")
    order = models.PositiveIntegerField(default=0, verbose_name="თანმიმდევრობა")

    class Meta:
        ordering = ['order', '-id']
        verbose_name = "უკუკავშირი"
        verbose_name_plural = "უკუკავშირები"

    def __str__(self):
        return self.name_ge


class BotSettings(models.Model):
    bot_token = models.CharField(max_length=255, verbose_name="Bot Token")
    admin_chat_id = models.CharField(max_length=100, verbose_name="Admin Chat ID")

    # მთავარი ტექსტები
    welcome_text_ge = models.TextField(default="✨ მოგესალმებით Wonderlander Wellness-ში!\n\nაირჩიეთ ნებისმიერი სექცია ქვემოთ ⬇️", verbose_name="მისალმების ტექსტი")
    services_menu_text_ge = models.CharField(max_length=255, default="💫 ჩვენი სერვისები — აირჩიეთ:", verbose_name="სერვისების მენიუს ტექსტი")
    courses_menu_text_ge = models.CharField(max_length=255, default="📚 ჩვენი კურსები — აირჩიეთ:", verbose_name="კურსების მენიუს ტექსტი")
    contact_text_ge = models.TextField(default="📍 <b>კონტაქტი</b>\n\n📧 dr.guranda8@gmail.com", verbose_name="კონტაქტის ტექსტი")
    booking_success_text_ge = models.TextField(default="🎉 <b>განაცხადი მიღებულია!</b>\n\nგურანდა მალე დაგიკავშირდებათ! ✨", verbose_name="ჯავშნის დასრულების ტექსტი")

    # მთავარი მენიუს ღილაკები
    btn_services = models.CharField(max_length=100, default="🌟 სერვისები", verbose_name="ღილაკი: სერვისები")
    btn_courses = models.CharField(max_length=100, default="📚 კურსები", verbose_name="ღილაკი: კურსები")
    btn_booking = models.CharField(max_length=100, default="📅 ჩაწერა", verbose_name="ღილაკი: ჩაწერა")
    btn_contact = models.CharField(max_length=100, default="📞 კონტაქტი", verbose_name="ღილაკი: კონტაქტი")
    btn_language = models.CharField(max_length=100, default="🌐 ენა / Language", verbose_name="ღილაკი: ენა")
    btn_back = models.CharField(max_length=100, default="🔙 უკან", verbose_name="ღილაკი: უკან")
    btn_pay_label = models.CharField(max_length=100, default="💳 გადახდა", verbose_name="ღილაკი: გადახდა")
    btn_language_ge = models.CharField(max_length=100, default="🇬🇪 ქართული", verbose_name="ღილაკი: ქართული ენა")
    btn_language_en = models.CharField(max_length=100, default="🇬🇧 English", verbose_name="ღილაკი: ინგლისური ენა")

    # ჯავშნის პროცესი
    booking_ask_name = models.TextField(default="📝 <b>ჩაწერის ფორმა</b>\n\nგთხოვთ, შეიყვანეთ თქვენი <b>სახელი და გვარი</b>:", verbose_name="ჯავშანი: სახელის მოთხოვნა")
    booking_ask_phone = models.CharField(max_length=255, default="✅ მადლობა!\n\nშეიყვანეთ თქვენი <b>ტელეფონის ნომერი</b> (მაგ: +995599123456):", verbose_name="ჯავშანი: ნომრის მოთხოვნა")
    booking_admin_notify = models.TextField(default="🔔 <b>ახალი განაცხადი ბოტიდან!</b>", verbose_name="ადმინის შეტყობინების სათაური")

    # სხვა შეტყობინებები
    payment_soon_text = models.CharField(max_length=255, default="💳 გადახდის სისტემა მალე გაიხსნება!", verbose_name="გადახდის მიმდინარე ტექსტი")
    not_found_text = models.CharField(max_length=255, default="❌ ინფორმაცია ვერ მოიძებნა", verbose_name="ვერ მოიძებნა — ტექსტი")
    language_choice_text = models.CharField(max_length=255, default="Choose language / ენა:", verbose_name="ენის არჩევის ტექსტი")
    bot_started_text = models.CharField(max_length=255, default="🟢 <b>ბოტი ჩაირთო!</b> Wonderlander Wellness Bot is running.", verbose_name="ბოტის ჩართვის შეტყობინება")

    class Meta:
        verbose_name = "ბოტის პარამეტრები"
        verbose_name_plural = "ბოტის პარამეტრები"

    def __str__(self):
        return "Telegram ბოტის პარამეტრები"
