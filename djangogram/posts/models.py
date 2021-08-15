from django.db import models
from djangogram.users import models as user_model
# Create your models here.
class TimeStamedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    #This model will then not be used to create any database table. 
    # Instead, when it is used as a base class for other models, 
    # its fields will be added to those of the child class.
    class Meta:
        abstract = True

class Post(TimeStamedModel):
    author = models.ForeignKey(
            user_model.User, #외래키
            null=True, #필드 값이 NULL로 저장되는 것 허용
            on_delete=models.CASCADE, #계정 삭제시 해당 정보도 삭제
            related_name='post_author' #특정 사용자가 작성한 질문을 얻을 때 사용, ex)some_user.post_author.all()                                       
            )
    image = models.ImageField(blank=True)
    caption = models.TextField(blank=True)
    image_likes = models.ManyToManyField(user_model.User, related_name='post_images_likes')

class Comment(TimeStamedModel):
    author = models.ForeignKey(
            user_model.User,
            null=True,
            on_delete=models.CASCADE, #계정 삭제시 해당 정보도 삭제
            related_name='post_author' #특정 사용자가 작성한 질문을 얻을 때 사용, ex)some_user.post_author.all()                                       
            )
    posts = models.ForeignKey(
            Post,
            null=True,
            on_delete=models.CASCADE, #계정 삭제시 해당 정보도 삭제
            related_name='comment_post' #특정 사용자가 작성한 질문을 얻을 때 사용, ex)some_user.post_author.all()                                       
            )
    contents = models.TextField(blank=True)
