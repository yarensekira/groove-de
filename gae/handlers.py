import webapp2

url = 'http://grooveshark.com'
import urllib2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        if not self.request.headers.get('Origin'):
            return self.response.out.write('')
        self.response.headers.add('Access-Control-Allow-Origin', '*')
        self.response.headers.add('Access-Control-Allow-Headers',
                                  'Content-Type')

        conn = urllib2.urlopen(url)
        html = conn.read()

        self.response.out.write(html)
