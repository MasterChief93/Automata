__author__ = 'MasterChief93'
from useless_symbs import useless_symbs

def e_prod_elim(term,nonterm,prod):
    null = [0]*len(nonterm)
    for nterm in nonterm:
        count = 0
        for pro in prod:
            if pro[0] == nterm:
                count += 1
        if count == 1 and [nterm,"e"] in prod:
            null[nonterm.index(nterm)] = 1
    for pro in prod:
        for symb in pro[1]:
            if symb in nonterm:
                if null[nonterm.index(symb)] == 1:
                    pro[1] = pro[1].replace(symb,"")
    for pro in prod:
        if pro[1] == "":
            null[nonterm.index(pro[0])] = 1
    if null[nonterm.index("S")] == 1 and ["S","e"] not in prod:
        prod.append(["S","e"])
    newprod = []
    for pro in prod:
        if not((pro[1] == "e" or pro[1] == "") and pro != ["S","e"]):
            newprod.append(pro)
    tempprod = []
    tempprod.extend(newprod)
    for pro in tempprod:
        if pro[0] not in term + nonterm:
            newprod.remove(pro)
            continue
        for symb in pro[1]:
            if symb not in term + nonterm + ["e"]:
                newprod.remove(pro)
    return useless_symbs(term,nonterm,newprod)