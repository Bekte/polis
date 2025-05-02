from django.db import models




class NavigBar(models.Model):
    title = models.CharField(max_length=100)
    icon_class = models.FileField(upload_to='icon_hw/',blank=True, null=True)


    def __str__(self):
        return self.title
    



# Create your models here.
class Main(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    description2 = models.CharField(max_length=150, null=True)
    sub_description = models.TextField()
    photo = models.ImageField(upload_to='static/images/', verbose_name='фото для об фона', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Главное'
        verbose_name_plural = 'Главные'


class About(models.Model):
    about = models.CharField(max_length=50, blank=True)
    more = models.CharField(max_length=200)
    def __str__(self):
        return self.about

class AboutPro(models.Model):
    ambitious = models.CharField(max_length=100)
    ambitious_description = models.TextField()
    photo = models.ImageField(upload_to='static/images/', verbose_name='фото для об фона', blank=True)

    def __str__(self):
        return self.ambitious

class AboutProPhoto(models.Model):
    picture_description = models.CharField(max_length=150, blank=True)
    year_of_experience = models.IntegerField(null=True)
    photo = models.ImageField(upload_to='static/images/', verbose_name='фото для об фона', blank=True)


    def __str__(self):
        return self.picture_description
    
class AboutPhoto(models.Model):
    about_about = models.CharField(max_length=100, default='Имя по умолчанию')
    about_experts = models.CharField(max_length=100, default='Имя по умолчанию')
    about_experts_description = models.TextField()

    def __str__(self):
        return self.about_about
    
class AboutExperts(models.Model):  
    experts = models.CharField(150)
    experts_description = models.TextField()
    photo_experts = models.ImageField(upload_to='static/images/', verbose_name='фото для об экспертов')
    def __str__(self):
        return self.experts

class ParticipantNumbers (models.Model):  
    participant_numbers = models.IntegerField()
    title = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Участников: {self.participant_numbers}"

    
class HelpMarketing(models.Model):
    title = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.title
    

class PictureMarketing(models.Model):
    title = models.CharField(max_length=200)
    icon_class = models.CharField(max_length=100)

    def __str__(self):
        return f"Участников: {self.title}"


class MarketingHead(models.Model):
    marketing_strategy = models.CharField(50)
    elements_of_marketing = models.CharField(250)

class MarketingBox(models.Model):
    head_marketing = models.CharField(max_length=50)
    head_marketing_description = models.CharField(max_length=150)
    head_marketing_subdescription = models.CharField(max_length=200)
    head_marketing_text = models.TextField()
    evaluation_of_company = models.CharField(50)

    

    def __str__(self):
        return self.head_marketing
    
    class Meta:
        verbose_name = 'Маркетинг'
        verbose_name_plural = 'Маркетинги'


class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
        
class ServiceList(models.Model):
    title = models.CharField(max_length=200)
    icon_class = models.FileField(upload_to='icon_hw',blank=True, null=True)
    description = models.TextField()
    


    def __str__(self):
        return self.title

class ReviewPhrases(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title  
    
class ReviewList(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    description = models.TextField()
    photo_experts = models.ImageField(upload_to='static/images/', verbose_name='фото сотрудника')
    

    def __str__(self):
        return self.full_name 
    


class Goods(models.Model):
    title = models.CharField(max_length=100) 
    our_title = models.CharField(max_length=100) 

    def __str__(self):
        return self.title

class GoodsPicture(models.Model):
    photo_goods = models.ImageField(upload_to='static/images/', verbose_name='фото сотрудника')
    title = models.CharField(max_length=100) 
    price = models.CharField(max_length=100) 
    def __str__(self):
        return self.title

    


class Blog(models.Model):
    title = models.CharField(max_length=100)
    title_description = models.CharField(max_length=100)

class BlogPicture(models.Model):
    photo_blog = models.ImageField(upload_to='static/images/', verbose_name='фото сотрудника')
    date_time = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    blog_description = models.TextField()

    def __str__(self):
        return self.title


class Adresses(models.Model):
    icon_class = models.FileField(upload_to='icon_hw',blank=True, null=True)
    title = models.CharField(max_length=100)
    more = models.CharField(max_length=100)
    contact_address = models.CharField(max_length=100)

    def __str__(self):
        return self.title






class Registartion(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    surname = models.CharField(max_length=200, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='адрес', unique=True)
    about_you = models.TextField(verbose_name='О вас')
    
    def __str__(self):
        return self.name


    