import webapp2

from handlers import MainHandler

app = webapp2.WSGIApplication([('/', MainHandler),
                              ],
                              debug=True)
