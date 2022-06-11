from django.db import models

class Todo(models.Model):

    PRIORITY_OPTIONS = [
        ("1", "HIGH"),
        ("2", "MEDIUM"),
        ("3", "LOW"),
       
    ]

    title = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=3, choices = PRIORITY_OPTIONS,default="UI")
    isCompleted = models.BooleanField()
    create_date =models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return (f"{self.title} - {self.priority} - {self.isCompleted}")

    class Meta:
        verbose_name_plural = "TODOS"





# from django.db import models

# class Student(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)

#     email = models.EmailField(max_length=154, unique=True, blank=True, null=True)
#     phone = models.CharField(max_length=50, unique=True, blank=True, null=True)

#     GENDER =(
#         ("1", "Female"),
#         ("2", "Male"),
#         ("3", "Other"),
#         ("4", "Prefer Not Say"),
#     )

#     gender = models.CharField(max_length=50, choices=GENDER)
#     number = models.IntegerField(blank=True, null=True)
#     image = models.ImageField(upload_to="student/", default="avatar.png")

#     def __str__(self):
#         return f"{self.number} {self.first_name} {self.last_name}"
