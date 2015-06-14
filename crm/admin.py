from django.contrib import admin

from crm.models import SubscriberOrganization, IndividualOrganization, Individual, Deal



class SubscriberOrganizationAdmin(admin.ModelAdmin):
	fields = ['org_name']
	search_fields = ['org_name']



class IndividualOrganizationAdmin(admin.ModelAdmin):
	fields = ['org_name', 'parent_org']
	search_fields = ['org_name', 'parent_org']

class IndividualAdmin(admin.ModelAdmin):
	fields = ['first_name', 'last_name', 'phone_number', 'email', 'organization', 'title', 'address', 'bio', 'parent_org']
	search_fields = ['first_name', 'last_name', 'phone_number', 'email', 'title', 'address', 'bio', 'parent_org']

class DealAdmin(admin.ModelAdmin):
	fields = ['deal_name', 'individual', 'deal_size', 'probability', 'parent_org']
	search_fields = ['deal_name', 'deal_size', 'probability', 'parent_org']

admin.site.register(SubscriberOrganization, SubscriberOrganizationAdmin)

admin.site.register(IndividualOrganization, IndividualOrganizationAdmin)
admin.site.register(Individual, IndividualAdmin)
admin.site.register(Deal, DealAdmin)