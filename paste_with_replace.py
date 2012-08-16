import sublime
import sublime_plugin
import re

from titlecase import titlecase

class PromptPasteWithReplaceCommand(sublime_plugin.WindowCommand):

    def get_last(self, key, default=''):

        view = self.window.active_view()

        if not view:
            return default

        return view.settings().get('paste_with_replace.last_' + key, default)

    def set_last(self, key, value):

        view = self.window.active_view()

        if (view):
            view.settings().set('paste_with_replace.last_' + key, value)

    def get_input(self, prompt, default, on_done):
        input_view = self.window.show_input_panel(prompt, default, on_done, None, None)
        input_view.sel().clear()
        input_view.sel().add(sublime.Region(0, input_view.size()))

    def run(self):
        self.get_input("Find:", self.get_last('find_text'), self.on_find_prompt_done)

    def on_find_prompt_done(self, text):
        self.find_text = text
        self.get_input("Replace With:", self.get_last('replace_text'), self.on_replace_prompt_done)

    def on_replace_prompt_done(self, text):

        self.set_last('find_text', self.find_text)
        self.set_last('replace_text', text)

        if self.window.active_view():
            self.window.active_view().run_command("paste_with_replace", {"find_text": self.find_text, "replace_text": text})


class PasteWithReplaceCommand(sublime_plugin.TextCommand):

    def handle_replace(self, m):

        found = m.group(0)

        if (found.upper() == found):
            return self.replace_text.upper()
        elif (found.lower() == found):
            return self.replace_text.lower()
        elif (titlecase(found) == found):
            return titlecase(self.replace_text)
        else:
            return self.replace_text

    def run(self, edit, find_text, replace_text):

        view = self.view
        text = sublime.get_clipboard()
        #edit = view.begin_edit()

        self.find_text = find_text
        self.replace_text = replace_text

        regex = re.compile(re.escape(find_text), re.IGNORECASE)
        text = regex.sub(self.handle_replace, text)

        for sel in view.sel():
            # Insert contents of clipboard
            view.replace(edit, sel, text)

        #view.end_edit(paste_edit)
