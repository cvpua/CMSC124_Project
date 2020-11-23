import re
import tkinter
from tkinter.filedialog import askopenfilename


class Lol:
      token_expressions = [
        (r"^HAI\s", "Code Delimiter"),
        (r"^KTHXBYE\s|^KTHXBYE$", "Code Delimiter"),
        (r"^BTW\s", "Comment Identifier"),
        (r"^OBTW\s", "Multilinecomment Delimiter"),
        (r"^TLDR\s", "Multilinecomment Delimiter"),
        (r"^I HAS A\s", "Variable Declaration"),
        (r"^ITZ\s", "Variable Assignment"),
        (r"^R\s", "KEYWORD"),
        (r"^SUM OF\s", "Addition Keyword"),
        (r"^DIFF OF\s", "Subtraction Keyword"),
        (r"^PRODUKT OF\s", "Multiplication Keyword"),
        (r"^QUOSHUNT OF\s", "Subtraction Keyword"),
        (r"^MOD OF\s", "Modulo Keyword"),
        (r"^BIGGR OF\s", "Max Keyword"),
        (r"^SMALLR OF\s", "Min Keyword"),
        (r"^BOTH OF\s", "And Keyword"),
        (r"^EITHER OF\s", "Or Keyword"),
        (r"^WON OF\s", "Xor Keyword"),
        (r"^NOT\s", "Not Keyword"),
        (r"^ANY OF\s", "KEYWORD"),
        (r"^ALL OF\s", "KEYWORD"),
        (r"^BOTH SAEM\s", "Comparison == Keyword"),
        (r"^DIFFRINT\s", "Comparison != Keyword"),
        (r"^SMOOSH\s", "String Concatenation Keyword"),
        (r"^MAEK\s", "KEYWORD"),
        (r"^A\s", "KEYWORD"),
        (r"^IS NOW A\s", "KEYWORD"),
        (r"^VISIBLE\s", "Output Keyword"),
        (r"^GIMMEH\s", "Input Keyword"),
        (r"^O RLY\?\s", "If-else Delimiter"),
        (r"^YA RLY\s", "If Delimiter"),
        (r"^MEBBE\s", "Elif Delimiter"),
        (r"^NO WAI\s", "Else Delimiter"),
        (r"^OIC\s", "If-else Delimiter or Switch Delimiter"),
        (r"^WTF\?\s", "Switch Delimiter"),
        (r"^OMG\s", "Case Delimiter"),
        (r"^OMGWTF\s", "Default Case Delimiter"),
        (r"^IM IN YR\s", "KEYWORD"),
        (r"^UPPIN\s", "KEYWORD"),
        (r"^NERFIN\s", "KEYWORD"),
        (r"^YR\s", "KEYWORD"),
        (r"^TIL\s", "KEYWORD"),
        (r"^WILE\s", "KEYWORD"),
        (r"^IM OUTTA YR\s", "KEYWORD"),
        (r"^(-?[0-9]+)\s", "Numbr Literal"),
        (r"^(-)?[0-9]*(\.)[0-9]+\s", "Numbar Literal"),
        (r"^\".+\"\s", "Yarn Literal"),
        (r"^(WIN|FAIL)\s", "Troof Literal"),
        (r"^(NOOB|NUMBR|NUMBAR|YARN|TROOF)\s", "Type Literal"),
        (r"^[a-zA-Z][a-zA-Z0-9_]*\s", "Variable Identifier"),
      ]

      tokens = []



      def readFile(self):
        filename = askopenfilename()
        file = open(filename,'r')
        self.text = file.read()

      def printTokens(self):
        for i in range(len(self.tokens)):
              print(self.tokens[i][0] + " \t" + self.tokens[i][1] )


      def lex(self):
        tokens = self.tokens
        text = self.text
        token_expressions = self.token_expressions

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
                tokens.append([match.group(0)[:-1],tag])
                line = line[match.end(0):]
                break
            else:
              print(f"Error in line number {line_number}; Invalid token")
              return
          line_number += 1
        return tokens

      
      
lol = Lol()
lol.readFile()
lol.lex()
lol.printTokens()
