__author__ = 'MasterChief93'
from epsilon_prods import e_prod_elim
from useless_symbs import useless_symbs

def trivial(prod):
    newprod = []
    for pro in prod:
        if pro[0] != pro[1]:
            newprod.append(pro)
    return newprod

def unitprod(term,nonterm,prod):
    result = e_prod_elim(term,nonterm,prod)
    term = result[0]
    nonterm = result[1]
    prod = result[2]
    queue = []
    while True:
        prod = trivial(prod)

        for pro in prod:
            if pro[0] != pro[1] and len(pro[0]) == len(pro[1]) == 1 and pro[0] in nonterm and pro[1] in nonterm:
                if pro not in queue:
                    queue.append(pro)
        selected_prod = queue[0]
        queue = queue[1:]
        tempprod = []
        tempprod.extend(prod)
        for pro in tempprod:
            if pro == selected_prod:
                for pro2 in tempprod:
                    if pro[1] == pro2[0] and [pro[0],pro2[1]] not in prod:
                        prod.append([pro[0],pro2[1]])
                prod.remove(selected_prod)
        prod = trivial(prod)
        if queue == []:
            break
    print useless_symbs(term,nonterm,prod)


term = ["a","b"]
nonterm = ["S","A","B"]
prod = [["S","AS"],["S","A"],["A","a"],["A","B"],["B","b"],["B","S"],["B","A"]]

unitprod(term,nonterm,prod)