import re
import requests
from __init__ import Handler


"""
    Todo:
     * Working version of library to send requests to the ifttt server
     * Update documentation to contain missing details
     * Useful handle function, possibly implement modular handle
"""

methods = {
    "post": request.post,
    "get": request.get,
}


class IftttHandler(Handler):
    """ This is a Handler class to communicate with the IFTTT service."""
    def __init__(self):
        self.expression = re.compile("somereg_ex")
        apikey = "secretkey"
        return 1

    def expression(self):
        """ Getter for the current expression. """
        return self.expression

    def handle(self):
        """ Currently unimplemented handle function."""
        return 1

    def build_uri(self, message):
        """ This function builds the ifttt request url"""
        prefix = "https://maker.ifttt.com/trigger/"
        event = message
        postfix = "/with/key/ + apikey"
        return (prefix + event + postfix)

    def do_req(self, message, parameters, method):
        """ This function performs the request to the ifttt service"""
        r = methods[method](self.build_uri(message), data=parameters)
