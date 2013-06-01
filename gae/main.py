import logging
import webapp2
from google.appengine.api import urlfetch


class GroovesharkHandler(webapp2.RequestHandler):
    GROOVESHARK_URL = 'http://grooveshark.com'
    TIMEOUT = 10

    _exclude_headers = frozenset(['Origin', 'Host'])

    def _copy_request_headers(self):
        return {key: val for key, val in self.request.headers.items()
                if not (key in self._exclude_headers or key.startswith('X-'))}

    def get(self):
        # resource forbidden if request wasn't made by XHR
        if not self.request.is_xhr:
            return self.response.set_status(403)

        # prepare URL Fetch re headers
        req_headers = self._copy_request_headers()

        # rewrite cookies
        if 'X-Cookie' in self.request.headers:
            req_headers['Cookie'] = self.request.headers['X-Cookie']

        # header needed for CORS
        self.response.headers.add('Access-Control-Allow-Origin', '*')

        try:
            resp = urlfetch.fetch(self.GROOVESHARK_URL, headers=req_headers,
                                  follow_redirects=False,
                                  deadline=self.TIMEOUT)
        except (urlfetch.DownloadError, urlfetch.ResponseTooLargeError) as e:
            self.response.set_status(500)
            self.response.out.write(e.message)
            logging.exception('fetching url failed')
        else:
            self.response.set_status = resp.status_code
            for key, val in resp.headers.items():
                self.response.headers.add(key, val)
            self.response.out.write(resp.content)

    def options(self):
        """OPTIONS method, needed for CORS

        Returns response with `Access-Control-Allow-*` headers
        required by CORS. This method will not be called if you added
        pattern that matches this host to the permissions sections of
        your manifest file.
        """
        self.response.headers.add('Access-Control-Allow-Origin', '*')
        self.response.headers.add('Access-Control-Allow-Headers',
                                  'X-Cookie, X-Requested-With')
        self.response.headers.add('Access-Control-Allow-Methods', 'GET')


app = webapp2.WSGIApplication([
    ('/', GroovesharkHandler),
], debug=True)
