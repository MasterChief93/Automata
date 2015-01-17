__author__ = 'MasterChief93'
from useless_symbs import useless_symbs

def e_prod_elim(term,nonterm,prod):
    null = [0]*len(nonterm) # sets of nullable symbols
    for nterm in nonterm:
        count = 0
        for pro in prod:     # We count how many production that non-terminal has
            if pro[0] == nterm:
                count += 1
        if count == 1 and [nterm,"e"] in prod: # if it has only one production and that production is epsilon
            null[nonterm.index(nterm)] = 1     # it is a nullable symbol
    for pro in prod:           # for the symbols produced
        for symb in pro[1]:
            if symb in nonterm:   #if that symbols are non-terminals
                if null[nonterm.index(symb)] == 1:  #if that symbols are nullable
                    pro[1] = pro[1].replace(symb,"")  # we can replace their presence with an epsilon-string (empty)
    for pro in prod:
        if pro[1] == "":   # if a production is an empty (all the symbols produced were nullable)
            null[nonterm.index(pro[0])] = 1  # that symbol is nullable too
    if null[nonterm.index("S")] == 1 and ["S","e"] not in prod:   # if S is nullable, we add ['S','e'] to productions
        prod.append(["S","e"])
    newprod = []
    for pro in prod:
        if not((pro[1] == "e" or pro[1] == "") and pro != ["S","e"]): # if the symbol is not nullable and the production
            newprod.append(pro)                                        # is differente from ['S','e'] than we can add it
    # tempprod = []                                                       # to the new set of productions
    # tempprod.extend(newprod)
    # for pro in tempprod:
    #     if pro[0] not in term + nonterm:
    #         newprod.remove(pro)
    #         continue
    #     for symb in pro[1]:
    #         if symb not in term + nonterm + ["e"]:
    #             newprod.remove(pro)
    return useless_symbs(term,nonterm,newprod)
