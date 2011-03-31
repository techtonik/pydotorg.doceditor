"""
See app/README.rst for setup instructions
"""

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')


def main():
    app = webapp.WSGIApplication([('/', MainHandler)], debug=True)
    run_wsgi_app(app)


if __name__ == '__main__':
    main()
