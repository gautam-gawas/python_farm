from django.views.generic import TemplateView
from .tables import *
from datetime import date,timedelta
from django.db.models import *


class FarmerListView(TemplateView):
    template_name = 'farm/home.html'

    def get_context_data(self, **kwargs):
        context = super(FarmerListView, self).get_context_data(**kwargs)
        schedule_query = Farm.objects.filter(sowing_date__range = (date.today(), (date.today() + timedelta(days=1))))
        farmer_query = Farm.objects.filter(crop_grown__isnull = False)
        price_query = Farmer.objects.annotate(total_price = Sum('farm__schedule__price'))
        due_query = Farm.objects.annotate(days= F("schedule__days_after_sowing"))
        context['schedule_table'] = ScheduleTable(schedule_query)
        context['farmer_table'] = FarmTable(farmer_query)
        context['price_table'] = PriceTable(price_query)
        context['due_table'] = DueTable(due_query)

        return context