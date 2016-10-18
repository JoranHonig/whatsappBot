import re
import handlers

#This class is used to pass information from the yowsup stack to specific handlers
class MessageHandler():
  def __init__(self):
    self.handlers = {}
    handl = handlers.led.LedHandler()
    expr = handl.expression
    self.handlers[expr] = handl

  def handle(self, message):
    print "Handling mesage."
    for expression in self.handlers.keys():
       match = expression.match(message) 
       if match != None:
         # Found handler
         handler = self.handlers[expression]
         return handler.handle(match.group(0))
    return 0


  def register(self, handler):
    regex = handler.expression()
    if (self.handlers.has_key(regex)):
      return 0
    dict[regex] = handler
    return 1
