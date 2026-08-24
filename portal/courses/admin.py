from django.contrib import admin
from .models import Department,Course,Student,Enrollment

# Register your models here.
# Method 1: Basic registration
admin.site.register(Department)
# Method 2: Customization using ModelAdmin
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('code', 'title', 'department', 'credits') # Columns shown in table
    list_filter =('department', 'credits') # Right sidebar filter
    search_fields= ('code', 'title') # Search box fields
    ordering=('code',) # Default sorting

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display=('student', 'course', 'enrolled_at', 'grade')
    list_filter =('grade', 'course')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('student_id', 'first_name', 'last_name', 'year_level')
    search_fields= ('student_id', 'first_name', 'last_name')
    list_filter =('year_level',)
    # Organize fields into sections
    fieldsets=(
        ('ข้อมูลประจําตัว',{
            'fields': ('student_id',('first_name', 'last_name'))
        }),
        ('สถานะการศึกษา',{
            'fields': ('year_level',),
            'classes':('collapse',), # Collapsible section
        }),
    )