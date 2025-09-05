from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.name} - {self.email}"

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('individual therapy', 'Individual Therapy'),
        ('couples therapy', 'Couples Therapy'),
        ('corporate therapy', 'Corporate Therapy'),
        ('stress therapy', 'Stress Therapy'),
        ('depression therapy', 'Depression Therapy'),
        ('anxiety therapy', 'Anxiety Therapy')
    ]

    SESSION_CHOICES = [
        ('virtual', 'Virtual Session'),
        ('in_person', 'In-person Session'),
        ('group', 'Group Session'),
    ]
    
    name = models.CharField(max_length=100)
    email = models. EmailField()
    phone = models.PositiveIntegerField()
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES, blank=True)
    date = models.DateField()
    time = models.TimeField()
    session = models.CharField(max_length=100, choices=SESSION_CHOICES, blank=True)
    notes = models.TextField()


def __str__(self):
        return f"{self.name} - {self.service} on {self.date}"
