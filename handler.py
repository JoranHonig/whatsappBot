import re
#This class is used to pass information from the yowsup stack to specific handlers
class MessageHandler():
  def __init__():
    self.handlers = {}

  def handle(self, message):
    for expression in self.handlers.keys():
       match = expression.match(message) 
       if match != None:
         # Found handler
         handler = handlers[expression]
         handler.handle(match.group(0))
    return 1


  def register(self, handler):
    regex = handler.expression()
    if (self.handlers.has_key(regex)):
      return 0
    dict[regex] = handler
    return 1
