from django.db import models

# Create your models here.

class UserInput(models.Model) :
    text_input = models.CharField(max_length=200)
    counter = models.IntegerField(default=5)

    def __str__(self) :
        return self.text_input  

# class orderTable(models.Model) :
#     # id = models.IntegerField(primary_key=True)
#     productName = models.CharField(max_length=200)
#     productCount = models.IntegerField(default=1)
#     testInt = models.IntegerField(default=5)

#     def __str__(self) :
#         return self.productName



# class order(models.Model) :
#     order_name = models.CharField(max_length=200)
#     order_count = models.IntegerField(default=0)

# class Choice(models.Model) :
#     question = models.ForeignKey(Question,on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

