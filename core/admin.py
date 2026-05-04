from django.contrib import admin
from .models import Service, Chakra, Course, CoursePackage, Retreat, RetreatDay, ContactInfo, Lead, SiteSettings

# Customize Admin Dashboard Headers
admin.site.site_header = "Wonderlander Wellness"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "მართვის პანელი"

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title_ge', 'price', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)

@admin.register(Chakra)
class ChakraAdmin(admin.ModelAdmin):
    list_display = ('number', 'name_ge', 'theme_ge', 'color')
    list_editable = ('color',)
    ordering = ('number',)

class CoursePackageInline(admin.StackedInline):
    model = CoursePackage
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title_ge', 'is_active')
    inlines = [CoursePackageInline]

class RetreatDayInline(admin.StackedInline):
    model = RetreatDay
    extra = 0

@admin.register(Retreat)
class RetreatAdmin(admin.ModelAdmin):
    list_display = ('title_ge', 'date_range', 'price', 'is_active')
    inlines = [RetreatDayInline]

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Allow only one instance of ContactInfo
        return not ContactInfo.objects.exists()

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Allow only one instance of SiteSettings
        return not SiteSettings.objects.exists()

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'purpose', 'created_at')
    list_filter = ('purpose',)
    search_fields = ('name', 'phone', 'email')
    readonly_fields = ('created_at',)
