from django.db import models

class Design(models.Model):
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    fabric = models.CharField(max_length=100)
    description = models.TextField()
    colour = models.CharField(max_length=50)
    size = models.PositiveBigIntegerField()
    print = models.BooleanField()
    image = models.CharField(max_length=300)
    design_drawing = models.CharField(max_length=300, blank=True)
    season = models.CharField(max_length=50)
    center_back_length = models.PositiveBigIntegerField(blank=True, null=True)
    center_front_length = models.PositiveBigIntegerField(blank=True, null=True)
    sleeve_length = models.PositiveBigIntegerField(blank=True, null=True)
    hem_length = models.PositiveBigIntegerField(blank=True, null=True)
    chest = models.PositiveBigIntegerField(blank=True, null=True)
    waist = models.PositiveBigIntegerField(blank=True, null=True)
    inside_leg_length = models.PositiveBigIntegerField(blank=True, null=True)
    outside_leg_length = models.PositiveBigIntegerField(blank=True, null=True)
    saved_by = models.ManyToManyField(
        'jwt_auth.User',
        related_name='saved_designs',
        blank='True'
    )

    added_by = models.ForeignKey(
        'jwt_auth.User',
        related_name='added_designs',
        on_delete=models.DO_NOTHING,
        blank=True
    )


    def __str__(self):
        return f'{self.name}'

class Comment(models.Model):
    text = models.TextField()
    rating = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    design = models.ForeignKey(
        Design,
        related_name='comments',
        on_delete=models.CASCADE
    )

    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='comments_made',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.design} : {self.id}'