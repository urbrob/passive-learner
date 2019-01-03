from django.contrib import admin
from .models import Category, SetOfQuestion, Group, Question, Answer, Membership, Copy, UserInfo
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    fieldsests = (
        ('Information', {'fields': ('Name', 'Description')}),
        ('Sets', {'fields': ('SetsOfQuestions')}),
    )
    list_display = ('Name', 'group_name', 'count_of_sets')
    search_fields = ('Name', 'group_name', 'count_of_sets')

    def group_name(self, obj):
        return obj.group

    def count_of_sets(self, obj):
        return obj.SetsOfQuestions.all().count()


admin.site.register(Category, CategoryAdmin)


class CategoryInline(admin.StackedInline):
    model = Category


class GroupAdmin(admin.ModelAdmin):
    fieldsests = (
        ('Information', {'fields': ('name', 'description')}),
    )
    inlines = [CategoryInline, ]
    list_display = ('name', 'count_of_categories')
    search_fields = ('name', 'count_of_categories')

    def count_of_categories(self, obj):
        return Category.objects.get(group=obj).count()


admin.site.register(Group, GroupAdmin)


class MembershipAdmin(admin.ModelAdmin):
    fields = ('group', 'user', 'role')
    list_display = ('group', 'user', 'role')
    search_fields = ('group', 'user', 'role')
    list_filter = ('role')


admin.site.register(Membership, MembershipAdmin)


class QuestionSetAdmin(admin.ModelAdmin):
    fieldsests = (
        ('Information', {'fields': ('name', 'author', 'public')}),
        ('Questions', {'fields': ('question')}),
    )
    list_display = ('name', 'author', 'public')
    list_editable = ('public', )
    list_filter = ('public', )
    search_fields = ('name', 'author')


admin.site.register(SetOfQuestions, SetOfQuestionsAdmin)


class AnswerAdmin(admin.ModelAdmin):
    fields = ('content', 'true', 'question')
    list_display = ('content', 'true')
    list_filter = ('true', )

admin.site.register(Answer, AnswerAdmin)


class QuestionAdmin(admin.ModelAdmin):
    fields = ('content', )
    list_display = ('content', 'count_of_answer')
    list_filter = ('count_of_answer')

    def count_of_answer(self, obj):
        return Answer.objects.get(question=obj).count()


admin.site.register(Question, QuestionAdmin)


class UserInfoAdmin(models.ModelAdmin):
    fields = ('user', 'date_of_creation', 'verified')
    list_filter = ('verified', )
    list_display = ('user', 'date_of_creation', 'verified')
    search_fields = ('user', 'date_of_creation')


admin.site.register(UserInfo,UserInfoAdmin)


admin.site.register(Copy)
