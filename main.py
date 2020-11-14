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
    itz_keyword = '^ITZ$'
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
            yarn_result = re.search(self.yarn_literal,content[i])
            
            if(yarn_result):
                result = yarn_result.group()
                print(result[1:len(result)-1])



code = Lol()
code.scanFIle()
code.classify()