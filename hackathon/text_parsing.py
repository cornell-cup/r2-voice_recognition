import language_check

class Text_Parsing:
  def fix_grammar(text):
    tool = language_check.LanguageTool('en-GB')
    matches = tool.check(text)
    return language_check.correct(text, matches)
