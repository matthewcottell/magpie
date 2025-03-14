from django.db import models


from django.contrib.auth.models import User

# Option 1: Create a profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Add custom fields here

    def __str__(self):
        return f"Profile for {self.user.username}"

# OR Option 2: Custom user model (requires settings.AUTH_USER_MODEL)
# from django.contrib.auth.models import AbstractUser
# class User(AbstractUser):
#     # Add custom fields here
#     pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username}"

    class Meta:
        ordering = ["-created_at"]  # To order posts by creation time


class Friendship(models.Model):
    user = models.ForeignKey(User, related_name="friend", on_delete=models.CASCADE)
    friend = models.ForeignKey(
        User, related_name="friends_with", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
