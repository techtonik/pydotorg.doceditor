"""
See app/README.rst for setup instructions
"""

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from app import docedit


class MainPage(webapp.RequestHandler):
    def get(self):
        applink = ('/docedit', 'DocEdit Version %s' % docedit.__version__)
        self.response.out.write('<a href="%s">%s</a>' % applink)
        # [ ] make this link to action through function
        #     to avoid grepping when link changes

class DocEdit(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Still writing..')


urlmap = [
    ('/', MainPage),
    ('/docedit', DocEdit),
]

def main():
    app = webapp.WSGIApplication(urlmap, debug=True)
    run_wsgi_app(app)


if __name__ == '__main__':
    main()
