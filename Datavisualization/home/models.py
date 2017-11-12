from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 1. Case Title (Eg. Facebook Vs. Tesla)
# 2. Case ID (Unique Identifier)
# 3. Mentioned in (Cases where self-case has been mentioned)
# 4. Mentions (Cases that are mentioned in self-case)
# 5. Body (Text)
# 6. Date of Judgement (Date)


class Case(models.Model):
	id = models.AutoField(primary_key = True)
	title = models.CharField(max_length=2000, default=None, null=False,blank=False)
	case_ref_no = models.CharField(max_length=200, default=None, null=False,blank=False)
	mentioned_in = models.IntegerField(default=0,help_text="No of times the case is mentioned in other cases")
	mentions = models.ManyToManyField("self", blank=True)
	body = models.TextField(help_text="About the Case")
	doj = models.DateField(auto_now=False, auto_now_add=False)


	def __str__(self):
		return str(self.case_ref_no)

	def __unicode__(self):
		return str(self.case_ref_no)


