from django.contrib import admin
from .models import Panda, PandaToy, PandaSnack
# Register your models here.
admin.site.register(Panda)
admin.site.register(PandaToy)
admin.site.register(PandaSnack)
