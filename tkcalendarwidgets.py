# file: tkcalendarwidgets.py

from tkcalendar import Calendar, DateEntry
from pygubu import BuilderObject, register_widget


class DateEntryBuilder(BuilderObject):
    class_ = DateEntry


register_widget('tkcalendarwidgets.DateEntry', DateEntryBuilder,
                'DateEntry', ('ttk', 'My Tkcalendar widgets'))