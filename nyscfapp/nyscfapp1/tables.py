# tutorial/tables.py
import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from .models import Df1, Dc1
#from django.core.urlresolvers import reverse


class Df1Table(tables.Table):
	filer_id = tables.LinkColumn('filers_detail', args=[A('pk')])

	class Meta:
		model = Df1
		template_name = 'django_tables2/bootstrap.html'


class Dc1Table(tables.Table):


	class Meta:
		model = Dc1
		template_name = 'django_tables2/bootstrap.html'
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
			'zip_56',
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

		def set_fields(self, fSet='default'):
			print (fSet)
			if fSet == 'default':
				self.fields = [
					#'filer_id_id',
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
					#'check_no_60',
					#'check_date_62',
					'amount_70',
					'amount2_72',
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
			elif fSet == 'all':
				self.fields = [
					#'filer_id_id',
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
					'crerec_date', 
				]

			else:
				self.fields = []

	# def show_all_fields(self):
	# 	self.fields = [
	# 	'filer_id_id',
	# 	'freport_id',
	# 	'transaction_code',
	# 	'e_year',
	# 	't3_trid',
	# 	'date1_10',
	# 	'date2_12',
	# 	'contrib_code_20',
	# 	'contrib_type_code_25',
	# 	'corp_30',
	# 	'first_name_40',
	# 	'mid_init_42',
	# 	'last_name_44',
	# 	'addr_1_50',
	# 	'city_52',
	# 	'state_54',
	# 	'zip_56',
	# 	'check_no_60',
	# 	'check_date_62',
	# 	'amount_70',
	# 	'amount2_72',
	# 	'description_80',
	# 	'other_recpt_code_90',
	# 	'purpose_code1_100',
	# 	'purpose_code2_102',
	# 	'explanation_110',
	# 	'xfer_type_120',
	# 	'chkbox_130',
	# 	'crerec_uid',
	# 	'crerec_date', 
	# 	]




# data = [
#     {'name': 'Bradley'},
#     {'name': 'Stevie'},
# ]

# class NameTable(tables.Table):
#     name = tables.Column()


def table_field_presets(fSet):
	if fSet == 'default':
		fields = [
			#'filer_id_id',
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
			#'check_no_60',
			#'check_date_62',
			'amount_70',
			'amount2_72',
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
	elif fSet == 'all':
		fields = [
			'filer_id',
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
			'crerec_date', 
		]

	else:
		fields = []

	return fields

