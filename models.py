from django.db import models

class Achievement(models.Model):
    title = models.CharField(max_length=256, help_text="Use a clever title. I hear who ever creates the best achievement gets an achievement.")
    slug = models.SlugField()
    description = models.TextField(help_text="Explain how to obtain this achievement.")
    image = models.ImageField(blank=True, null=True, upload_to="pics/", help_text="I can has awesome pic?")


    points = models.IntegerField(help_text="How much is this worth? Give more points for behavior we want to encourage.")
    xp = models.IntegerField()

    creation_date = models.DateTimeField(auto_now=True)
    avalible_until = models.DateTimeField(blank=True, null=True, help_text="Not Required")
    

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/achievements/%s/' % self.slug

    class Meta:
        ordering = ["title"]
