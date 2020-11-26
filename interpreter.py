import re

token_expressions = [
  (r"^HAI\s", "KEYWORD"),
  (r"^KTHXBYE\s|^KTHXBYE$", "KEYWORD"),
  (r"^BTW\s", "KEYWORD"),
  (r"^OBTW\s", "KEYWORD"),
  (r"^TLDR\s", "KEYWORD"),
  (r"^I HAS A\s", "KEYWORD"),
  (r"^ITZ\s", "KEYWORD"),
  (r"^R\s", "KEYWORD"),
  (r"^SUM OF\s", "KEYWORD"),
  (r"^DIFF OF\s", "KEYWORD"),
  (r"^PRODUKT OF\s", "KEYWORD"),
  (r"^QUOSHUNT OF\s", "KEYWORD"),
  (r"^MOD OF\s", "KEYWORD"),
  (r"^BIGGR OF\s", "KEYWORD"),
  (r"^SMALLR OF\s", "KEYWORD"),
  (r"^BOTH OF\s", "KEYWORD"),
  (r"^EITHER OF\s", "KEYWORD"),
  (r"^WON OF\s", "KEYWORD"),
  (r"^NOT\s", "KEYWORD"),
  (r"^ANY OF\s", "KEYWORD"),
  (r"^ALL OF\s", "KEYWORD"),
  (r"^BOTH SAEM\s", "KEYWORD"),
  (r"^DIFFRINT\s", "KEYWORD"),
  (r"^SMOOSH\s", "KEYWORD"),
  (r"^MAEK\s", "KEYWORD"),
  (r"^A\s", "KEYWORD"),
  (r"^IS NOW A\s", "KEYWORD"),
  (r"^VISIBLE\s", "KEYWORD"),
  (r"^GIMMEH\s", "KEYWORD"),
  (r"^O RLY\?\s", "KEYWORD"),
  (r"^YA RLY\s", "KEYWORD"),
  (r"^MEBBE\s", "KEYWORD"),
  (r"^NO WAI\s", "KEYWORD"),
  (r"^OIC\s", "KEYWORD"),
  (r"^WTF\?\s", "KEYWORD"),
  (r"^OMG\s", "KEYWORD"),
  (r"^OMGWTF\s", "KEYWORD"),
  (r"^IM IN YR\s", "KEYWORD"),
  (r"^UPPIN\s", "KEYWORD"),
  (r"^NERFIN\s", "KEYWORD"),
  (r"^YR\s", "KEYWORD"),
  (r"^TIL\s", "KEYWORD"),
  (r"^WILE\s", "KEYWORD"),
  (r"^IM OUTTA YR\s", "KEYWORD"),
  (r"^(-?[0-9]+)\s", "NUMBR_LITERAL"),
  (r"^(-)?[0-9]*(\.)[0-9]+\s", "NUMBAR_LITERAL"),
  (r"^\".+\"\s", "YARN_LITERAL"),
  (r"^(WIN|FAIL)\s", "TROOF_LITERAL"),
  (r"^(NOOB|NUMBR|NUMBAR|YARN|TROOF)\s", "TYPE_LITERAL"),
  (r"^[a-zA-Z][a-zA-Z0-9_]*\s", "IDENTIFIER"),
]

def lex(text, token_expressions):
  tokens = {}
  
  lines = text.split("\n")
  line_number = 1
  for line in lines:
    line = line.strip()
    line = line + "\n"
    while (line != "" and line != "\n"):
      for token_exp in token_expressions:
        pattern, tag = token_exp
        match = re.match(pattern, line)
        if (match):
          if (tokens.get(match.group(0)[:-1]) == None):
            tokens.update({match.group(0)[:-1]: tag})
          line = line[match.end(0):]
          print(tokens)
          break
      else:
        print(f"Error in line number {line_number}; Invalid token")
        return
    line_number += 1
  return tokens

file = open("input.lol", "r")
text = file.read()

print(lex(text, token_expressions))