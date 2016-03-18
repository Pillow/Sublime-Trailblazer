import sublime, sublime_plugin
from .pathmaker import *

class TrailBlazerCommand(sublime_plugin.TextCommand):
  def get_selected_text(self):
    view = self.view
    s = ""
    for region in view.sel():
      s += (view.substr(region))

    return s

  def run(self, edit, **args):
    if args and args['extension']:
      selected_text = self.get_selected_text() + args['extension']
    else:
      selected_text = self.get_selected_text()

    file = makeFilePath(self.view.file_name(), selected_text)
    self.view.window().open_file(file)