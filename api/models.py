from users.models import CustomUser

from django.db import models

# Create your models here.


class UserDetail(models.Model):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    Completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.Name

# follow - user id ,follower id
# user content - userid , content , followerid


list_status = (('active', 'active'),
               ('inactive', 'inactive')
               )


class UserShare(models.Model):
    Share_Owner = models.ForeignKey(
        CustomUser, null=True, on_delete=models.CASCADE)
    Share_Name = models.CharField(max_length=100)
    
    Share_Count = models.IntegerField()
    Share_Price = models.FloatField()
    Status = models.CharField(max_length=50, choices=list_status)

    def __str__(self):
        return f'{self.Share_Name}{self.Share_Owner}'


class UserTransaction(models.Model):
    Seller_ID = models.IntegerField()
    User_ID = models.ForeignKey(
        CustomUser, null=True, on_delete=models.CASCADE)
    Share_ID = models.ForeignKey(
        UserShare, null=True, on_delete=models.CASCADE)
    Share_Count = models.IntegerField()
    Date_time = models.DateField(auto_now_add=True)
    Amount = models.IntegerField()


class UserWallet(models.Model):
    User_ID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Amount = models.IntegerField()


action = (('Follow', 'Follow'),
          ('Unfollow', 'Unfollow'))


class Userfollow(models.Model):
    UserID = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,  related_name='UserID')
    Followerid = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='Followerid')
    Action = models.CharField(max_length=100, choices=action)


class UserContent(models.Model):
    Userid = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='Userid')
    FollowerID = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='FollowerID')
    Content = models.CharField(max_length=100)
