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
        # hide the resource if request wasn't made by XHR
        if not self.request.is_xhr:
            return self.response.set_status(404)

        try:
            resp = urlfetch.fetch(self.GROOVESHARK_URL,
                                  headers=self._copy_request_headers(),
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


app = webapp2.WSGIApplication([
    ('/', GroovesharkHandler),
], debug=True)
