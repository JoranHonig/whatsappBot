import re
from __init__ import Handler
class LedHandler(Handler):  
  def __init__(self):

    self.leds = {}
    for i in range(1,6):
      self.leds[i] = LedStrip(i, 1)

    self.expression = re.compile("led: ([a-z])+ (([a-z]|[A-Z])+|0?\.[0-9]+)( for [1-5])?")

  def expression(self):
    return self.expression

  def handle(self, message):
    print message
    return "Message received"
    words = message.split(' ')
    mode = words[1]
    value = words[2]
    if len(words) > 3:
      ledid = words[4]
   
    # No switch :'(
    if mode == 'cl' and ledid:
      self.handle_color(value, ledid)
    elif mode == 'cl':
      self.handle_color(value)
    elif mode == 'br' and ledid:
      self.handle_brightness(value, ledid)
    elif mode == 'br':
      self.handle_brightness(value)
    elif mode == 'md' and ledid:
      self.handle_mode(mode, ledid)
    elif mode == 'md':
      self.handle_mode(value)
    else:
      return 0

    return 1


  def handle_color(self, color):
    for i in range(1,6):
       self.leds[i].set_color(color)

  def handle_color(self, color, ledid):
    self.leds[ledid].set_color(color)

  def handle_brightness(self, brightness):
    for i in range(1,6):
       self.leds[i].set_brightness(brightness)

  def handle_brightness(self, brightness, ledid):
    self.leds[ledid].set_brightness(brightness)
  
  def handle_mode(self, mode):
    for i in range(1,6):
       self.leds[i].set_mode(mode)

  def handle_mode(self, mode, ledid):
    self.leds[ledid].set_mode(ledid) 

class LedStrip:
  def __init__(self, number, serial):
    self.serial = serial
    self.mode = 'default'
    self.brightness = 0.8
    self.color = 'white'
    self.number = number
  def set_color(self, color):
    self.color = color
      
  def set_brightness(self, brightness):
    self.brightness = brightness
  
  def set_mode(self, mode):
    self.mode = mode

