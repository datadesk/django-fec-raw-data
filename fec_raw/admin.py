from django.contrib import admin
from fec_raw.models import RawF3XFiling, RawF3PFiling, RawF24Filing
from fec_raw.models import RawContribution, RawIndependentExpenditure

class RawF3XFilingAdmin(admin.ModelAdmin):
    pass

class RawF3PFilingAdmin(admin.ModelAdmin):
    pass

class RawF24FilingAdmin(admin.ModelAdmin):
    pass

class RawContributionAdmin(admin.ModelAdmin):
    pass

class RawIndependentExpenditureAdmin(admin.ModelAdmin):
    pass

admin.site.register(RawF3XFiling, RawF3XFilingAdmin)
admin.site.register(RawF3PFiling, RawF3PFilingAdmin)
admin.site.register(RawF24Filing, RawF24FilingAdmin)
admin.site.register(RawContribution, RawContributionAdmin)
admin.site.register(RawIndependentExpenditure, RawIndependentExpenditureAdmin)