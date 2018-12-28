from django.contrib import admin
from .models import Category,SetOfQuestion,Group,Question,Answer,Membership,Copy
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    fieldsests = (
                    ('Information',{'fields':('Name','Description')}),
                    ('Sets',{'fields':('SetsOfQuestions')}),
                    )
    list_display = ('Name','group_name','count_of_sets')
    search_fields = ('Name','group_name','count_of_sets')
    def group_name(self,obj):
        return obj.Group
    def count_of_sets(self,obj):
        return obj.SetsOfQuestions.all().count()
admin.site.register(Category,CategoryAdmin)

class CategoryInline(admin.StackedInline):
    model = Category
class GroupAdmin(admin.ModelAdmin):
    fieldsests = (
                    ('Information',{'fields':('Name','Description')}),
                    )
    inlines = [CategoryInline,]
    list_display = ('Name','count_of_categories')
    search_fields = ('Name','count_of_categories')
    def count_of_categories(self,obj):
        return Category.objects.get(Group=obj).count()
admin.site.register(Group,GroupAdmin)

class MembershipAdmin(admin.ModelAdmin):
    fields = ('Group','User','Role')
    list_display = ('Group','User','Role')
    search_fields = ('Group','User','Role')
    list_filter = ('Role')
admin.site.register(Membership,MembershipAdmin)

class SetOfQuestionsAdmin(admin.ModelAdmin):
    fieldsests = (
                    ('Information',{'fields':('Name','Author','Public')}),
                    ('Questions',{'fields':('Question')}),
                    )
    list_display = ('Name','Author','Public')
    list_editable = ('Public')
    list_filter = ('Public')
    search_fields = ('Name','Author')
admin.site.register(SetOfQuestions,SetOfQuestionsAdmin)

class AnswerAdmin(admin.ModelAdmin):
    fields = ('Content','True','Question')
    list_display = ('Content','True')
    list_filter = ('True')
admin.site.register(Answer,AnswerAdmin)

class QuestionAdmin(admin.ModelAdmin):
    fields = ('Content')
    list_display = ('Content','count_of_answer')
    list_filter = ('count_of_answer')
    def count_of_answer(self,obj):
        return Answer.objects.get(Question=obj).count()
admin.site.register(Question,QuestionAdmin)

admin.site.register(Copy)
