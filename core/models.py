from django.db import models


class SiteSettings(models.Model):
    site_title_ge = models.CharField(max_length=255, default="Wonderlander Wellness")
    site_title_en = models.CharField(max_length=255, default="Wonderlander Wellness")
    hero_title_ge = models.CharField(max_length=500, default="ინდივიდუალურ სესიაზე რეგისტრაცია")
    hero_title_en = models.CharField(max_length=500, default="Individual Session Registration")
    hero_subtitle_ge = models.TextField(default="გამარჯობა. პირველ რიგში, მადლობა ნდობისთვის ☀️")
    hero_subtitle_en = models.TextField(default="Hello. First of all, thank you for your trust ☀️")
    about_text_ge = models.TextField(verbose_name="ჩემს შესახებ (GE)", blank=True)
    about_text_en = models.TextField(verbose_name="About Me (EN)", blank=True)
    credentials_ge = models.TextField(verbose_name="კვალიფიკაცია (GE)", blank=True)
    credentials_en = models.TextField(verbose_name="Credentials (EN)", blank=True)
    hero_image = models.ImageField(upload_to='hero/', blank=True, null=True)

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
