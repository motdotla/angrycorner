from angrycorner import app
from angrycorner.views.common import load_template, layout

class IndexViews():
  """ Views for Index """

  def draw_index(self):
    """ draw_index """

    form_html = load_template('index/index.html', {})

    return layout({'body_content' : form_html })
