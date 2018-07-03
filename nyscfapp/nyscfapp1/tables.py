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
	#filer_id = tables.Column(filer_id='C01217')
	#Df1.dc1_set
	#table = Df1.objects.filter(filer_id='C01217')
	tmp = "hello"
	#name = tables.Column()
	class Meta:
		model = Dc1
		template_name = 'django_tables2/bootstrap.html'




# data = [
#     {'name': 'Bradley'},
#     {'name': 'Stevie'},
# ]

# class NameTable(tables.Table):
#     name = tables.Column()



