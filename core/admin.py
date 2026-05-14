from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import SiteSettings, Service, Chakra, Course, Retreat, Lead, ContactInfo

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Global & Navbar', {
            'fields': ('site_title_ge', 'site_title_en', 'navbar_cta_ge', 'navbar_cta_en', 
                       'nav_home_ge', 'nav_course_ge', 'nav_retreat_ge', 'nav_contact_ge')
        }),
        ('Hero Section', {
            'fields': ('hero_badge_ge', 'hero_title_ge', 'hero_subtitle_ge', 
                       'hero_btn1_ge', 'hero_btn2_ge', 'hero_creds_ge')
        }),
        ('Intro & Stats', {
            'fields': ('stat1_num', 'stat1_label_ge', 'stat2_num', 'stat2_label_ge', 
                       'stat3_num', 'stat3_label_ge', 'stat4_num', 'stat4_label_ge', 
                       'intro_tags_ge')
        }),
        ('Section Titles', {
            'fields': ('services_title_ge', 'chakras_title_ge', 'about_title_ge')
        }),
        ('About Me', {
            'fields': ('about_text_ge',)
        }),
        ('Footer', {
            'fields': ('footer_copy_ge',)
        }),
    )

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Social & Links', {
            'fields': ('whatsapp', 'telegram', 'instagram', 'email')
        }),
        ('Bank Details Labels', {
            'fields': ('bank_title_ge', 'bank_recipient_label_ge', 'bank_recipient_name', 'bank_iban_label', 'bank_swift_label')
        }),
        ('Bank Accounts Content', {
            'fields': ('bank_accounts_ge', 'bank_accounts_en')
        }),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title_ge', 'price', 'image_preview')
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" style="border-radius:5px;" />')
        return "No Image"

@admin.register(Chakra)
class ChakraAdmin(admin.ModelAdmin):
    list_display = ('number', 'name_ge', 'image_preview')
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" style="border-radius:5px;" />')
        return "No Image"

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title_ge', 'is_active')

@admin.register(Retreat)
class RetreatAdmin(admin.ModelAdmin):
    list_display = ('title_ge', 'price')

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'purpose', 'created_at')
    list_filter = ('purpose', 'created_at')
