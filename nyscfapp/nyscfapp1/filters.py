import django_filters
from django import forms
from .models import Df1, Dc1, Zip2Fips

# class Df1Filter(django_filters.FilterSet):
# 	status = django_filters.ModelMultipleChoiceFilter(queryset=Df1.objects.all(),widget=forms.CheckboxSelectMultiple)
    
#     class Meta:
#         model = Df1
#         fields = ['filer_id', 'filer_name', 'filer_type', 'status']

# class Df1Filter(django_filters.FilterSet):
# 	filer_name = django_filters.CharFilter(lookup_expr='icontains')

#     class Meta:
#         model = Df1
#         fields = ['filer_id', 'filer_name', 'filer_type', 'status']


# class Df1Filter(django_filters.FilterSet):
#     filer_name = django_filters.CharFilter(lookup_expr='icontains')
#     status = django_filters.ModelMultipleChoiceFilter(
#     	name='status',
#     	to_field_name='status',
#     	queryset=Df1.objects.all())
#     class Meta:
#         model = Df1
#         fields = ['filer_id', 'filer_name', 'filer_type']
STATUS_LIST = Df1.objects.values_list('status', flat=True).distinct()

STATUS_CHOICES = [(s, s) for s in STATUS_LIST]

# STATUS_CHOICES = [
# 	('ACTIVE', 'ACTIVE'),
# 	('INACTIVE', "INACTIVE")
# ]

class Df1Filter(django_filters.FilterSet):
    filer_name = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.ChoiceFilter(choices=STATUS_CHOICES)
    #zip = django_filters.Zip2Fips.CharFilter(lookup_expr='iexact')
    #zip_id = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Df1
        fields = [
        	'filer_id',
			'filer_name', 
			'filer_type', 
			'status', 
			'committee_type', 
			'office', 
			'district', 
			'treas_first_name', 
			'treas_last_name', 
			'address', 
			'city', 
			'state', 
			'zip__zip'
        ]

# class Dc1Filter(django_filters.FilterSet):
#     #filer_name = django_filters.CharFilter(lookup_expr='icontains')
#     #status = django_filters.MultipleChoiceFilter(choices=STATUS_CHOICES)
#     class Meta:
#         model = Dc1
#         fields = [
#         	#'filer_id',
# 			'freport_id',
# 			'transaction_code',
# 			'e_year',
# 			't3_trid',
# 			'date1_10',
# 			'date2_12',
# 			'contrib_code_20',
# 			'contrib_type_code_25',
# 			'corp_30',
# 			'first_name_40',
# 			'mid_init_42',
# 			'last_name_44',
# 			'addr_1_50',
# 			'city_52',
# 			'state_54',
# 			'zip_56',
# 			'check_no_60',
# 			'check_date_62',
# 			'amount_70',
# 			'amount2_72',
# 			'description_80',
# 			'other_recpt_code_90',
# 			'purpose_code1_100',
# 			'purpose_code2_102',
# 			'explanation_110',
# 			'xfer_type_120',
# 			'chkbox_130',
# 			'crerec_uid',
# 			'crerec_date'
#         ]

# class Dc1Filter(django_filters.FilterSet):
#     #filer_name = django_filters.CharFilter(lookup_expr='icontains')
#     #status = django_filters.MultipleChoiceFilter(choices=STATUS_CHOICES)
#     class Meta:
#         model = Df1


# TRANCACTION_CODE_CHOICES = [
# 	( 'A', 'A' ),
# 	( 'B', 'B' ),
# 	( 'C', 'C' ),
# 	( 'D', 'D' ),
# 	( 'E', 'E' ),
# 	( 'F', 'F' ),
# 	( 'G', 'G' ),
# 	( 'H', 'H' ),
# 	( 'I', 'I' ),
# 	( 'J', 'J' ),
# 	( 'K', 'K' ),
# 	( 'L', 'L' ),
# 	( 'M', 'M' ),
# 	( 'N', 'N' ),
# 	( 'O', 'O' ),
# 	( 'P', 'P' ),
# 	( 'Q', 'Q' ),
# 	( 'R', 'R' ),
# 	( 'R', 'R' ),
# 	( 'X', 'X' ),
# 	( 'Y', 'Y' ),
#  ]

TRANCACTION_CODE_CHOICES = [
	( 'A', 'A - Monetary Contributions/Individual & Partnerships' ),
	( 'B', 'B - Monetary Contributions/Corporate' ),
	( 'C', 'C - Monetary Contributions/All Other' ),
	( 'D', 'D - In Kind Contributions' ),
	( 'E', 'E - Other Receipts' ),
	( 'F', 'F - Expenditure/Payments' ),
	( 'G', 'G - Transfers In' ),
	( 'H', 'H - Transfers Out' ),
	( 'I', 'I - Loans Received' ),
	( 'J', 'J - Loan Repayments' ),
	( 'K', 'K - Liabilities/Loans Forgiven' ),
	( 'L', 'L - Expenditure Refunds' ),
	( 'M', 'M - Contributions Refunded' ),
	( 'N', 'N - Outstanding Liabilities' ),
	( 'O', 'O - Partners / Subcontracts' ),
	( 'P', 'P - Non Campaign Housekeeping Receipts' ),
	( 'Q', 'Q - Non Campaign Housekeeping Expenses' ),
	( 'R', 'R - Unknown Code' ),
	( 'V', 'V - Unknown Code' ),
	( 'X', 'X - A No Activity Statement Was Submitted' ),
	( 'Y', 'Y - A In Lieu Of Statement Was Submitted' ),
 ]
FREPORT_CODE_CHOICES = [
	( 'A', 'A - 32 Day Pre-Primary' ),
	( 'B', 'B - 11 Day Pre-Primary' ),
	( 'C', 'C - 10 Day Post-Primary' ),
	( 'D', 'D - 32 Day Pre-General' ),
	( 'E', 'E - 11 Day Pre-General' ),
	( 'F', 'F - 27 Day Post-General' ),
	( 'G', 'G - 32 Day Pre-Special' ),
	( 'H', 'H - 11 Day Pre-Special' ),
	( 'I', 'I - 27 Day Post-Special' ),
	( 'J', 'J - January Periodic' ),
	( 'K', 'K - July Periodic' ),
	( 'L', 'L - Off-Cycle' ),
 ]



#ABCDGP

class Dc1Filter(django_filters.FilterSet):
    #filer_name = django_filters.CharFilter(lookup_expr='icontains')
    freport_id = django_filters.MultipleChoiceFilter(choices=FREPORT_CODE_CHOICES)
    transaction_code = django_filters.MultipleChoiceFilter(choices=TRANCACTION_CODE_CHOICES)
    corp_30 = django_filters.CharFilter(lookup_expr='icontains')
    first_name_40 = django_filters.CharFilter(lookup_expr='icontains')
    mid_init_42 = django_filters.CharFilter(lookup_expr='icontains')
    last_name_44 = django_filters.CharFilter(lookup_expr='icontains')
    #zip_56 = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Dc1

        fields = [
        	#'filer_id_id',
			'e_year',
			#'t3_trid',
			'corp_30',
			'first_name_40',
			'mid_init_42',
			'last_name_44',
			'addr_1_50',
			'city_52',
			'state_54',
			'zip_56__zip',
			#'check_no_60',
			#'check_date_62',
			'amount_70',
			'amount2_72',
			'date1_10',
			'date2_12',
			'contrib_code_20',
			'contrib_type_code_25',
			'freport_id',
			'transaction_code',
			#'description_80',
			#'other_recpt_code_90',
			#'purpose_code1_100',
			#'purpose_code2_102',
			#'explanation_110',
			#'xfer_type_120',
			#'chkbox_130',
			#'crerec_uid',
			#'crerec_date', 
        ]