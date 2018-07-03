import django_filters
from django import forms
from .models import Df1, Dc1

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
    status = django_filters.MultipleChoiceFilter(choices=STATUS_CHOICES)
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
			'zip'
        ]

class Dc1Filter(django_filters.FilterSet):
    #filer_name = django_filters.CharFilter(lookup_expr='icontains')
    #status = django_filters.MultipleChoiceFilter(choices=STATUS_CHOICES)
    class Meta:
        model = Dc1
        fields = [
        	#'filer_id',
			'freport_id',
			'transaction_code',
			'e_year',
			't3_trid',
			'date1_10',
			'date2_12',
			'contrib_code_20',
			'contrib_type_code_25',
			'corp_30',
			'first_name_40',
			'mid_init_42',
			'last_name_44',
			'addr_1_50',
			'city_52',
			'state_54',
			'zip_56',
			'check_no_60',
			'check_date_62',
			'amount_70',
			'amount2_72',
			'description_80',
			'other_recpt_code_90',
			'purpose_code1_100',
			'purpose_code2_102',
			'explanation_110',
			'xfer_type_120',
			'chkbox_130',
			'crerec_uid',
			'crerec_date'
        ]