from django.db import models
from django.contrib.auth.models import User, UserManager

## Subscriber Section - Organization is parent of all models ##

class SubscriberOrganization(models.Model):
	subscriber = models.ForeignKey(User)
	org_name = models.CharField(max_length=200)
	def __str__(self):
		return self.org_name

#class Subscriber(models.Model):
#	username = models.CharField(max_length=36)
#	password = models.CharField(max_length=256)
#	email = models.EmailField(max_length=200)
#	first_name = models.CharField(max_length=36)
#	last_name = models.CharField(max_length=36)
#	organization = models.ForeignKey(SubscriberOrganization)
#	def __str__(self):
#		return self.username

## Individual Section - These models map out the data we are storing in the CRM ##

class IndividualOrganization(models.Model):
	org_name = models.CharField(max_length=200)
	parent_org = models.ForeignKey(SubscriberOrganization)
	def __str__(self):
		return self.org_name

class Individual(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
#	organization = models.ForeignKey(IndividualOrganization)
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	bio = models.TextField()
	#string formatting is used here - taking variables and putting them into a string
	parent_org = models.ForeignKey(SubscriberOrganization)
	def __str__(self):
		return "{0} {1}".format(self.first_name, self.last_name)

class Deal(models.Model):
	deal_name = models.CharField(max_length=200)
	individual = models.ForeignKey(Individual)
	deal_size = models.CharField(max_length=200)
	probability = models.IntegerField()
	parent_org = models.ForeignKey(SubscriberOrganization)
	def __str__(self):
		return self.deal_name

