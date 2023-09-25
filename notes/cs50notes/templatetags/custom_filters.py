from django import template
import re
from html import unescape  
from django.utils.html import linebreaks



register = template.Library()

@register.filter
def add_line_breaks(value):
    return linebreaks(value)
    
    
@register.filter
def decode_html_entities(value):
    return unescape(value)

@register.filter
def remove_html_tags(value):
    # Use a regular expression to remove all HTML tags
    return re.sub(r'<[^>]*>', '', value)
    
@register.filter(name='remove_spaces')
def remove_spaces(value):
    return value.strip()