TOK_EXP = [
    (r"^HAI\s", "HAI_KEYWORD"),
    (r"^KTHXBYE\s|^KTHXBYE$", "KTHXBYE_KEYWORD"),
    (r"^BTW\s", "BTW_KEYWORD"),
    (r"^OBTW\s", "OBTW_KEYWORD"),
    (r"^TLDR\s", "TLDR_KEYWORD"),
    (r"^I HAS A\s", "I_HAS_A_KEYWORD"),
    (r"^ITZ\s", "ITZ_KEYWORD"),
    (r"^R\s", "R_KEYWORD"),
    (r"^SUM OF\s", "SUM_OF_KEYWORD"),
    (r"^DIFF OF\s", "DIFF_OF_KEYWORD"),
    (r"^PRODUKT OF\s", "PRODUKT_OF_KEYWORD"),
    (r"^QUOSHUNT OF\s", "QUOSHUNT_OF_KEYWORD"),
    (r"^MOD OF\s", "MOD_OF_KEYWORD"),
    (r"^BIGGR OF\s", "BIGGR_OF_KEYWORD"),
    (r"^SMALLR OF\s", "SMALLR_OF_KEYWORD"),
    (r"^BOTH OF\s", "BOTH_OF_KEYWORD"),
    (r"^EITHER OF\s", "EITHER_OF_KEYWORD"),
    (r"^WON OF\s", "WON_OF_KEYWORD"),
    (r"^NOT\s", "NOT_KEYWORD"),
    (r"^ANY OF\s", "ANY_OF_KEYWORD"),
    (r"^ALL OF\s", "ALL_OF_KEYWORD"),
    (r"^BOTH SAEM\s", "BOTH_SAEM_KEYWORD"),
    (r"^DIFFRINT\s", "DIFFRINT_KEYWORD"),
    (r"^SMOOSH\s", "SMOOSH_KEYWORD"),
    (r"^MAEK\s", "MAEK_KEYWORD"),
    (r"^A\s", "A_KEYWORD"),
    (r"^IS NOW A\s", "IS_NOW_A_KEYWORD"),
    (r"^VISIBLE\s", "VISIBLE_KEYWORD"),
    (r"^GIMMEH\s", "GIMMEH_KEYWORD"),
    (r"^O RLY\?\s", "O_RLY?_KEYWORD"),
    (r"^YA RLY\s", "YA_RLY_KEYWORD"),
    (r"^MEBBE\s", "MEBBE_KEYWORD"),
    (r"^NO WAI\s", "NO_WAI_KEYWORD"),
    (r"^OIC\s", "OIC_KEYWORD"),
    (r"^WTF\?\s", "WTF?_KEYWORD"),
    (r"^OMG\s", "OMG_KEYWORD"),
    (r"^OMGWTF\s", "OMGWTF_KEYWORD"),
    (r"^IM IN YR\s", "IM_IN_YR_KEYWORD"),
    (r"^UPPIN\s", "UPPIN_KEYWORD"),
    (r"^NERFIN\s", "NERFIN_KEYWORD"),
    (r"^YR\s", "YR_KEYWORD"),
    (r"^TIL\s", "TIL_KEYWORD"),
    (r"^WILE\s", "WILE_KEYWORD"),
    (r"^IM OUTTA YR\s", "IM_OUTTA_YR_KEYWORD"),
    (r"^IT\s", "IT_KEYWORD"),
    (r"^(-?[0-9]+)\s", "NUMBR_LITERAL"),
    (r"^(-)?[0-9]*(\.)[0-9]+\s", "NUMBAR_LITERAL"),
    (r"^\".+\"\s", "YARN_LITERAL"),
    (r"^(WIN|FAIL)\s", "TROOF_LITERAL"),
    (r"^(NOOB|NUMBR|NUMBAR|YARN|TROOF)\s", "TYPE_LITERAL"),
    (r"^[a-zA-Z][a-zA-Z0-9_]*\s", "VAR_IDENTIFIER"),
  ]