from django.contrib.humanize.templatetags import humanize
from django.db import models, transaction
# Create your models here.


class Pocket(models.Model):
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_one = models.DateField()
    date_two = models.DateField()
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def initial_amount(self):
        return humanize.intcomma(self.amount + self.spend())

    def spend(self):
        return sum([
           s.amount for s in CurentSpend.objects.filter(pocket=self)
        ])

    def humanize_amount(self):
        return humanize.intcomma(self.amount)

    def spend_humanize(self):
        return humanize.intcomma(self.spend())


class CurentSpend(models.Model):
    description = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    register = models.DateTimeField(auto_now_add=True)
    pocket = models.ForeignKey(
        Pocket,
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.discount_pocket()
        super().save(*args, **kwargs)

    @transaction.atomic
    def discount_pocket(self):
        self.pocket.amount -= self.amount
        self.pocket.save()
