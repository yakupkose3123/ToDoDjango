from django.db import models

class TODO(models.Model):

    PRIORITY_OPTIONS = [
        ("UI", "URGENT / IMPORTANT"),
        ("UN", "URGENT / NOT-IMPORTANT"),
        ("NI", "NOT-URGENT / IMPORTANT"),
        ("NN", "NOT-URGENT / NOT-IMPORTANT"),
    ]

    title = models.CharField(max_length=60)
    discription = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=3, choices = PRIORITY_OPTIONS,default="UI")
    isCompleted = models.BooleanField(default="false")
    # create_date =models.DateTimeField()
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return (f"{self.title} - {self.priority} - {self.isCompleted}")

    class Meta:
        verbose_name_plural = "TODOS"