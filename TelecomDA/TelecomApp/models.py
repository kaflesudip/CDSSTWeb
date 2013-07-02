from django.db import models


class HomeSlider(models.Model):
    """Slider to show in homepage"""
    slider_header = models.CharField(max_length=500, blank=True)
    slider_image = models.ImageField(upload_to=".",
                                     null=True, blank=True)
    slider_description = models.TextField(max_length=500, blank=True)

    def __unicode__(self):
        return self.slider_header


class HomeContent(models.Model):
    """The homepage of our project"""
    mid_content_header = models.CharField(max_length=500, blank=True)
    mid_content_image = models.ImageField(upload_to=".",
                                          null=True, blank=True)
    mid_content_description = models.TextField(max_length=500, blank=True)

    def __unicode__(self):
        return self.mid_content_header


class HomeDetails(models.Model):
    """The homepage of our project"""
    mid_content_header = models.CharField(max_length=500, blank=True)
    mid_content_image = models.ImageField(upload_to=".",
                                          null=True, blank=True)
    mid_content_description = models.TextField(max_length=5000, blank=True)

    def __unicode__(self):
        return self.mid_content_header


class Overview(models.Model):
    """Overview page for our project"""
    title = models.CharField(max_length=500, blank=True)
    content = models.TextField(max_length=5000, blank=True)
    #abstract = models.TextField(max_length=5000, blank=True)
    #introduction = models.TextField(max_length=5000, blank=True)
    #objective = models.TextField(max_length=5000, blank=True)
    #scope = models.TextField(max_length=5000, blank=True)
    #problem_statement = models.TextField(max_length=5000, blank=True)
    #proposed_solution = models.TextField(max_length=5000, blank=True)
    #methodology = models.TextField(max_length=5000, blank=True)
    #tools = models.TextField(max_length=5000, blank=True)
    #schedule = models.TextField(max_length=5000, blank=True)
    #cost = models.TextField(max_length=5000, blank=True)

    def __unicode__(self):
        return self.title


class Screenshot(models.Model):
    """Screenshots of our output"""
    screenshot_header = models.CharField(max_length=500, blank=True)
    screenshot_description = models.TextField(max_length=5000, blank=True)
    screenshot_image = models.ImageField(upload_to=".", null=True,
                                         blank=True)

    def __unicode__(self):
        return self.screenshot_header


class Tool(models.Model):
    """The homepage of our project"""
    tool_header = models.CharField(max_length=500, blank=True)
    tool_image = models.ImageField(upload_to=".",
                                   null=True, blank=True)
    tool_description = models.TextField(max_length=500, blank=True)

    def __unicode__(self):
        return self.tool_header


class Team(models.Model):
    """Model for representing team description"""
    name = models.CharField(max_length=500, blank=True)
    Institute = models.CharField(max_length=500, blank=True)
    roll_no = models.CharField(max_length=500, blank=True)
    email = models.EmailField(max_length=500, blank=True)
    image = models.ImageField(upload_to=".", null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.name
