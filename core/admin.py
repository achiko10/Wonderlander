from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import SiteSettings, Service, Chakra, Course, CoursePackage, Retreat, RetreatDay, RetreatActivity, Lead, ContactInfo, Review, BotSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('🌐 საიტის მთავარი პარამეტრები & მენიუ', {
            'fields': (
                'site_title_ge', 'site_title_en',
                'navbar_cta_ge', 'navbar_cta_en',
                'nav_home_ge', 'nav_home_en',
                'nav_course_ge', 'nav_course_en',
                'nav_retreat_ge', 'nav_retreat_en',
                'nav_contact_ge', 'nav_contact_en',
                'nav_review_ge', 'nav_review_en'
            ),
            'description': 'საიტის ძირითადი სათაურები, ლოგოს ტექსტი და მენიუს ღილაკების სახელები.'
        }),
        ('✨ მთავარი სექცია (Hero Section)', {
            'fields': (
                'hero_badge_ge', 'hero_badge_en',
                'hero_title_ge', 'hero_title_en',
                'hero_subtitle_ge', 'hero_subtitle_en',
                'hero_btn1_ge', 'hero_btn1_en',
                'hero_btn2_ge', 'hero_btn2_en',
                'hero_creds_ge', 'hero_creds_en',
                'hero_image'
            ),
            'description': 'მთავარი გვერდის პირველი ბლოკი - დიდი სურათი, მთავარი სათაურები და ღილაკები.'
        }),
        ('📊 სტატისტიკა & ტეგები (Stats & Tags)', {
            'fields': (
                'stat1_num', 'stat1_label_ge', 'stat1_label_en',
                'stat2_num', 'stat2_label_ge', 'stat2_label_en',
                'stat3_num', 'stat3_label_ge', 'stat3_label_en',
                'stat4_num', 'stat4_label_ge', 'stat4_label_en',
                'intro_tags_ge', 'intro_tags_en'
            ),
            'description': 'საიტზე არსებული ციფრები/სტატისტიკა და ტეგების ჩამონათვალი.'
        }),
        ('📄 სექციების სათაურები (Section Titles)', {
            'fields': (
                'services_title_ge', 'services_title_en',
                'chakras_title_ge', 'chakras_title_en',
                'about_title_ge', 'about_title_en',
                'reviews_title_ge', 'reviews_title_en',
                'reviews_empty_text_ge', 'reviews_empty_text_en'
            ),
            'description': 'სხვადასხვა სექციის სათაურები მთავარ გვერდზე.',
            'classes': ('collapse',),
        }),
        ('👤 ჩემს შესახებ (About Me)', {
            'fields': ('about_text_ge', 'about_text_en', 'about_image'),
            'description': 'თქვენი ბიოგრაფია, ფოტო და აღწერა.'
        }),
        ('🛡️ რატომ ჩემთან? & ქვედა ბანერი (CTA)', {
            'fields': (
                'home_why_title_ge', 'home_why_title_en',
                'home_why_text1_ge', 'home_why_text1_en',
                'home_why_text2_ge', 'home_why_text2_en',
                'home_cta_title_ge', 'home_cta_title_en',
                'home_cta_text_ge', 'home_cta_text_en'
            ),
            'description': 'ტექსტები, სადაც განმარტავთ რატომ უნდა აგირჩიონ თქვენ და მთავარი გვერდის ბოლო სარეგისტრაციო ბლოკი.'
        }),
        ('🏷️ საიტის პატარა ტექსტები და ღილაკები (UI Labels)', {
            'fields': (
                'label_details_ge', 'label_details_en',
                'label_popular_ge', 'label_popular_en',
                'label_save_ge', 'label_save_en',
                'label_book_session_ge', 'label_book_session_en',
                'label_our_courses_ge', 'label_our_courses_en',
                'label_choose_course_ge', 'label_choose_course_en',
                'label_course_ge', 'label_course_en',
                'label_you_feel_ge', 'label_you_feel_en',
                'label_what_learn_ge', 'label_what_learn_en',
                'label_total_value_ge', 'label_total_value_en',
                'label_guarantee_ge', 'label_guarantee_en',
                'label_let_start_ge', 'label_let_start_en',
                'label_booking_ge', 'label_booking_en',
                'label_submit_app_ge', 'label_submit_app_en',
                'label_included_ge', 'label_included_en',
                'label_program_ge', 'label_program_en',
                'label_early_bird_ge', 'label_early_bird_en',
                'label_regular_price_ge', 'label_regular_price_en',
                'label_energy_centers_ge', 'label_energy_centers_en',
                'label_choose_chakra_ge', 'label_choose_chakra_en',
                'label_enroll_ge', 'label_enroll_en',
                'label_book_ge', 'label_book_en',
                'label_select_ge', 'label_select_en',
                'label_bonuses_ge', 'label_bonuses_en',
                'label_whatsapp_btn_ge', 'label_whatsapp_btn_en',
            ),
            'classes': ('collapse',),
            'description': '⚠️ ყურადღება: ამ სექციაში მოცემულია საიტის პატარა ღილაკების და წარწერების თარგმანები. ჩვეულებრივ რეჟიმში მათი შეცვლა საჭირო არ არის.'
        }),
        ('👣 საიტის ქვედა ნაწილი (Footer)', {
            'fields': ('footer_copy_ge', 'footer_copy_en'),
            'classes': ('collapse',),
        }),
    )

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Social & Links', {
            'fields': ('whatsapp', 'telegram', 'instagram', 'email')
        }),
        ('Bank Details Labels', {
            'fields': (
                'bank_title_ge', 'bank_title_en',
                'bank_recipient_label_ge', 'bank_recipient_label_en', 
                'bank_recipient_name', 'bank_recipient_name_en',
                'bank_iban_label', 'bank_swift_label'
            )
        }),
        ('Bank Accounts Content', {
            'fields': ('bank_accounts_ge', 'bank_accounts_en')
        }),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title_ge', 'price', 'duration', 'is_active', 'order', 'image_preview')
    list_editable = ('order', 'is_active')
    
    fieldsets = (
        ('⚙️ ძირითადი პარამეტრები', {
            'fields': ('is_active', 'order', 'price', 'duration', 'icon', 'image')
        }),
        ('🇬🇪 ქართული ვერსია (Georgian)', {
            'fields': ('title_ge', 'short_description_ge', 'description_ge')
        }),
        ('🇬🇧 ინგლისური ვერსია (English)', {
            'fields': ('title_en', 'short_description_en', 'description_en'),
            'classes': ('collapse',),
            'description': 'შეავსეთ ინგლისური ვერსიისთვის (არასავალდებულო).'
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" style="border-radius:5px;" />')
        return "—"
    image_preview.short_description = 'ფოტო'

from django import forms
class ChakraAdminForm(forms.ModelForm):
    class Meta:
        model = Chakra
        fields = '__all__'
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 80px; cursor: pointer;'}),
        }

@admin.register(Chakra)
class ChakraAdmin(admin.ModelAdmin):
    form = ChakraAdminForm
    list_display = ('number', 'name_ge', 'color_preview', 'image_preview')
    
    fieldsets = (
        ('⚙️ ძირითადი პარამეტრები', {
            'fields': ('number', 'color', 'icon', 'image')
        }),
        ('🇬🇪 ქართული ვერსია (Georgian)', {
            'fields': ('name_ge', 'theme_ge', 'conditions_ge', 'description_ge')
        }),
        ('🇬🇧 ინგლისური ვერსია (English)', {
            'fields': ('name_en', 'theme_en', 'conditions_en', 'description_en'),
            'classes': ('collapse',),
            'description': 'შეავსეთ ინგლისური ვერსიისთვის (არასავალდებულო).'
        }),
    )

    def color_preview(self, obj):
        return mark_safe(f'<div style="width: 25px; height: 25px; border-radius: 50%; background-color: {obj.color}; border: 1px solid #ccc;"></div>')
    color_preview.short_description = 'ფერი'

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" style="border-radius:5px;" />')
        return "—"
    image_preview.short_description = 'ფოტო'

class CoursePackageInline(admin.TabularInline):
    model = CoursePackage
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title_ge', 'is_active', 'image_preview')
    inlines = [CoursePackageInline]
    
    fieldsets = (
        ('⚙️ ძირითადი პარამეტრები', {
            'fields': ('is_active', 'image', 'discount_code', 'registration_form_url')
        }),
        ('🇬🇪 ქართული ვერსია (Georgian)', {
            'fields': ('title_ge', 'subtitle_ge', 'description_ge', 'what_you_learn_ge', 'bonuses_ge', 'packages_title_ge', 'total_value_ge')
        }),
        ('🇬🇧 ინგლისური ვერსია (English)', {
            'fields': ('title_en', 'subtitle_en', 'description_en', 'what_you_learn_en', 'bonuses_en', 'packages_title_en', 'total_value_en'),
            'classes': ('collapse',),
            'description': 'შეავსეთ ინგლისური ვერსიისთვის (არასავალდებულო).'
        }),
        ('🔗 რეკვიზიტები', {
            'fields': ('bank_accounts',),
            'classes': ('collapse',),
            'description': 'საბანკო რეკვიზიტები სპეციალურად ამ კურსისთვის.'
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" style="border-radius:5px;" />')
        return "—"
    image_preview.short_description = 'ფოტო'

@admin.register(Retreat)
class RetreatAdmin(admin.ModelAdmin):
    list_display = ('title_ge', 'price', 'is_active')
    inlines = [RetreatDayInline]
    
    fieldsets = (
        ('⚙️ ძირითადი პარამეტრები', {
            'fields': ('is_active', 'price', 'early_bird_price', 'image')
        }),
        ('🇬🇪 ქართული ვერსია (Georgian)', {
            'fields': ('title_ge', 'date_range_ge', 'location_ge', 'description_ge', 'includes_ge', 'disclaimer_ge')
        }),
        ('🇬🇧 ინგლისური ვერსია (English)', {
            'fields': ('title_en', 'date_range_en', 'location_en', 'description_en', 'includes_en', 'disclaimer_en'),
            'classes': ('collapse',),
            'description': 'შეავსეთ ინგლისური ვერსიისთვის (არასავალდებულო).'
        }),
        ('🔗 რეკვიზიტები', {
            'fields': ('bank_accounts',),
            'classes': ('collapse',),
            'description': 'საბანკო რეკვიზიტები სპეციალურად ამ რიტრიტისთვის.'
        }),
    )

@admin.register(RetreatDay)
class RetreatDayAdmin(admin.ModelAdmin):
    list_display = ('retreat', 'day_number', 'date_label', 'title_ge')
    list_filter = ('retreat',)
    inlines = [RetreatActivityInline]
    
    fieldsets = (
        ('⚙️ ძირითადი პარამეტრები', {
            'fields': ('retreat', 'day_number')
        }),
        ('🇬🇪 ქართული ვერსია (Georgian)', {
            'fields': ('date_label', 'title_ge', 'content_ge')
        }),
        ('🇬🇧 ინგლისური ვერსია (English)', {
            'fields': ('date_label_en', 'title_en', 'content_en'),
            'classes': ('collapse',),
            'description': 'შეავსეთ ინგლისური ვერსიისთვის (არასავალდებულო).'
        }),
    )

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'purpose', 'created_at')
    list_filter = ('purpose', 'created_at')
    readonly_fields = ('name', 'phone', 'email', 'purpose', 'message', 'created_at')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name_ge', 'rating', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    
    fieldsets = (
        ('⚙️ პარამეტრები', {
            'fields': ('is_active', 'order', 'rating', 'image')
        }),
        ('🇬🇪 ქართული ვერსია (Georgian)', {
            'fields': ('name_ge', 'text_ge')
        }),
        ('🇬🇧 ინგლისური ვერსია (English)', {
            'fields': ('name_en', 'text_en'),
            'classes': ('collapse',),
            'description': 'შეავსეთ ინგლისური ვერსიისთვის (არასავალდებულო).'
        }),
    )

@admin.register(BotSettings)
class BotSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('🔑 ტექნიკური პარამეტრები (ბოტის კავშირი)', {
            'fields': ('bot_token', 'admin_chat_id'),
            'description': '⚠️ ყურადღება: ბოტის ტოკენი და ადმინისტრატორის ID. არ შეცვალოთ მფლობელის გარეშე.'
        }),
        ('💬 მისალმება და ძირითადი ტექსტები', {
            'fields': (
                'welcome_text_ge',
                'services_menu_text_ge',
                'courses_menu_text_ge',
                'contact_text_ge',
                'booking_success_text_ge',
                'language_choice_text',
            ),
            'description': 'ტელეგრამ ბოტში გამოსაჩენი მისალმებები და განმარტებითი ტექსტები.'
        }),
        ('📅 ჩაწერის პროცესი (Booking)', {
            'fields': (
                'booking_ask_name',
                'booking_ask_phone',
                'booking_admin_notify',
            ),
            'description': 'ტექსტები, რომლებიც ბოტში ჩაწერის დროს იგზავნება.'
        }),
        ('🔘 ბოტის მენიუს ღილაკები', {
            'fields': (
                'btn_services',
                'btn_courses',
                'btn_booking',
                'btn_contact',
                'btn_language',
                'btn_back',
                'btn_pay_label',
                'btn_language_ge',
                'btn_language_en',
            ),
            'description': 'ღილაკების სახელები. შეგიძლიათ ჩასვათ ემოჯები.',
            'classes': ('collapse',),
        }),
        ('⚙️ დამხმარე შეტყობინებები', {
            'fields': (
                'payment_soon_text',
                'not_found_text',
                'bot_started_text',
            ),
            'classes': ('collapse',),
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

