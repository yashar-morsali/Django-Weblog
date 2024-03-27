from django.db import models 
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=150) 
    main = models.BooleanField()
    parent = models.ForeignKey('self' , on_delete=models.CASCADE , null=True , blank=True , related_name='children')

    class Meta:
        verbose_name = "Caregories"
        
    def __str__(self):
        if self.parent :
            return f"{self.name}   -> {self.parent.name}"
        else :
             return f'{self.name}'


class Comment(models.Model):
    name = models.CharField(max_length=50 , null=True , blank=True)
    #user =models.ForeignKey(User , on_delete=models.CASCADE , null=False , blank=False)
    email = models.EmailField(null=True , blank=True) 
    content = models.CharField(max_length=300)
    post = models.ForeignKey('Post' , on_delete=models.CASCADE , null=False , blank=False , related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comments"
        ordering = ['id','created_at']

    def __str__(self):
        return f"id:{self.id} | post:{self.post.title} | {self.content}"

class Post(models.Model):

    author = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank=True ,related_name="posts")
    title = models.CharField(max_length=100)
    intro = models.CharField( max_length=200)
    image = models.ImageField(upload_to='Posts/posts_main_image')
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE , null=False , blank=False )
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"title:{self.title} | created time:{self.created_at}"


    



#Done connect category to posts and back 
#Done connect comments on post 
#(no need) create a custome user 


#(Done) how to find post comments / find posts by category / 