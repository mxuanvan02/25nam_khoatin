from django.contrib import admin
from .models import Image, Join, Cooperate, Activity, MailAdmin, Link_QRCode, Title



MAX_OBJECTS = 1


class OneObj(admin.ModelAdmin):
  

  def has_add_permission(self, request):
    if self.model.objects.count() >= MAX_OBJECTS:
      return False
    return super().has_add_permission(request)



class ImageAdmin(admin.ModelAdmin):
  def status_true(modeladmin, request, queryset):
    return queryset.update(status='True')

  def status_false(modeladmin, request, queryset):
    return queryset.update(status='False')



  list_display = ['year', 'status']
  ordering = ['year']
  actions = [status_true, status_false]

class ActivitiAdmin(admin.ModelAdmin):
  def status_true(modeladmin, request, queryset):
    return queryset.update(status='True')

  def status_false(modeladmin, request, queryset):
    return queryset.update(status='False')




  list_display = ['name', 'status']
  ordering = ['name']
  actions = [status_true, status_false]



class JoinAdmin(admin.ModelAdmin):
  list_display = ['name', 'year', 'email', 'attend']

class MailAdminAdmin(admin.ModelAdmin):
  list_display = ['name', 'email']



admin.site.register(Join, JoinAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Cooperate)
admin.site.register(Title)
admin.site.register(Activity, ActivitiAdmin)
admin.site.register(MailAdmin, MailAdminAdmin)
admin.site.register(Link_QRCode, OneObj)


