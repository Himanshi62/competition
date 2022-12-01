from django.db import models

# Create your models here.


class Submission(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    colgName = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    mobileNo = models.IntegerField()
    # mail = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    year = models.CharField(max_length=200)
    roll_no = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return (
            f"{self.name} | "
            f"{self.email} "
        )
