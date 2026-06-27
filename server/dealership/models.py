from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.car_make.name} {self.name}"

class Dealer(models.Model):
    full_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)   # store full state name, e.g., "Kansas"
    address = models.TextField()
    zip = models.CharField(max_length=10)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    short_name = models.CharField(max_length=50)
    def __str__(self):
        return self.full_name

class Review(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    review_text = models.TextField()
    sentiment = models.CharField(max_length=20, blank=True)
    purchase = models.BooleanField(default=False)
    purchase_date = models.DateField(null=True, blank=True)
    car_make = models.ForeignKey(CarMake, null=True, blank=True, on_delete=models.SET_NULL)
    car_model = models.ForeignKey(CarModel, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Review for {self.dealer.full_name} by {self.user.username}"