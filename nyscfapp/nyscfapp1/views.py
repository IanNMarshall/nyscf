 # howdy/views.py
import math
import geopandas as gp
import pandas as pd
from .helpers import county_plot as cp
from django.shortcuts import render
from django.views import generic
from django_filters.views import FilterView, FilterMixin
from django_tables2.views import SingleTableView, SingleTableMixin, RequestConfig
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Df1, Dc1, Zip2Fips
from django.db.models import Sum
from .filters import Df1Filter, Dc1Filter
from .tables import Df1Table, Dc1Table
from django_tables2.export.views import ExportMixin
#for plotly views
from rest_framework.views import APIView
from rest_framework.response import Response
import sys, os
from nyscfapp.settings import BASE_DIR
#file_path = os.path.join(BASE_DIR, '/nyscfapp1/helpers/')
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
    num_conts = Dc1.objects.all().count()
    def get(self, request, **kwargs):

        return render(
            request, 
            'nyscf_home.html', 
            context={'num_filers':self.num_filers, 'num_conts':self.num_conts})


class NYSCFFilerView(FilterView): #FilterMixin, generic.ListView):
    template_name = "df1_list.html"
    model = Df1
    filterset_class = Dc1Filter
    #queryset
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
    def get_county_plot_data(self, **kwargs):
        df = cp.read_county_shp()
        
        
        df3 = cp.merge_dfs(df, 1)
        fig = cp.set_plot_data(df3)
        plot_div = cp.get_div(fig)
        plot_data = {
            "plot_div": plot_div,

        }
        return plot_data


    def get_plot_data(self, **kwargs):
        #initial filter - 
        slug = self.kwargs.get(self.slug_url_kwarg)
        cData = Dc1.objects.filter(filer_id=slug).values('e_year', 'corp_30', 'zip_56', 'state_54', 'amount_70')

        #years
        years2 = cData.values('e_year').annotate(Sum('amount_70'))
        years2 = sorted(years2, key=lambda x: x['amount_70__sum'])
        years2labels = [ row['e_year'] for row in years2 ]
        years2data = [ row['amount_70__sum'] for row in years2 ]
        #state 'state_54'
        state2 = cData.values('state_54').annotate(Sum('amount_70'))
        state2 = sorted(state2, key=lambda x: x['amount_70__sum'])
        state2labels = [ row['state_54'] for row in state2 ]
        state2data = [ row['amount_70__sum'] for row in state2 ]
        axis_state = 10000.0 #dynamically scale axis rnd to 10k, or 10k if no results
        if len(state2data) > 0:
            axis_state = math.ceil(float(state2data[-1]) / 
                10000.0)*10000.0
        #state 'zip_56'
        zip2 = cData.values('zip_56').annotate(Sum('amount_70'))
        zip2 = sorted(zip2, key=lambda x: x['amount_70__sum'])
        zip2labels = [ row['zip_56'] for row in zip2 ]
        zip2data = [ row['amount_70__sum'] for row in zip2 ]
        #fips lookup double underscore off of FK notation
        fips2 = cData.values('zip_56__fips').annotate(Sum('amount_70'))
        fips2 = sorted(fips2, key=lambda x: x['amount_70__sum'])
        fips2labels = [ row['zip_56__fips'] for row in fips2 ]
        fips2data = [ row['amount_70__sum'] for row in fips2 ]

        #convert to data frame to pass into county plot func.
        fips2df = {"FIPS": fips2labels, "AMT": fips2data}
        df_fips = pd.DataFrame.from_dict(fips2df)

        #external function calls for plot data generation
        df = cp.read_county_shp()
        df3 = cp.merge_dfs(df, df_fips)
        fig = cp.set_plot_data(df3)
        cont_by_county_plot_div = cp.get_div(fig)
        #test2 = Dc1.objects.filter(filer_id='C01217').values_list('zip_56', 'zip_56__fips')
        plot_data = {
            "cont_by_year_labels": years2labels,
            'cont_by_year_data': years2data,
            "cont_by_state_labels": state2labels,
            'cont_by_state_data': state2data,
            "cont_by_zip_labels": zip2labels,
            'cont_by_zip_data': zip2data,
            "cont_by_fips_labels": fips2labels,
            'cont_by_fips_data': fips2data,
            "cont_by_county_plot_div" : cont_by_county_plot_div,
            "axis_state": axis_state,

        }

        return plot_data


    #override context data to pass additional info
    def get_context_data(self, **kwargs):
        context = super(NYSCFFilerDetail2View, self).get_context_data(**kwargs)
        #cart_product_form = CartAddProductForm()
        plot_data = self.get_plot_data(**kwargs)
        #county_plot_data = self.get_county_plot_data(**kwargs)
        context['plot_data'] = plot_data
        #context['county_plot_data'] = county_plot_data
        print(context['df1'])
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


class NYSCFFilerDetailView(ExportMixin, SingleTableMixin, FilterView): #generic.DetailView): generic.detail.SingleObjectMixin,
    """
    Main Detail View of Filer - accessed by direct url 
    """
    template_name = "df1_detail_table.html"
    slug_url_kwarg = 'slug'
    #model = Dc1
    slug_field = 'filer_id'
    filterset_class = Dc1Filter
    table_class = Dc1Table #different model for table_class
    #queryset = Dc1.objects.filter(filer_id='A00162')
    master_qs = None

    test2 = "hello"


    def get_plot_data(self, **kwargs):

        """
        Format Data into nice dicts
        Call external helper functions to pull in GIS data
        Merge table data with GIS data
        Plotly offline plot -> div 
        Returns: entire div object to be embedded)
        """
        #initial filter - 
        slug = self.kwargs.get(self.slug_url_kwarg)
        #cData = Dc1.objects.filter(filer_id=slug).values('e_year', 'corp_30', 'zip_56', 'state_54', 'amount_70')
        cData = self.table_data.values('e_year', 'corp_30', 'zip_56', 'state_54', 'amount_70') #table data for auto update of charts on filtering
        #years
        years2 = cData.values('e_year').annotate(Sum('amount_70'))
        years2 = sorted(years2, key=lambda x: x['amount_70__sum'])
        years2labels = [ row['e_year'] for row in years2 ]
        years2data = [ row['amount_70__sum'] for row in years2 ]
        #state 'state_54'
        state2 = cData.values('state_54').annotate(Sum('amount_70'))
        state2 = sorted(state2, key=lambda x: x['amount_70__sum'])
        state2labels = [ row['state_54'] for row in state2 ]
        state2data = [ row['amount_70__sum'] for row in state2 ]
        #TO DO: Match dynamic scaling done in County Plot
        axis_state = 0.0 #dynamically scale axis rnd to 10k, or 10k if no results
        if len(state2data) > 0:
            axis_state = math.ceil(float(state2data[-1]) / 
                10000.0)*10000.0
        #state 'zip_56'
        zip2 = cData.values('zip_56').annotate(Sum('amount_70'))
        zip2 = sorted(zip2, key=lambda x: x['amount_70__sum'])
        zip2labels = [ row['zip_56'] for row in zip2 ]
        zip2data = [ row['amount_70__sum'] for row in zip2 ]
        #fips lookup double underscore off of FK notation
        fips2 = cData.values('zip_56__fips').annotate(Sum('amount_70'))
        fips2 = sorted(fips2, key=lambda x: x['amount_70__sum'])
        fips2labels = [ row['zip_56__fips'] for row in fips2 ]
        fips2data = [ row['amount_70__sum'] for row in fips2 ]

        #convert to data frame to pass into county plot func.
        fips2df = {"FIPS": fips2labels, "AMT": fips2data}
        df_fips = pd.DataFrame.from_dict(fips2df)
        df1_FIPS = Df1.objects.filter(filer_id=slug).values_list('zip__fips', flat=True)[0]

        #external function calls for plot data generation (python Plotly offline (see helpers))
        df = cp.read_county_shp()
        df3 = cp.merge_dfs(df, df_fips)
        fig = cp.set_plot_data(df3, df1_FIPS)
        cont_by_county_plot_div = cp.get_div(fig)

        #format to one dict which will add to context data and send with request
        plot_data = {
            "cont_by_year_labels": years2labels,
            'cont_by_year_data': years2data,
            "cont_by_state_labels": state2labels,
            'cont_by_state_data': state2data,
            "cont_by_zip_labels": zip2labels,
            'cont_by_zip_data': zip2data,
            "cont_by_fips_labels": fips2labels,
            'cont_by_fips_data': fips2data,
            "cont_by_county_plot_div" : cont_by_county_plot_div,
            "axis_state": axis_state,

        }

        return plot_data

    def get(self, request, *args, **kwargs):
        #print('hello_get')
        #print(self.master_qs)
        slug = self.kwargs.get(self.slug_url_kwarg)
        filterset_class = self.get_filterset_class()
        self.filterset = self.get_filterset(filterset_class)
        self.master_qs = self.filterset.qs.filter(filer_id=slug)
        #print(self.master_qs)




        #filterset_class = self.get_filterset_class()
        #self.filterset = self.get_filterset(filterset_class)
        self.object_list = self.master_qs #self.filterset.qs
        #slug = self.kwargs.get(self.slug_url_kwarg)
        #print(self.object_list)
        # if self.filterset.is_valid() or not self.get_strict():
        #     self.object_list = self.filterset.qs
        # else:
        #     self.object_list = self.filterset.queryset.none()

        context = self.get_context_data(filter=self.filterset,
                                        object_list=self.object_list)
        return self.render_to_response(context)

    def get_table(self, **kwargs):
        """
        OVERLOADED FROM SingleTableMixin in order to match table_data to filter_set
        """
        slug = self.kwargs.get(self.slug_url_kwarg)
        #print("hello")
        table_class = self.get_table_class()
        self.table_data = self.object_list.filter(filer_id=slug)
        table = table_class(data=self.table_data, **kwargs)
        return RequestConfig(self.request, paginate=self.get_table_pagination(table)).configure(
            table
        )



    #override context data to pass additional info
    def get_context_data(self, **kwargs):
        """
        Overload to add context data and filter on urlConf Slug
        """
        slug = self.kwargs.get(self.slug_url_kwarg)
        context = super(NYSCFFilerDetailView, self).get_context_data(**kwargs)
        plot_data = self.get_plot_data(**kwargs)
        context['plot_data'] = plot_data
        #TO DO: Find better way of ensuring we keep our filer_id=slug... dc1_set or something analogous?
        #print(len(context['object_list']))
        ##context['object_list'] = context['object_list'].filter(filer_id=slug) 
        #context['dc1_list'] = self.master_qs #context['dc1_list'].filter(filer_id=slug)
        #self.table_data = context['dc1_list'] #taking care of this in get_table didn't work here
        context['df1'] = Df1.objects.get(filer_id=slug)
        context['test3'] = 'hello' 
        #print (context['df1'].values_list())
        #print(len(context['object_list'].values_list()))
        print(context.keys())
        return context



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

        
        fips2 = Dc1.objects.filter(filer_id='C01217').values('zip_56__fips').annotate(Sum('amount_70'))
        fips2 = sorted(fips2, key=lambda x: x['amount_70__sum'])
        fips2labels = [ f['zip_56__fips'] for f in fips2 ]
        fips2data = [ f['amount_70__sum'] for f in fips2 ]


        

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
            "fips2labels": fips2labels,
            "fips2data": fips2data

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