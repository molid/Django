from django.contrib import admin
from TestModel.models import Test,Contact,Tag,Question, Choice
# Register your models here.
# admin.site.register(Test)


# admin.site.register([Test, Contact, Tag])


# class ContactAdmin(admin.ModelAdmin):
#     fields = ('name', 'email')
#
#
# admin.site.register(Contact, ContactAdmin)
# admin.site.register([Test, Tag])

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # list
    search_fields = ('name',)
    inlines = [TagInline]
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
admin.site.site_header = "Molid"