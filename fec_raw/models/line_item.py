from decimal import Decimal
from django.db import models
from fec_raw.fields import CharField, IntegerField, DecimalField

class RawContribution(models.Model):
    """
    One-to-one mapping of the fields in the raw data CSVs.
    Specific to Schedule A line items.
    """
    filing_no = IntegerField(
        db_index=True
    )
    form_type = CharField(
        max_length=8
    )
    filer_committee_id_number = CharField(
        max_length=9
    )
    transaction_id = CharField(
        max_length=20,
        null=True,
        blank=True
    )
    back_reference_tran_id_number = CharField(
        max_length=20,
        null=True,
        blank=True
    )
    back_reference_sched_name = CharField(
        max_length=8,
        null=True,
        blank=True
    )
    entity_type = CharField(
        max_length=3,
        null=True,
        blank=True
    )
    contributor_organization_name = CharField(
        max_length=200,
        null=True,
        blank=True
    )
    contributor_last_name = CharField(
        max_length=50,
        null=True,
        blank=True
    )
    contributor_first_name = CharField(
        max_length=50,
        null=True,
        blank=True
    )
    contributor_middle_name = CharField(
        max_length=50,
        null=True,
        blank=True
    )
    contributor_prefix = CharField(
        max_length=10,
        null=True,
        blank=True
    )
    contributor_suffix = CharField(
        max_length=10,
        null=True,
        blank=True
    )
    contributor_street_1 = CharField(
        max_length=50,
        null=True,
        blank=True
    )
    contributor_street_2 = CharField(
        max_length=50,
        null=True,
        blank=True
    )
    contributor_city = CharField(
        max_length=30,
        null=True,
        blank=True
    )
    contributor_state = CharField(
        max_length=2,
        null=True,
        blank=True
    )
    contributor_zip_code = CharField(
        max_length=20,
        null=True,
        blank=True
    )
    election_code = CharField(
        max_length=5,
        null=True,
        blank=True
    )
    election_other_description = CharField(
        max_length=200,
        null=True,
        blank=True
    )
    contribution_date = models.DateField(
        auto_now=False,
        null=True
    )
    contribution_amount = DecimalField(
        max_digits=16,
        decimal_places=2,
        default=0,
        null=True
    )
    contribution_aggregate = DecimalField(
        max_digits=16,
        decimal_places=2,
        default=0,
        null=True
    )
    contribution_purpose_descrip = CharField(
        max_length=100,
        null=True,
        blank=True
    )
    contributor_employer = CharField(
        max_length=50,
        null=True,
        blank=True
    )
    contributor_occupation = CharField(
        max_length=50,
        null=True,
        blank=True
    )
    donor_committee_fec_id = CharField(
        max_length=9,
        null=True,
        blank=True
    )
    donor_committee_name = CharField(
        max_length=200,
        null=True,
        blank=True
    )
    donor_candidate_fec_id = CharField(
        max_length=9,
        null=True,
        blank=True
    )
    donor_candidate_last_name = CharField(
        max_length=50,
        null=True,
        blank=True
    )
    donor_candidate_first_name = CharField(
        max_length=50,
        null=True,
        blank=True
    )
    donor_candidate_middle_name = CharField(
        max_length=50,
        null=True,
        blank=True
    )
    donor_candidate_prefix = CharField(
        max_length=200,
        null=True,
        blank=True
    )
    donor_candidate_suffix = CharField(
        max_length=10,
        null=True,
        blank=True
    )
    donor_candidate_office = CharField(
        max_length=1,
        null=True,
        blank=True
    )
    donor_candidate_state = CharField(
        max_length=2,
        null=True,
        blank=True
    )
    donor_candidate_district = CharField(
        max_length=2,
        null=True,
        blank=True
    )
    conduit_name = CharField(
        max_length=200,
        null=True,
        blank=True
    )
    conduit_street1 = CharField(
        max_length=50,
        null=True,
        blank=True
    )
    conduit_street2 = CharField(
        max_length=50,
        null=True,
        blank=True
    )
    conduit_city = CharField(
        max_length=30,
        null=True,
        blank=True
    )
    conduit_state = CharField(
        max_length=2,
        null=True,
        blank=True
    )
    conduit_zip_code = CharField(
        max_length=20,
        null=True,
        blank=True
    )
    memo_code = CharField(
        max_length=1,
        null=True,
        blank=True
    )
    memo_text_description = CharField(
        max_length=200,
        null=True,
        blank=True
    )
    reference_code = CharField(
        max_length=9,
        null=True,
        blank=True)

    # For lobbyist contributions from F3L SA line items
    lobbyist_registrant_organization_name = CharField(
        max_length=200,
        null=True,
        blank=True)
    lobbyist_registrant_last_name = CharField(
        max_length=50,
        null=True,
        blank=True)
    lobbyist_registrant_first_name = CharField(
        max_length=50,
        null=True,
        blank=True)
    lobbyist_registrant_middle_name = CharField(
        max_length=50,
        null=True,
        blank=True)
    lobbyist_registrant_prefix = CharField(
        max_length=10,
        null=True,
        blank=True)
    lobbyist_registrant_suffix = CharField(
        max_length=10,
        null=True,
        blank=True)
    lobbyist_registrant_street_1 = CharField(
        max_length=50,
        null=True,
        blank=True)
    lobbyist_registrant_street_2 = CharField(
        max_length=50,
        null=True,
        blank=True)
    lobbyist_registrant_city = CharField(
        max_length=30,
        null=True,
        blank=True)
    lobbyist_registrant_state = CharField(
        max_length=2,
        null=True,
        blank=True)
    lobbyist_registrant_zip_code = CharField(
        max_length=20,
        null=True,
        blank=True)
    contribution_purpose_code = CharField(
        max_length=100,
        null=True,
        blank=True)
    bundled_amount_period = DecimalField(
        max_digits=16,
        decimal_places=2,
        default=0,
        null=True)
    bundled_amount_semi_annual = DecimalField(
        max_digits=16,
        decimal_places=2,
        default=0,
        null=True)
    lobbyist_registrant_employer = CharField(
        max_length=50,
        null=True,
        blank=True)
    lobbyist_registrant_occupation = CharField(
        max_length=50,
        null=True,
        blank=True)
    associated_text_record = CharField(
        max_length=200,
        null=True,
        blank=True)
    memo_text = CharField(
        max_length=100,
        null=True,
        blank=True)
    reference_code = CharField(
        max_length=50,
        null=True,
        blank=True)

    def __unicode__(self):
        return 'SA {} in filing {}'.format(
            self.transaction_id,
            self.filing_no)

class RawIndependentExpenditure(models.Model):
    """
    One-to-one mapping of the fields in the raw data CSVs.
    Specific to Schedule E line items.
    """
    filing_no = models.IntegerField(
        db_index=True)
    form_type = CharField(
        max_length=8)
    filer_committee_id_number = CharField(
        max_length=9)
    transaction_id_number = CharField(
        max_length=20)
    back_reference_tran_id_number = CharField(max_length=20,
        null=True,
        blank=True)
    back_reference_sched_name = CharField(max_length=8,
        null=True,
        blank=True)
    entity_type = CharField(max_length=3,
        null=True,
        blank=True)
    payee_organization_name = CharField(
        max_length=200,
        null=True,
        blank=True)
    payee_last_name = CharField(
        max_length=50,
        null=True,
        blank=True)
    payee_first_name = CharField(
        max_length=50,
        null=True,
        blank=True)
    payee_middle_name = CharField(
        max_length=50,
        null=True,
        blank=True)
    payee_prefix = CharField(
        max_length=10,
        null=True,
        blank=True)
    payee_suffix = CharField(
        max_length=10,
        null=True,
        blank=True)
    payee_street_1 = CharField(
        max_length=50,
        null=True,
        blank=True)
    payee_street_2 = CharField(
        max_length=50,
        null=True,
        blank=True)
    payee_city = CharField(
        max_length=30,
        null=True,
        blank=True)
    payee_state = CharField(
        max_length=2,
        null=True,
        blank=True)
    payee_zip_code = CharField(
        max_length=20,
        null=True,
        blank=True)
    election_code = CharField(
        max_length=5,
        null=True,
        blank=True)
    election_other_description = CharField(
        max_length=20,
        null=True,
        blank=True)
    dissemination_date = models.DateField(
        auto_now=False,
        null=True)
    expenditure_amount = DecimalField(
        max_digits=16,
        decimal_places=2,
        default=0)
    disbursement_date = models.DateField(
        auto_now=False,
        null=True)
    calendar_y_t_d_per_election_office = DecimalField(
        max_digits=16,
        decimal_places=2,
        default=0)
    expenditure_purpose_descrip = CharField(
        max_length=100,
        null=True,
        blank=True)
    category_code = CharField(
        max_length=3,
        null=True,
        blank=True)
    payee_cmtte_fec_id_number = CharField(
        max_length=9,
        null=True,
        blank=True)
    support_oppose_code = CharField(max_length=1,
        null=True,
        blank=True)
    candidate_id_number = CharField(max_length=9,
        null=True,
        blank=True)
    candidate_last_name = CharField(
        max_length=50,
        null=True,
        blank=True)
    candidate_first_name = CharField(
        max_length=50,
        null=True,
        blank=True)
    candidate_middle_name = CharField(
        max_length=50,
        null=True,
        blank=True)
    candidate_prefix = CharField(
        max_length=10,
        null=True,
        blank=True)
    candidate_suffix = CharField(
        max_length=10,
        null=True,
        blank=True)
    candidate_office = CharField(
        max_length=3,
        null=True,
        blank=True)
    candidate_district = CharField(
        max_length=2,
        null=True,
        blank=True)
    candidate_state = CharField(
        max_length=2,
        null=True,
        blank=True)
    completing_last_name = CharField(
        max_length=50,
        null=True,
        blank=True)
    completing_first_name = CharField(
        max_length=50,
        null=True,
        blank=True)
    completing_middle_name = CharField(
        max_length=50,
        null=True,
        blank=True)
    completing_prefix = CharField(
        max_length=10,
        null=True,
        blank=True)
    completing_suffix = CharField(
        max_length=10,
        null=True,
        blank=True)
    date_signed = models.DateField(
        auto_now=False, null=True)
    memo_code = CharField(
        max_length=1,
        null=True,
        blank=True)
    memo_text_description = CharField(
        max_length=100,
        null=True,
        blank=True)

    def __unicode__(self):
        return 'IE {} in filing {}'.format(
            self.transaction_id_number,
            self.filing_no)
