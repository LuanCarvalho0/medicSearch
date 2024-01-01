from django.contrib import admin
from medicSearch.models import Profile, State, City, Neighborhood, Address \
, DayWeek, Rating, Speciality


class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user', 'role', 'birth', 'specialitesList', 'addressesList',)
    list_display_links = ('user', 'role',)
    list_filter = ('user__is_active',)
    #fields = ('user', ('role', ), 'image', 'birthday', 'specialites', 'addresses',)
    exclude = ('favorites', 'created_at', 'updated_at',)
    empty_value_display  = 'vazio'
    readonly_fields = ('user',)
    search_fields = ('user__username',)

    fieldsets = (
        ('Usuário', {
            'fields': ('user', 'birthday', 'image')
        }),
        ('Função', {
            'fields': ('role',)
        }),
        ('Extras', {
            'fields': ('specialites', 'addresses')
        }),
    )

    def birth(self, obj):
        if obj.birthday:
            return obj.birthday.strftime('%d/%m/%Y')
    birth.empty_value_display = '__/__/____'

    def specialitesList(self, obj):
        return [i.name for i in obj.specialites.all()]
    
    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
