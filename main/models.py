from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=150, default='')  # кратко для главной
    description = models.TextField()
    price_from = models.IntegerField()
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome класс, например 'fas fa-code'")

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    service_type = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Request(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"Заявка от {self.name}"
