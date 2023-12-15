from django.urls import converters

class LongStringConverter(converters.StringConverter):
    regex = '[\s\S]*'
