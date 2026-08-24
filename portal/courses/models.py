from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        # Human-readable string representation
        return f"{self.name} ({self.code})"

class Student(models.Model):
    class YearLevel(models.TextChoices):
        FRESHMAN = 'FR', 'Freshman (ปี 1)'
        SOPHOMORE = 'SO', 'Sophomore (ปี 2)'
        JUNIOR = 'JR', 'Junior (ปี 3)'
        SENIOR = 'SR', 'Senior (ปี 4)'
    student_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year_level = models.CharField(
        max_length=2,
        choices=YearLevel.choices,
        default=YearLevel.JUNIOR
    )
    
class Course(models.Model):
    # Field Definitions (Attributes map to database columns)
    code=models.CharField(max_length=10,unique=True,verbose_name="รหัสวิชา")
    title = models.CharField(max_length=100,verbose_name="ชื ่อวิชา")
    description =models.TextField(blank=True,verbose_name="คําอธิบายรายวิชา")
    credits = models.PositiveSmallIntegerField(default=3, verbose_name="หน่วยกิต")
    is_active=models.BooleanField(default=True,verbose_name="เปิดสอน")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    students = models.ManyToManyField(Student, through='Enrollment')

    class Meta:
        db_table= "custom_course_table" # Custom table name in SQL
        verbose_name = "รายวิชา" # Singular name in Admin
        verbose_name_plural= "รายวิชาทั ้งหมด" # Plural name in Admin
        ordering=['code'] # Default sorting by code ascending
        indexes = [
            # Index for single column
            models.Index(fields=['title'], name='course_title_idx'),
            # Composite Index for multi-column search
            models.Index(fields=['is_active', 'code'], name='course_active_code_idx'),
        ]
    department=models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='courses' # Used for reverse lookup
    )

    def __str__(self):
        return f"{self.code}-{self.title}"
    
class StudentProfile(models.Model):
    # 1:1 link with Django built-in User model
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='student_profile')
    student=models.OneToOneField(Student,on_delete=models.CASCADE,related_name='profile')
    student_id1=models.CharField(max_length=10,unique=True)
    phone_number=models.CharField(max_length=15,blank=True)
    advisor_name=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return f"{self.student_id} ({self.user.username})"
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=2, blank=True, default='')
    class Meta:
        unique_together = ('student', 'course') # Prevent duplicate enrollment