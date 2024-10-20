from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

def translit_to_eng(s: str) -> str:
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}
 
    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))


class ModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=Trainer.Status.ACTIVATED)





class CardAbout(models.Model):
    
    slug = models.SlugField(unique=True,max_length=255,db_index=True,verbose_name='URL')
    image = models.ImageField(upload_to="images/",verbose_name='Картинка карточки')
    title = models.CharField(max_length=255,verbose_name='Заголовок')
    description = models.TextField(blank=True,verbose_name='Описание')
    start_time = models.TimeField(auto_now_add=True,null=True)
    end_time = models.TimeField(auto_now_add=True,null=True)
    trainer_classes = models.ForeignKey('Trainer',on_delete=models.PROTECT,null=True,verbose_name='Тренер')
    membership_type_allow = models.ForeignKey('Membership',on_delete=models.PROTECT,null=True,verbose_name='Абонемент для занятия')
    area_of_text = models.TextField(blank=True,verbose_name='Описание-на сайте')
    
    
    
    
    
    def get_absolute_url(self):
        return reverse("card__about", kwargs={"card__about__slug": self.slug})
    
    def save(self,*args,**kwargs):
        self.slug = slugify(translit_to_eng(self.title))
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['slug']
        
        
        indexes = [
            models.Index(fields=['slug'])
        ]
        
        verbose_name = 'Карточку'
        verbose_name_plural = 'Карточки'
        
        
        
        
        
class Members(models.Model):    
        
    first_name = models.CharField(max_length=255,verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    email = models.EmailField(blank=False,unique=True,verbose_name='Почта')
    phone = models.IntegerField(blank=False,unique=True,verbose_name='Телефон')
    membership_type = models.ForeignKey('Membership',on_delete=models.PROTECT,null=True,verbose_name='Тип абонемента')
    membership_start_date = models.DateTimeField(auto_now_add=True,verbose_name='Присоединился(ась)')
    membership_end_date = models.DateTimeField(auto_now_add=True,verbose_name='Дата окончания')
    profile_photo = models.ImageField(upload_to="images/",verbose_name='Фото-профиля',blank=True)
    is_active = models.BooleanField(default=True,verbose_name='Активно')
    trainer = models.ForeignKey('Trainer',models.PROTECT,null=True,verbose_name='Прикрепленный тренер')
     
    
    def __str__(self):
        return self.last_name
    
    class Meta:
        ordering = ['first_name']
        indexes = [
            models.Index(fields=['first_name'])
        ]
        verbose_name = 'Человекa'
        verbose_name_plural = 'Людей'
        
        
        
        
class Membership(models.Model):
    
    slug = models.SlugField(unique=True,max_length=255,db_index=True,verbose_name='URL-Абонемента')
    name= models.CharField(max_length=100,db_index=True,verbose_name='Название абонемента')
    membership_photo = models.ImageField(upload_to="images/",verbose_name='Фото-абонемента')
    price = models.IntegerField(blank=False,unique=True,verbose_name='Цена')
    desc_membership = models.TextField(max_length=255,unique=True,blank=True,verbose_name='Описание абонемента')
    about_membership = models.TextField(max_length=559,blank=True,verbose_name='О абонементе') 
    
    
    def get_absolute_url(self):
        return reverse('membership', kwargs={'membership__slug': self.slug})



    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'
        ordering = ['id','name']
        
        
        
        
class Trainer(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Не тренерует'
        ACTIVATED = 1, 'Тренерует'
        
        
        
        
        
    
    first_name = models.CharField(max_length=255,verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    email = models.EmailField(blank=False,unique=True,verbose_name='Почта')
    phone = models.IntegerField(blank=False,unique=True,verbose_name='Телефон')
    profile_photo = models.ImageField(upload_to="images/",verbose_name='Фото-профиля')
    slug = models.SlugField(unique=True,max_length=255,db_index=True,verbose_name='URL-trainer')
    classes_type = models.ForeignKey('CardAbout',on_delete=models.DO_NOTHING,null=True,verbose_name='Занятия')
    is_active = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]),x[1]),Status.choices)), default=Status.DRAFT,verbose_name='Тренeрует?')
    
    objects = models.Manager()
    act = ModelManager()
    
    
    
    
    
    
    
    
    
    def get_absolute_url(self):
        return reverse('trainer', kwargs={'trainer__slug': self.slug})
    
    
    def __str__(self):
        return self.last_name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(translit_to_eng(self.last_name))
        super().save(*args,**kwargs)
    
    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренера'
        ordering = ['id','first_name']
        
        indexes = [
            models.Index(fields=['first_name'])
        ]
        
    
    

        
        
    