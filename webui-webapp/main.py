"""
See app/README.rst for setup instructions
"""

import cgi
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

# --- docedit import and configuration ---
from app import docedit

docedit.DOCDIR = 'app/docs/'
docedit.DOCURL = '/static/docs/'
# --- / ---


TEMPLATES = os.path.join(os.path.dirname(__file__), 'templates')

def render(tpl, values):
    return template.render(os.path.join(TEMPLATES, tpl), values)


class MainPage(webapp.RequestHandler):
    def get(self):
        values = {
            'applink': '/docedit',
            'applink_text':'DocEdit Version %s' % docedit.__version__,
        }
        self.response.out.write(render('main.html', values))
        # [ ] main.html contains link to action that is better to generate
        #     to avoid grepping when link changes

class DocEdit(webapp.RequestHandler):
    def get(self):
        """
        Args:
          page: name of the page resource
        """
        # [ ] add debug messages
        pagename = self.request.get('page')
        values = {}
        if not pagename:
            # show index page
            # [ ] or choose remote one
            values = dict(
                title = 'documentation sources on this server',
                pagelist = docedit.listfiles(),
                # [ ] need backurl function
            )
        elif pagename not in docedit.listfiles():
            # show error page 
            # [ ] link to the code where the error occured
            values['error'] = 'invalid page name: %s' % cgi.escape(pagename)
        else:
            # show editor page
            # [ ] add unittests
            values['error'] = 'a sophisticated editor for %s' % cgi.escape(pagename)
        self.response.out.write(render('docedit.html', values))


urlmap = [
    ('/', MainPage),
    ('/docedit', DocEdit),
]

def main():
    app = webapp.WSGIApplication(urlmap, debug=True)
    run_wsgi_app(app)


if __name__ == '__main__':
    main()
