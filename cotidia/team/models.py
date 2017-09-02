from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, null=True)
    role = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    active = models.BooleanField(default=True)

    photo = models.ImageField(upload_to='team', max_length=100, blank=True)

    order_id = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        ordering = ('order_id',)

    def __str__(self):
        return self.name()

    def name(self):
        return "{} {}".format(self.first_name, self.last_name)


class MemberSocial(models.Model):
    SOCIAL_NETWORKS = (
        ('LINKEDIN', 'LinkedIn'),
        ('TWITTER', 'Twitter'),
        ('FACEBOOK', 'Facebook'),
        ('INSTAGRAM', 'Instagram'),
        ('BEHANCE', 'Behance'),
    )
    member = models.ForeignKey("team.Member")
    network = models.CharField(max_length=50, choices=SOCIAL_NETWORKS)
    url = models.URLField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} [{}]".format(self.network_label, self.url)

    def network_label(self):
        return dict(self.SOCIAL_NETWORKS).get(self.network)

