from .models import *
from table import Table
from table.columns import *
from django.utils.html import escape
from table.utils import Accessor
from datetime import date,timedelta


class DTColumn(Column):
    ''' Display Date input and blank instead of None '''

    def render(self, value):
        data = Accessor(self.field).resolve(value)
        date = data.strftime("%d/%m/%Y") if data else ''
        return escape(date)

class DueDTColumn(Column):
    ''' Display Date input and blank instead of None '''

    def render(self, value):
        data = Accessor(self.field).resolve(value)
        data_new = value.sowing_date + timedelta(days=value.days) if data else ''
        data_new = data_new.strftime("%d/%m/%Y") if data_new >= date.today() else ''
        return escape(data_new)

class FarmTable(Table):
    name = Column(field='farmer', header='Farmer Name')
    area = Column(field='area', header='Area')
    village = Column(field='village', header='Village')
    crop_grown = Column(field='crop_grown', header='Crop Grown')
    sowing_date = DTColumn(field='sowing_date', header='Sowing Date')

    class Meta:
        model = Farm

class ScheduleTable(FarmTable):

    class Meta:
        model = Farm

class PriceTable(Table):
    name = Column(field='name', header='Farmer Name')
    total_price = Column(field='total_price', header='Total Price')

    class Meta:
        model = Farmer

class DueTable(FarmTable):
    due_date = DueDTColumn(field='days', header='Schedule Due Date')

    class Meta:
        model = Farm