import re

class Lol:

    variable_identifier = '\\b[a-zA-Z][a-zA-Z0-9_]*\\b'
    function_identifier = '^[a-zA-Z][a-zA-Z0-9_]*$'
    loop_identifier = '^[a-zA-Z][a-zA-Z0-9_]*$'
 
    numbr_literal = '^(-?[0-9]+)$'
    numbar_literal = '^(-)?[0-9]*(\.)[0-9]+$'
    yarn_literal = '\"[^\"]*\"'
    troof_literal = '^(WIN|FAIL)$' 
    type_literal = '^(NOOB|NUMBR|NUMBAR|YARN|TROOF)$'

    hai_keyword = '\\bHAI\\b'
    kthxbye_keyword = '\\bKTHXBYE\\b'
    btw_keyword = '^BTW$'
    obtw_keyword = '^OBTW$'
    tldr_keyword = '^TLDR$'
    iHasA_keyword = '\\bI HAS A\\b' 
    itz_keyword = '\\bITZ\\b'
    r_keyword = '^R$'
    sumOf_keyword = '^SUM OF$'
    diffOf_keyword = '^DIFF OF$'
    produktOf_keyword = '^PRODUKT OF'
    quoshntOf_keyword = '^QUOSHUNT OF$'
    modOf_keyword = '^MOD OF$'
    biggrOf_keyword = '^BIGGR OF$'
    smallrOf_keyword = '^SMALLR OF$' 
    bothOf_keyword = '^BOTH OF$'
    eitherOf_keyword = '^EITHER OF$'
    wonOf_keyword = '^WON O$'
    not_keyword = '^NOT$'
    anyOf_keyword = '^ANY OF$'
    allOf_keyword = '^ALL OF$'
    bothSaem_keyword = '^BOTH SAEM$'
    diffrint_keyword = '^DIFFRINT$'
    smoosh_keyword = '^SMOOSH$'
    maek_keyword = '^MAEK$'
    a_keyword = '^A$'
    isNowA_keyword = '^IS NOW A$'
    visible_keyword = '\\bVISIBLE\\b'
    gimmeh_keyword = '^GIMMEH$'
    oRly_keyword = '^O RLY?$'
    yaRly_keyword = '^YA RLY$'
    mebbe_keyword = '^MEBBE$'
    noWai_keyword = '^NO WAI$'
    oic_keyword = '^OIC$'
    wtf_keyword = '^WTF?$'
    omg_keyword = '^OMG$'
    omgWtf_keyword = '^OMGWTF$'
    imInYr_keyword = '^IM IN YR$'
    uppin_keyword = '^UPPIN$'
    nerfin_keyword = '^NERFIN$'
    yr_keyword = '^YR$'
    til_keyword = '^TIL$'
    wile_keyword = '^WILE$'
    imOuttaYr_keyword = '^IM OUTTA YR$'

    quote_delimiter = '\"'

    symbol_table = []
    lexeme_table = {}

    def scanFIle(self):
        file = open('input.lol','r')
        self.content = file.read().split('\n')
        
    
    def classify(self):
        content = self.content
        for i in range(len(content)):
            hai_result = re.search(self.hai_keyword,content[i])
            iHasA_result = re.search(self.iHasA_keyword,content[i])
            itz_result = re.search(self.itz_keyword,content[i])
            visible_result = re.search(self.visible_keyword,content[i])
            kthx_result = re.search(self.kthxbye_keyword,content[i])
            
            # HAI
            if(hai_result):
                print(hai_result.group())
            
            # I HAS A
            if(iHasA_result): 
                print(iHasA_result.group())
                var_word = content[i].split()
                var_word = var_word[3:]
                var_word = " ".join(var_word)
                
                # var
                var_result = re.search(self.variable_identifier,var_word)
                if(var_result):
                    print(var_result.group())

                    val_declaration = var_word.split()
                    val_declaration = val_declaration[1:]
                    val_declaration = " ".join(val_declaration)
                    
                    # ITZ
                    itz_result = re.search(self.itz_keyword,val_declaration)
                    if(itz_result):
                        print(itz_result.group())

                        value = val_declaration.split()
                        value = value[1:]
                        value = " ".join(value)
                        
                        # 12
                        numbr_result = re.search(self.numbr_literal,value)
                        numbar_result = re.search(self.numbar_literal,value)
                        yarn_result = re.search(self.yarn_literal,value)
                        troof_result = re.search(self.troof_literal,value)
                        type_result = re.search(self.type_literal,value)
                        
                        if(numbr_result):
                            print(numbr_result.group())
                        if(numbar_result):
                            print(numbar_result.group())
                        if(yarn_result):
                            print(yarn_result.group())
                        if(troof_result):
                            print(troof_result.group())
                        if(type_result):
                            print(type_result.group())
            # VISIBLE
            if(visible_result):
                print(visible_result.group())

                value = content[i].split()
                value = value[1:]
                value = " ".join(value)
                # Naka while kasi pwedeng magprint ng multiple variables
                while(value):    
                    numbr_result = re.search(self.numbr_literal,value)
                    numbar_result = re.search(self.numbar_literal,value)
                    yarn_result = re.search(self.yarn_literal,value)
                    troof_result = re.search(self.troof_literal,value)
                    type_result = re.search(self.type_literal,value)
                    var_result = re.search(self.variable_identifier,var_word)
                    
                    if(numbr_result):
                        print(numbr_result.group())
                    if(numbar_result):
                        print(numbar_result.group())
                    if(yarn_result):
                        string_literal = yarn_result.group()
                        print(string_literal[0])
                        print(string_literal[1:-1])
                        print(string_literal[-1])
                    if(troof_result):
                        print(troof_result.group())
                    if(type_result):
                        print(type_result.group())
                    if(var_result):
                        print(var_result.group())

                    
                    value = value.split()
                    value = value[1:]
                    if value:
                        value = None
                    else:    
                        value = " ".join(value)
            
            # KTHXBYE
            if(kthx_result):
                print(kthx_result.group())
                    
                    
                    


code = Lol()
code.scanFIle()
code.classify()