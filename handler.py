import re
import handlers

#
class MessageHandler():
    def __init__(self):
        """ This class is used to pass information from the yowsup stack to specific handlers """
        self.handlers = {}
        handl = handlers.led.LedHandler()
        expr = handl.expression
        self.handlers[expr] = handl

    def handle(self, message):
        """ Distributes the message to the appropriate handler by using its expression."""
        print "Handling mesage."
        for expression in self.handlers.keys():
            match = expression.match(message)
        if match != None:
             # Found handler
             handler = self.handlers[expression]
             return handler.handle(match.group(0))
        return 0


    def register(self, handler):
        """Registers a handler with the MessageHandler

        This function adds handler to this.handlers, using handler.expression() as the key
        """
        regex = handler.expression()
        if (self.handlers.has_key(regex)):
            return 0
        dict[regex] = handler
        return 1
