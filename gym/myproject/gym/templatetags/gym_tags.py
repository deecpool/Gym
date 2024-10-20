from django import template
import gym.views as views
from gym.utils import menu
register = template.Library()



@register.simple_tag()
def get_menu():
    return menu