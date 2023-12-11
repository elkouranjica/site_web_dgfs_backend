from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_header = "DGFS"


admin_site = MyAdminSite(name="myadmin")
