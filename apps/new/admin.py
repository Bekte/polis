from django.contrib import admin
from apps.new.models import *

# Register your models here.
admin.site.register(Main)
admin.site.register(About)
admin.site.register(AboutPro)
admin.site.register(AboutProPhoto)
admin.site.register(AboutPhoto) 
                    
admin.site.register(AboutExperts)
admin.site.register(ParticipantNumbers)
admin.site.register(HelpMarketing)

admin.site.register(PictureMarketing)

admin.site.register(MarketingHead)
admin.site.register(MarketingBox)

admin.site.register(Service)
admin.site.register(ServiceList)
class SvgAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'icon_class')

admin.site.register(ReviewPhrases)
admin.site.register(ReviewList)

admin.site.register(Goods)
admin.site.register(GoodsPicture)
admin.site.register(Registartion)
admin.site.register(Blog)
admin.site.register(BlogPicture)
admin.site.register(Adresses)
admin.site.register(NavigBar)
