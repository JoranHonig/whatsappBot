import re

class Handler():
  def __init__(self):
    self.expression = re.compile(".*") 

  def expression(self):
    return self.expression
  
  def handle(self, message):
    return True 
   
