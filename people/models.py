from django.db import models

# Create your models here.
class Person(models.Model):
	good_id = models.BigIntegerField(primary_key=True)
	su_name = models.TextField()
	group = models.TextField()
	prep = models.TextField()
	level = models.TextField()
	type = models.TextField()
	sort_order = models.BigIntegerField()

	class Meta:
			managed = False
			db_table = 'core_prep_variants'
			db_table_comment = 'core'