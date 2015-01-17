__author__ = 'MasterChief93'
from epsilon_prods import e_prod_elim

def chomsky(term,nonterm,prod):
    result = e_prod_elim(term,nonterm,prod)
    terms = result[0]
    nonterms= result[1]
    prods = result[2]
    W = []
    W.extend(nonterms)
    R = []
    for pro in prods:
        if pro != ['S','e']:
            R.append(pro)

