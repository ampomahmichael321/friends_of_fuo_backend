from django.contrib import admin

# Register your models here.
# disable recent actions on admin dashboard
admin.site.disable_action('view_recent_actions')