from django.db import models

class Expense(models.Model) :
    name = models.CharField(max_length=255)
    amount = models.IntegerField() 
    category = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)


    
