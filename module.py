from textblob import TextBlob
from language_tool_python import LanguageTool


class SpellCheckerModule:

    def __init__(self):
        self.grammar_tool = LanguageTool('en-US')

    def correct_spell(self, text):
        corrected_text = str(TextBlob(text).correct())
        return corrected_text

    def correct_grammar(self, text):
        matches = self.grammar_tool.check(text)
        corrected_text = self.grammar_tool.correct(text)
        mistakes_count = len(matches)

        return corrected_text, mistakes_count
