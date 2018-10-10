import sublime
import sublime_plugin

class PromptSurrounderCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Surround by:", "", self.on_done, None, None)

    def on_done(self, tag):
        try:
            if self.window.active_view():
                self.window.active_view().run_command("surround_by", {"tag": tag})
        except ValueError:
            print('hi')


class SurroundByCommand(sublime_plugin.TextCommand):
	def run(self, edit, tag):
		for region in self.view.sel():
			text = self.view.substr(region)
			self.view.replace(edit,region,"<"+tag+">"+text+"</"+tag.split()[0]+">")

