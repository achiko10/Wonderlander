from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import SiteSettings, Service, Chakra, Course, CoursePackage, Retreat, RetreatDay, Lead, ContactInfo

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Global & Navbar', {
            'fields': (
                'site_title_ge', 'site_title_en',
                'navbar_cta_ge', 'navbar_cta_en',
                'nav_home_ge', 'nav_home_en',
                'nav_course_ge', 'nav_course_en',
                'nav_retreat_ge', 'nav_retreat_en',
                'nav_contact_ge', 'nav_contact_en'
            )
        }),
        ('Hero Section', {
            'fields': (
                'hero_badge_ge', 'hero_badge_en',
                'hero_title_ge', 'hero_title_en',
                'hero_subtitle_ge', 'hero_subtitle_en',
                'hero_btn1_ge', 'hero_btn1_en',
                'hero_btn2_ge', 'hero_btn2_en',
                'hero_creds_ge', 'hero_creds_en',
                'hero_image'
            )
        }),
        ('Intro & Stats', {
            'fields': (
                'stat1_num', 'stat1_label_ge', 'stat1_label_en',
                'stat2_num', 'stat2_label_ge', 'stat2_label_en',
                'stat3_num', 'stat3_label_ge', 'stat3_label_en',
                'stat4_num', 'stat4_label_ge', 'stat4_label_en',
                'intro_tags_ge', 'intro_tags_en'
            )
        }),
        ('Section Titles', {
            'fields': (
                'services_title_ge', 'services_title_en',
                'chakras_title_ge', 'chakras_title_en',
                'about_title_ge', 'about_title_en'
            )
        }),
        ('About Me', {
            'fields': ('about_text_ge', 'about_text_en', 'about_image')
        }),
        ('Footer', {
            'fields': ('footer_copy_ge', 'footer_copy_en')
        }),
        ('UI Labels (Buttons & Text)', {
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
                'label_submit_app_ge', 'label_submit_app_en'
            ),
            'classes': ('collapse',),
            'description': 'აქედან შეგიძლიათ შეცვალოთ საიტზე არსებული ყველა პატარა ტექსტი და ღილაკი.'
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
        ('სათაური და ძირითადი', {
            'fields': ('icon', 'title_ge', 'title_en', 'price', 'duration', 'order', 'is_active', 'image')
        }),
        ('📋 მოკლე ტექსტი — კარტზე (ჩამოთვლის გვერდი)', {
            'fields': ('short_description_ge', 'short_description_en'),
            'description': '⚠️ ეს ტექსტი გამოჩნდება სერვისების ბარათებზე მთავარ გვერდზე. შეავსეთ 1-2 წინადადება. ცარიელია = ავტომატური შემოკლება.'
        }),
        ('📄 სრული ტექსტი — დეტალების გვერდი', {
            'fields': ('description_ge', 'description_en'),
            'description': 'სრული ტექსტი ჩანს მხოლოდ "დეტალურად" ღილაკზე დაჭერის შემდეგ.'
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" style="border-radius:5px;" />')
        return "—"
    image_preview.short_description = 'ფოტო'

@admin.register(Chakra)
class ChakraAdmin(admin.ModelAdmin):
    list_display = ('number', 'name_ge', 'image_preview')
    fieldsets = (
        ('ძირითადი ინფორმაცია', {
            'fields': ('number', 'icon', 'name_ge', 'name_en', 'theme_ge', 'theme_en', 'color', 'image')
        }),
        ('📋 მოკლე ჩამონათვალი — კარტზე (რა მდგომარეობის დროს?)', {
            'fields': ('conditions_ge', 'conditions_en'),
            'description': 'ეს ტექსტი გამოჩნდება მთავარ გვერდზე, ჩაკრის ბარათზე (ავტომატურად შემოკლდება).'
        }),
        ('📄 სრული აღწერა — დეტალების გვერდი', {
            'fields': ('description_ge', 'description_en'),
            'description': 'სრული ტექსტი, რომელიც გამოჩნდება მხოლოდ ჩაკრის დეტალურ გვერდზე.'
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" style="border-radius:5px;" />')
        return "No Image"
    image_preview.short_description = 'ფოტო'

class CoursePackageInline(admin.TabularInline):
    model = CoursePackage
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title_ge', 'is_active', 'image_preview')
    inlines = [CoursePackageInline]
    
    fieldsets = (
        ('ძირითადი ინფორმაცია', {
            'fields': ('title_ge', 'title_en', 'subtitle_ge', 'subtitle_en', 'is_active', 'image')
        }),
        ('📄 აღწერა და სწავლება', {
            'fields': ('description_ge', 'description_en', 'what_you_learn_ge', 'what_you_learn_en')
        }),
        ('🎁 ბონუსები და ღირებულება', {
            'fields': ('bonuses_ge', 'bonuses_en', 'total_value_ge', 'total_value_en', 'discount_code')
        }),
        ('🏷️ პაკეტების სექცია', {
            'fields': ('packages_title_ge', 'packages_title_en'),
            'description': 'სათაური, რომელიც გამოჩნდება პაკეტების (პრაისინგის) სექციაში.'
        }),
        ('🔗 ბმულები და რეკვიზიტები', {
            'fields': ('bank_accounts', 'registration_form_url')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" style="border-radius:5px;" />')
        return "—"
    image_preview.short_description = 'ფოტო'

class RetreatDayInline(admin.TabularInline):
    model = RetreatDay
    extra = 1

@admin.register(Retreat)
class RetreatAdmin(admin.ModelAdmin):
    list_display = ('title_ge', 'price')
    inlines = [RetreatDayInline]

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'purpose', 'created_at')
    list_filter = ('purpose', 'created_at')
