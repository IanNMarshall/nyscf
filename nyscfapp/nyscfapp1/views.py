 # howdy/views.py
from django.shortcuts import render
from django.views import generic
from django_filters.views import FilterView
from django_tables2.views import SingleTableView, SingleTableMixin, RequestConfig
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Df1, Dc1, Zip2Fips
from .filters import Df1Filter, Dc1Filter
from .tables import Df1Table, Dc1Table
from django_tables2.export.views import ExportMixin
#for plotly views
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"


 # Add this view
class HankPageView(TemplateView):
    template_name = "hank.html"

class NYSCFHomeView(TemplateView):
    #template_name = "nyscf_home.html"
    num_filers = Df1.objects.all().count()
    def get(self, request, **kwargs):

        return render(
        	request, 
        	'nyscf_home.html', 
        	context={'num_filers':self.num_filers})


class NYSCFFilerView(generic.ListView):
    #template_name = "nyscf_home.html"
    model = Df1
    #num_filers = Df1.objects.all().count()
"""
class NYSCFFilerFilterView(SingleTableMixin, FilterView):

    #table_class = Df1
    #model = Df1
    #template_name = 'df1_filter.html'
    #filterset_class = Df1Filter
    #table = Df1Table(Df1.objects.all())
	def get(self, request, **kwargs):
		table = Df1Table(Df1.objects.all())
		RequestConfig(
			request, 
			paginate={'per_page': 25}).configure(table)
		return render(
			request, 
			'df1_filter.html', 
			{'filers': table})
"""
"""
#single table view
class NYSCFFilerFilterView(SingleTableMixin, FilterView):
	model = Df1
	table_class = Df1Table
	template_name = 'df1_filter.html'
    filterset_class = Df1Filter

""" #filter
class NYSCFFilerFilterView(ExportMixin, SingleTableMixin, FilterView):
	model = Df1
	table_class = Df1Table
	template_name = 'df1_filter.html'
	filterset_class = Df1Filter


class NYSCFContributionFilterView(ExportMixin, SingleTableMixin, FilterView):
    model = Dc1
    table_class = Dc1Table
    template_name = 'dc1_filter.html'
    filterset_class = Dc1Filter

	#def get(self, request, **kwargs):
        #return render(request)

class NYSCFFilerDetail2View(generic.DetailView):
    template_name = "df1_detail2.html"
    model = Df1
    slug_field = 'filer_id'
    #plot_data = ["Hello Hank!"]

    def get_plot_data(self, **kwargs):

        slug = self.kwargs.get(self.slug_url_kwarg)
        cData = Dc1.objects.filter(filer_id=slug).values('e_year', 'corp_30', 'zip_56', 'state_54', 'amount_70')
        cont_by_year = dict()
        cont_by_state = dict()
        cont_by_zip = dict()        
        cont_by_fips = dict() 
        for row in cData:
            #Year
            if row['e_year'] in cont_by_year.keys():
                cont_by_year[row['e_year']] = cont_by_year[row['e_year']]  + row['amount_70']
            else:
                cont_by_year[row['e_year']] = row['amount_70']
            #State
            if row['state_54'] in cont_by_state.keys():
                cont_by_state[row['state_54']] = cont_by_state[row['state_54']]  + row['amount_70']
            else:
                cont_by_state[row['state_54']] = row['amount_70']
            #Zips
            if row['zip_56'] in cont_by_zip.keys():
                cont_by_zip[row['zip_56']] = cont_by_zip[row['zip_56']]  + row['amount_70']
            else:
                cont_by_zip[row['zip_56']] = row['amount_70']
            #FIPS
            #row_fips = 
            #if row['zip_56'] in cont_by_zip.keys():
                #cont_by_zip[row['zip_56']] = cont_by_zip[row['zip_56']]  + row['amount_70']
            #else:
                #cont_by_zip[row['zip_56']] = row['amount_70']
        

        cont_by_year = sorted(cont_by_year.items(), key=lambda x: x[1])
        cont_by_year = dict(cont_by_year)
        cont_by_state = sorted(cont_by_state.items(), key=lambda x: x[1])
        cont_by_state = dict(cont_by_state)
        cont_by_zip = sorted(cont_by_zip.items(), key=lambda x: x[1])
        cont_by_zip = dict(cont_by_zip)
        cont_by_fips = sorted(cont_by_fips.items(), key=lambda x: x[1])
        cont_by_fips = dict(cont_by_fips)

        plot_data = {
            "cont_by_year_labels": cont_by_year.keys(),
            'cont_by_year_data': cont_by_year.values(),
            "cont_by_state_labels": cont_by_state.keys(),
            'cont_by_state_data': cont_by_state.values(),
            "cont_by_zip_labels": cont_by_zip.keys(),
            'cont_by_zip_data': cont_by_zip.values(),
            "cont_by_fips_labels": cont_by_fips.keys(),
            'cont_by_fips_data': cont_by_fips.values(),

        }
        return plot_data
        #plot_data = {"NY": 10000, "MA": 5001}
        #return plot_data
        #return str(plot_data).strip('"').replace("'", '"')
        #return "abcd"

    #override context data to pass additional info
    def get_context_data(self, **kwargs):
        context = super(NYSCFFilerDetail2View, self).get_context_data(**kwargs)
        #cart_product_form = CartAddProductForm()
        plot_data = self.get_plot_data(**kwargs)
        context['plot_data'] = plot_data
        return context



# class NYSCFFilerDetailView(generic.ListView):
#     template_name = "df1_list.html"
#     model = Df1

#     def get_queryset(self, **kwargs):
#         qs = super(generic.DetailView, self).get_queryset()
#         return qs



# class NYSCFFilerDetailView(SingleTableMixin, generic.DetailView):
#     template_name = "df1_detail_table.html"
#     model = Df1
    
#     #b = model.objects.filter(filer_id='C01217')
#     # def get_queryset(self, **kwargs):
#     #     qs = super(generic.DetailView, self).get_queryset()
#     #     return qs

#     table_class = Dc1Table


class NYSCFFilerDetailView(ExportMixin, SingleTableMixin, generic.DetailView):
    template_name = "df1_detail_table.html"
    model = Df1
    slug_field = 'filer_id'
    table_class = Dc1Table #different model for table_class
    table_data = [] #inintialize table_data, will be set by get_obj

    def get_object(self, queryset=None):
        """
        Overriding get_object from DetailView as to update table_data
        Return the object the view is displaying.
        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})

        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        #self.table_data = queryset.filter(pk=pk)
        self.table_data = Dc1.objects.filter(filer_id=slug)
        return obj


#plotly stuff
class ChartData(APIView):
# you can these two variables down the road to enhance security, but for now just leave them blank
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        articles = dict()
        #for company in Company.objects.all():
            #if company.articles.count() > 0:
                #articles[company.company_name] = company.articles.count()
        articles = {'google': 3, 'amazon': 2, 'netflix' : 5, 'facebook': 1}

        articles = sorted(articles.items(), key=lambda x: x[1])
        articles = dict(articles)

        data = {
            "article_labels": articles.keys(),
            "article_data": articles.values(),
        }
    
        return Response(data)

class ContByFilerAPIData(APIView):
# you can these two variables down the road to enhance security, but for now just leave them blank
    authentication_classes = []
    permission_classes = []
    #cData = Dc1.objects.filter(filer_id='C01217')
    def get(self, request, format=None):
        cData = Dc1.objects.filter(filer_id='C01217').values('e_year', 'corp_30', 'zip_56', 'state_54', 'amount_70')
        cont_by_year = dict()
        cont_by_state = dict()
        cont_by_zip = dict()        
        cont_by_fips = dict() 
        #cont_by_fips["?????"] = 0.00
        for row in cData:
            #Year
            if row['e_year'] in cont_by_year.keys():
                cont_by_year[row['e_year']] = cont_by_year[row['e_year']]  + row['amount_70']
            else:
                cont_by_year[row['e_year']] = row['amount_70']
            #State
            if row['state_54'] in cont_by_state.keys():
                cont_by_state[row['state_54']] = cont_by_state[row['state_54']]  + row['amount_70']
            else:
                cont_by_state[row['state_54']] = row['amount_70']
            #Zips
            if row['zip_56'] in cont_by_zip.keys():
                cont_by_zip[row['zip_56']] = cont_by_zip[row['zip_56']]  + row['amount_70']
            else:
                cont_by_zip[row['zip_56']] = row['amount_70']
            #FIPS
            q_row_fips = Zip2Fips.objects.filter(zip=row['zip_56']).values('fips')
            if (len(q_row_fips) > 0):
                row_fips = q_row_fips[0]
                if row_fips['fips'] in cont_by_fips.keys():
                    cont_by_fips[row_fips['fips']] = cont_by_fips[row_fips['fips']]  + row['amount_70']
                else:
                    cont_by_fips[row_fips['fips']] = row['amount_70']
            #Fips Lookup Failure
            else:
                if "?????" in cont_by_fips.keys():
                    cont_by_fips["?????"] = cont_by_fips["?????"]  + row['amount_70']
                else: 
                    cont_by_fips["?????"] = row['amount_70']

        

        cont_by_year = sorted(cont_by_year.items(), key=lambda x: x[1])
        cont_by_year = dict(cont_by_year)
        cont_by_state = sorted(cont_by_state.items(), key=lambda x: x[1])
        cont_by_state = dict(cont_by_state)
        cont_by_zip = sorted(cont_by_zip.items(), key=lambda x: x[1])
        cont_by_zip = dict(cont_by_zip)
        cont_by_fips = sorted(cont_by_fips.items(), key=lambda x: x[1])
        cont_by_fips = dict(cont_by_fips)

        data = {
            "cont_by_year_labels": cont_by_year.keys(),
            'cont_by_year_data': cont_by_year.values(),
            "cont_by_state_labels": cont_by_state.keys(),
            'cont_by_state_data': cont_by_state.values(),
            "cont_by_zip_labels": cont_by_zip.keys(),
            'cont_by_zip_data': cont_by_zip.values(),
            "cont_by_fips_labels": cont_by_fips.keys(),
            'cont_by_fips_data': cont_by_fips.values(),

        }

        return Response(data)

# SELECT E_YEAR, SUM(AMOUNT_70)
# FROM DC1
# WHERE CORP_30 LIKE 'Unitemized'
# AND (TRANSACTION_CODE = 'A'
# OR TRANSACTION_CODE = 'B'
# OR TRANSACTION_CODE = 'C'
# OR TRANSACTION_CODE = 'D'
# OR TRANSACTION_CODE = 'G'
# OR TRANSACTION_CODE = 'P')
# GROUP BY E_YEAR
# ORDER BY E_YEAR;



class ChartDataView(TemplateView):
    template_name = 'plotly2.html'

class ChartContribByYearView(TemplateView):
    template_name = 'plotly4.html'

class ChartContribByStateView(TemplateView):
    template_name = 'plotly6.html'



#No longer using ===========
def dex(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, filer_id):
    return HttpResponse("You're looking at filer %s." % filer_id)

    