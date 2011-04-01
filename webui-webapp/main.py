"""
See app/README.rst for setup instructions
"""

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

# --- docedit import and configuration ---
from app import docedit

docedit.DOCDIR = 'app/docs/'
docedit.DOCURL = '/static/docs/'
# --- / ---


class MainPage(webapp.RequestHandler):
    def get(self):
        applink = ('/docedit', 'DocEdit Version %s' % docedit.__version__)
        self.response.out.write('<a href="%s">%s</a>' % applink)
        # [ ] make this link to action through function
        #     to avoid grepping when link changes

class DocEdit(webapp.RequestHandler):
    def get(self):
        # [ ] add debug messages
        self.response.out.write('<h4>documentation sources on this server</h4>\n')
        # [ ] or choose remote one
        self.response.out.write('<ul>')
        for link in docedit.listfiles():
            self.response.out.write('<li><a href="%s">%s</a></li>' % (link, link))
            # [ ] backurl function is needed
        self.response.out.write('</ul>')


urlmap = [
    ('/', MainPage),
    ('/docedit', DocEdit),
]

def main():
    app = webapp.WSGIApplication(urlmap, debug=True)
    run_wsgi_app(app)


if __name__ == '__main__':
    main()
