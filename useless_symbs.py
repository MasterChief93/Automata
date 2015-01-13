__author__ = 'MasterChief93'

def frombelow(term,nonterm,prod):
    newnonterm = []
    for nterm in nonterm:
        for pro in prod:
            if nterm in pro[0]:
                if nterm not in newnonterm:
                    newnonterm.append(nterm)

    for pro in prod:
        if pro[0] not in newnonterm + term:
            prod.remove(pro)
            continue
        for symb in pro[1]:
            if symb not in newnonterm + term and symb != "e":
                prod.remove(pro)
    return[term,newnonterm,prod]


def fromabove(term,nonterm,prod):
    newterm = []
    newnonterm = ["S"]
    for pro in prod:
        if pro[0] in newnonterm:
            for symb in pro[1]:
                if symb in nonterm and symb not in newnonterm:
                    newnonterm.append(symb)
                if symb in term and symb not in newterm:
                    newterm.append(symb)
    newprod = []
    newprod.extend(prod)
    for pro in newprod:
        if pro[0] not in newnonterm + newterm + ["e"]:
            prod.remove(pro)
            continue
        for symb in pro[1]:
            if symb not in newnonterm + newterm + ["e"]:
                prod.remove(pro)
    return [newterm,newnonterm,prod]

def useless_symbs(term,nonterm,prod):
    result = frombelow(term,nonterm,prod)
    return fromabove(result[0],result[1],result[2])
