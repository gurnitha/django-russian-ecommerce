# apps/home/models.py

# Django modules
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.forms import ModelForm, TextInput, Textarea

# Django locals

# Create your models here.


# Setting
class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# ContactMessage
class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name= models.CharField(blank=True,max_length=20)
    email= models.CharField(blank=True,max_length=50)
    subject= models.CharField(blank=True,max_length=50)
    message= models.TextField(blank=True,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ContactForm
class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
       # The fields and widgets bellow are based on the contact form fields
        fields = ['name', 'email', 'subject','message']
        widgets = {
            'name'    : TextInput(attrs={'class': 'input','placeholder':'Name & Surname'}),
            'subject' : TextInput(attrs={'class': 'input','placeholder':'Subject'}),
            'email'   : TextInput(attrs={'class': 'input','placeholder':'Email Address'}),
            'message' : Textarea(attrs={'class': 'input','placeholder':'Your Message','rows':'5'}),
        }


        """ 
        --------- By adding {{ form.as_p }} in the contactus page
        THE ContactMessage & ContactForm will create form as seen bellow :-------

        <p>
            <label for="id_name">Name:</label> 
            <input type="text" name="name" class="input" placeholder="Name &amp; Surname" maxlength="20" id="id_name">
        </p>
        <p>
            <label for="id_email">Email:</label> 
            <input type="text" name="email" class="input" placeholder="Email Address" maxlength="50" id="id_email">
        </p>
        <p>
            <label for="id_subject">Subject:</label> 
            <input type="text" name="subject" class="input" placeholder="Subject" maxlength="50" id="id_subject">
        </p>
        <p>
            <label for="id_message">Message:</label> 
            <textarea name="message" cols="40" rows="5" class="input" placeholder="Your Message" maxlength="255" id="id_message"></textarea>
        </p>
        """        