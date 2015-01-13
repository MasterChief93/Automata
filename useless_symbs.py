__author__ = 'MasterChief93'

def frombelow(term,nonterm,prod):
    #The FromBelow procedure eliminates the symbols which do not generate words
    newnonterm = []    #This array will contains all the non-terminal symbols which generate words
    for nterm in nonterm:
        for pro in prod:
            if nterm in pro[0]:
                if nterm not in newnonterm:   # If the symbol has a productions where it appears on the left hand side
                    newnonterm.append(nterm)  # that symbol can be included in the new non-terminal set of symbols
    # We can now eliminate all the productions in which compare symbols not included in the new non-terminal set of symbols
    for pro in prod:
        if pro[0] not in newnonterm + term:  # Both on the left hand side
            prod.remove(pro)
            continue
        for symb in pro[1]:
            if symb not in newnonterm + term and symb != "e": # and the right hand side (except epsilon)
                prod.remove(pro)
    return [term,newnonterm,prod]


def fromabove(term,nonterm,prod):
    # The FromAbove procedure eliminates all the symbols thare are unreachable from the start symbol S
    newterm = []        # We mantain two set. newterm will contains all the new terminals
    newnonterm = ["S"]  # while newnonterm will contains all the new non-terminals including S at the beginning
    for pro in prod:
        if pro[0] in newnonterm:
            for symb in pro[1]:
                if symb in nonterm and symb not in newnonterm: # If the symbols that the new non-terminal produce
                    newnonterm.append(symb)                    # belongs to the terminals, then we add it to the new set of non-terminals
                if symb in term and symb not in newterm:       # We do the same with the terminals
                    newterm.append(symb)
    # Now we have to eliminate all the productions that include symbols that are not included in the new sets
    newprod = []            # I wrote these 2 lines of code because if I modify "prod" then "newprod" see the changes
    newprod.extend(prod)
    for pro in newprod:
        if pro[0] not in newnonterm + newterm + ["e"]:
            prod.remove(pro)   # if the symbol generates new ones but this is not included in the new sets
            continue           # we can eliminate it (THERE'S NO NEED TO CHECK THE SYMBOLES THAT IT PRODUCES)
        for symb in pro[1]:
            if symb not in newnonterm + newterm + ["e"]:
                prod.remove(pro)      # if one of the symbols that the non-terminal produces is not include in the new sets
    return [newterm,newnonterm,prod]  # we can eliminate the production

def useless_symbs(term,nonterm,prod):
    # Useless Symbols simply calls the two precedent functions in order to apply the algorithm
    result = frombelow(term,nonterm,prod)
    return fromabove(result[0],result[1],result[2])
