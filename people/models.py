from django.db import models
from datetime import datetime

class People(models.Model):
    iin = models.CharField (max_length=12, primary_key=True)
    age = models.IntegerField ()

    def save(self, *args, **kwargs):
        if self.iin[6] in ['1', '2']:
            bday = f'18{self.iin[0:6:1]}'
        if self.iin[6] in ['3', '4']:
            bday = f'19{self.iin[0:6:1]}'
        if self.iin[6] in ['5', '6']:
            bday = f'20{self.iin[0:6:1]}'
        age = (datetime.today() - datetime.strptime(bday, '%Y%m%d')).days // 365
        self.age = age
        super().save(*args, **kwargs)