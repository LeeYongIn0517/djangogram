from django.db import models
from djangogram.users import models as user_model
# Create your models here.
class TimeStamedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    #추상적인 모델임을 선언, 상속만 가능
    class Meta:
        abstract = True

class Post(TimeStamedModel):
    author = models.ForeignKey(
            user_model.User, #외래키
            null=True, #필드 값이 NULL로 저장되는 것 허용
            on_delete=models.CASCADE, #계정 삭제시 해당 정보도 삭제
            related_name='post_author' #특정 사용자가 작성한 질문을 얻을 때 사용, ex)some_user.post_author.all()
            )
    image = models.ImageField(blank=False)
    caption = models.TextField(blank=False)
    image_likes = models.ManyToManyField(
            user_model.User,
            blank=True,
            related_name='post_images_likes'
        )

    def __str__(self):
        return f"{self.author}: {self.caption}"

class Comment(TimeStamedModel):
    author = models.ForeignKey(
            user_model.User,
            null=True,
            on_delete=models.CASCADE, #계정 삭제시 해당 정보도 삭제
            related_name='comment_author' #특정 사용자가 작성한 질문을 얻을 때 사용, ex)some_user.post_author.all()
            )
    posts = models.ForeignKey(
            Post,
            null=True,
            on_delete=models.CASCADE, #계정 삭제시 해당 정보도 삭제
            related_name='comment_post' #특정 사용자가 작성한 질문을 얻을 때 사용, ex)some_user.post_author.all()
            )
    contents = models.TextField(blank=True)

    def __str__(self):
        return f"{self.author}: {self.contents}"
