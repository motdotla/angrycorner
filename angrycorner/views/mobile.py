from angrycorner import app
from angrycorner.views.common import load_template, layout

class MobileViews():
  def draw_index(self):
    form_html = load_template('mobile/index.html', {})

    return layout({'body_content' : form_html })

  def draw_result(self):
    form_html = load_template('mobile/result.html', {})

    return layout({'body_content' : form_html })
