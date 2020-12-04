import re

from classes.Token import Token

class Lexer:
  def __init__(self, text, TOK_EXP):
    self.text = text
    self.token_expressions = TOK_EXP

  def tokenize(self):
    tokens = [] 
    lines = self.text.split("\n")
    line_number = 1
    for line in lines:
      line = line.strip()
      line = line + "\n"
      while (line != "" and line != "\n"):
        for token_exp in self.token_expressions:
          pattern, tag = token_exp
          match = re.match(pattern, line)
          if (match):
            if(tag == 'YARN_LITERAL'):
              name = match.group(0)[1:-2]
            else:
              name = match.group(0)[:-1]
            tokens.append(
                Token(name,tag, line_number)
              )
            line = line[match.end(0):]
            break
        else:
          raise Exception(f"Error in line number {line_number}: Invalid token")
      tokens.append(Token("\\n", "LINEBREAK", line_number))
      line_number += 1
    return tokens