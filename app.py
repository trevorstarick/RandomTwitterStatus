from twitter import *
from random import choice

AZaz = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_random_str():
    return ''.join(choice(AZaz) for _ in range(10))

bot = Twitter(auth=OAuth('243403250-g6MFdKqhdsC9haHRRifhaegH78UKskJuGU9ff0','nFGgJ0XmLNPylDF4pFF3KcxuCesO68oX37z9PA3OY','bWtVjG0ujOvYanIHa1WEw','YKPDjxaSmdLtFztvE4WPjEv1sYSL7FT2yOnnw8U'))
def tweet():
  status="@trevorstarick: "+ get_random_str()
	bot.statuses.update(status=status)

tweet()
