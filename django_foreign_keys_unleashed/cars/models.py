from django.db import models
from django.db.models import Q
from django.conf import settings
from django.contrib.auth import get_user_model


User = settings.AUTH_USER_MODEL  # 'auth.User'


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     city = models.CharField(max_length=120)
#     image = models.ImageField()

# class CompanyProfile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     city = models.CharField(max_length=120)
#     image = models.ImageField()

# user_obj = User.objects.first()
# user_obj.companyprofile_set.all()


def set_delete_user():
    User = get_user_model()
    return User.objects.get_or_create(username='deleted')[0]  # get_or_create -> ( obj, True )


def limit_user_choices():
    return Q(username_icontains='e') | Q(username_icontains='c')
    # return {'is_staff': True}


class Car(models.Model):
    user = models.ForeignKey(
        User,
        # related_name='car_set',  # default related_name
        on_delete=models.SET(set_delete_user),
        # limit_choices_to={'is_staff': True}
        limit_choices_to=limit_user_choices
    )
    updated_by = models.ForeignKey(User, related_name='updated_car_user', null=True, blank=True)
    # drivers = models.ManyToManyField(User)
    # first_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    # passengers = models.ManyToManyField(User)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


# ManyToManyField
# car_1 = Car.objects.first()
# cfe = car_1.first_owner
# User = cfe.__class__
# first_user = User.objects.first()
# first_user.car


# ManyToManyField
# car_1 = Car.objects.first()
# user_qs = car_1.drivers.all()  # returns queryset of users
# cfe = user_qs.first()
# cfe.car_set.all()
# Car.objects.filter(drivers=cfe)
# Car.objects.filter(drivers__in=user_qs)


# ManyToOneField(), A user can have many cars, but A car only belongs to one user.
# car_obj = Car.objects.first()
# User = car_obj.user.__class__
# micro = User.objects.all().last()  # filter querysets
# micro_cars = micro.car_set.all()
# micro_cars_qs = Car.objects.filter(user=micro)
