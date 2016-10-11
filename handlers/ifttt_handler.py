import re
import requests
from __init__ import Handler

methods = {
  "post" : request.post,
  "get"  : request.get,
}
class IftttHandler(Handler):

  def __init__(self):
    self.expression = re.compile("somereg_ex")
    apikey = "secretkey"
    return 1

  def expression(self):
    return self.expression

  def handle():
    return 1

  def build_uri(self, message):
    prefix  = https://maker.ifttt.com/trigger/
    event   = message
    postfix = /with/key/ + apikey
    
    return (prefix + event + postfix)
  def do_req(self, message, parameters, method):
    r = methods[method]( self.build_uri(message), data = parameters )
