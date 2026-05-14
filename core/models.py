from django.db import models


class SiteSettings(models.Model):
    # Global & Navbar
    site_title_ge = models.CharField(max_length=255, default="Wonderlander Wellness")
    site_title_en = models.CharField(max_length=255, default="Wonderlander Wellness")
    navbar_cta_ge = models.CharField(max_length=50, default="ჩაწერა", verbose_name="ნავბარის ღილაკი (GE)")
    navbar_cta_en = models.CharField(max_length=50, default="Book Now", verbose_name="ნავბარის ღილაკი (EN)")
    nav_home_ge = models.CharField(max_length=50, default="მთავარი")
    nav_course_ge = models.CharField(max_length=50, default="ფემინური სიმდიდრე")
    nav_retreat_ge = models.CharField(max_length=50, default="ბალი")
    nav_contact_ge = models.CharField(max_length=50, default="კონტაქტი")
    
    # Hero Section
    hero_badge_ge = models.CharField(max_length=100, default="✦ WONDERLANDER WELLNESS")
    hero_title_ge = models.TextField(default="საკუთარ თავთან ჰარმონიული ურთიერთობა")
    hero_subtitle_ge = models.TextField(default="გამარჯობა. მადლობა ნდობისთვის ☀️")
    hero_btn1_ge = models.CharField(max_length=50, default="ჩაწერა ❣️")
    hero_btn2_ge = models.CharField(max_length=50, default="სერვისები")
    hero_creds_ge = models.CharField(max_length=255, default="🎓 MD, 🧠 NLP, 🌿 Holistic, 🔥 Kundalini", help_text="მძიმით გამოყოფილი")
    hero_image = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name="მთავარი (Hero) ფოტო")
    
    # Intro Statistics (4 slots)
    stat1_num = models.CharField(max_length=20, default="10x")
    stat1_label_ge = models.CharField(max_length=100, default="უფრო სწრაფი შედეგი")
    stat2_num = models.CharField(max_length=20, default="1-5")
    stat2_label_ge = models.CharField(max_length=100, default="სესია მიზნისთვის")
    stat3_num = models.CharField(max_length=20, default="7")
    stat3_label_ge = models.CharField(max_length=100, default="ენერგეტ. ცენტრი")
    stat4_num = models.CharField(max_length=20, default="💎")
    stat4_label_ge = models.CharField(max_length=100, default="სამოქმ. გეგმა")
    
    # Tags
    intro_tags_ge = models.TextField(default="ფსიქო-სომატიკა, NLP, ჰიპნოთერაპია, კუნდალინი, EFT, არტ თერაპია, იოგა, მედიტაცია")

    # Section Titles
    services_title_ge = models.CharField(max_length=255, default="ინვესტიცია საკუთარ თავში")
    chakras_title_ge = models.CharField(max_length=255, default="რა მდგომარეობის დროს მომმართოთ?")
    about_title_ge = models.CharField(max_length=255, default="გურანდა ლაზარაშვილი")
    
    # About Section
    about_text_ge = models.TextField(verbose_name="ჩემს შესახებ (GE)", blank=True)
    about_image = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name="პროფილის (About) ფოტო")
    
    # Footer
    footer_copy_ge = models.CharField(max_length=255, default="© 2024 Wonderlander Wellness. ყველა უფლება დაცულია.")


    class Meta:
        verbose_name = "საიტის პარამეტრები"
        verbose_name_plural = "საიტის პარამეტრები"

    def __str__(self):
        return "საიტის პარამეტრები"


class Service(models.Model):
    title_ge = models.CharField(max_length=255, verbose_name="სათაური (GE)")
    title_en = models.CharField(max_length=255, verbose_name="Title (EN)")
    description_ge = models.TextField(verbose_name="აღწერა (GE)")
    description_en = models.TextField(verbose_name="Description (EN)")
    price = models.CharField(max_length=100, verbose_name="ფასი/ინვესტიცია")
    duration = models.CharField(max_length=100, blank=True, null=True, verbose_name="ხანგრძლივობა")
    icon = models.CharField(max_length=10, default="🧩", verbose_name="იკონი (emoji)")
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
    icon = models.CharField(max_length=10, default="🧩", verbose_name="იკონი")
    image = models.ImageField(upload_to='chakras/', blank=True, null=True, verbose_name="ფოტო")

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
    date_range = models.CharField(max_length=255, verbose_name="თარიღი")
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

    class Meta:
        verbose_name = "რიტრიტი / მოგზაურობა"
        verbose_name_plural = "რიტრიტები / მოგზაურობები"

    def __str__(self):
        return self.title_ge


class RetreatDay(models.Model):
    retreat = models.ForeignKey(Retreat, related_name='days', on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField(verbose_name="დღე №")
    date_label = models.CharField(max_length=100, verbose_name="თარიღი (მაგ: 11 სექტემბერი)")
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
    bank_recipient_label_ge = models.CharField(max_length=100, default="მიმღები", verbose_name="მიმღების ლეიბლი (GE)")
    bank_recipient_name = models.CharField(max_length=255, default="გურანდა ლაზარაშვილი", verbose_name="მიმღების სახელი")
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
        ('session', 'ინდივიდუალური სესია'),
        ('course', 'კურსი - ფემინური სიმდიდრე'),
        ('retreat', 'ბალის რიტრიტი'),
        ('mentoring', 'მენტორობა'),
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
