from django.contrib import admin
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


class MyAdminSite(admin.AdminSite):
    site_header = "DGFS"
    path = BASE_DIR / "statics"

    class Meta:
        css = {
            'all': (os.path.join(BASE_DIR, "static/admin.css"),),
        }


admin_site = MyAdminSite(name="myadmin")
