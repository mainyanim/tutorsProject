from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class Subject(models.Model):
    """
    Model representing a subject (e.g. Math, Chemisty etc.).
    """

    name = models.CharField(max_length=200, help_text="Enter a subject you want to teach (e.g. Math, Biology, Computer Science etc.)")
    #tutor = models.ManyToManyField('Tutor', related_name='tutor_type',help_text="Select a subject")

    def get_absolute_url(self):
        """
        Returns the url to access a particular subject instance.
        """
        return reverse('accounts:subject-detail', args=[str(self.pk)])

    def __unicode__(self):
        return self.name

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    image = models.ImageField(upload_to='profile_image', default='profile_image/mystery-person-graphic.jpg', blank=True)
    title =  models.CharField(max_length=100, default = 'Hello World!')
    first_name = models.CharField(max_length=200, default = '')
    last_name = models.CharField(max_length=200, default = '')
    subject = models.ManyToManyField('Subject', related_name='tutor_type', default = '', help_text="Select a subject")
    AREA_STATUS = (
        ('Jerusalem', 'Jerusalem'),
        ('Tel Aviv', 'Tel Aviv'),
        ('Haifa', 'Haifa'),
        ('Eilat', 'Eilat')
    )
    area = models.CharField(max_length=200, choices=AREA_STATUS, blank=True, default='', help_text='Tutor area')
      # Foreign Key used because tutor can only have one area, but area can have multiple tutors
      # Author as a string rather than object because it hasn't been declared yet in file.
    description = models.TextField(max_length=4000, help_text="Enter a brief description about yourself")
    charge = models.IntegerField(default = '0')
      # ManyToManyField used because Subject can contain many tutors. Tutors can cover many subjects.
      # Subject declared as an object because it has already been defined.
    LANGUAGE_CHOICES = (
        ('English','English'),
        ('Hebrew','Hebrew'),
        ('Russian','Russian'),
        ('French','French'),
        ('Arabic','Arabic'),
    )
    language = models.CharField('Language', choices = LANGUAGE_CHOICES, max_length=50, null=True)

    def __str__(self):
        return self.user.username

    def display_subject(self):
        """
        Creates a string for the subject. This is required to display subject in Admin.
        """
        return ', '.join([ subject.name for subject in self.subject.all()[:3] ])
        display_subject.short_description = 'Subject'

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender = User)


class Language(models.Model):
    """
    Model representing a Language (e.g. English, French, Japanese, etc.)
    """
    name = models.CharField(max_length=200, help_text="Enter a language you speak (e.g. English, French, Hebrew etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
