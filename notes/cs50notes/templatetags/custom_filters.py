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
    
    
    
# @register.filter(name='remove_spaces')
# def remove_spaces(value):
#     return value.strip()    


# modify your custom format_code filter to not only wrap code blocks in <code> 
# tags but also apply a text color change for those code blocks

@register.filter(name='format_code')
def format_code(value):
    # Split the input by triple backticks to find code blocks
    code_blocks = value.split('```')
    formatted_value = ''

    # Iterate through the code blocks
    for i, block in enumerate(code_blocks):
        # Wrap code blocks in <code> tags with green color and typewriter font
        if i % 2 == 0:
            formatted_value += block
        else:
            formatted_value += f'<code class="green-code typewriter-font">{block}</code>'

    return formatted_value


@register.filter(name='style_code')
def style_code(value):
    # Wrap the code in <code> tags with a CSS class for styling
    styled_code = f'<code class="code-style">{value}</code>'
    return styled_code