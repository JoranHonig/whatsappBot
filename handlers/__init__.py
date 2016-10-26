import re
import led

class Handler():
    """Super class for all handlers"""
    def __init__(self):
        self.expression = re.compile(".*")

    def expression(self):
        return self.expression
  
    def handle(self, message):
        return True
   
