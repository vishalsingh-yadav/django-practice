from django import template

register = template.Library()

@register.filter(name='cutt') #Decorator
def cutt(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cutt',cutt) # Used Decorator in place of this
