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
    result = e_prod_elim(term,nonterm,prod) # this algorithm work only with grammar without epsilon-productions
    term = result[0]
    nonterm = result[1]
    prod = result[2]
    # We create the queue where we put (in any order) all the non-trivial unit-productions in the grammar
    queue = []
    while True:
        prod = trivial(prod) # elimination of all trivial productions
        for pro in prod:
            if len(pro[0]) == len(pro[1]) == 1 and pro[0] in nonterm and pro[1] in nonterm:
                if pro not in queue:
                    queue.append(pro) # we can add to the queue the new unit-production
        if len(queue) == 0:
            return useless_symbs(term,nonterm,prod)
        # Then we pop the first one
        selected_prod = queue[0]
        # and reduce the queue
        queue = queue[1:]
        tempprod = []
        tempprod.extend(prod)
        for pro in tempprod:
            if pro == selected_prod:
                for pro2 in tempprod:  # Replacement of the symbol produced in the unit-production with its productions
                    if pro[1] == pro2[0] and [pro[0],pro2[1]] not in prod:
                        prod.append([pro[0],pro2[1]])
                prod.remove(selected_prod) # We can now remove that unit-production from productions
        # Elimination of every trivial unit-production occurred
        prod = trivial(prod)
        # The cicle end when the queue is empty
        if queue == []:
            break
    # Elimination of every useless-symbols occured and return
    return useless_symbs(term,nonterm,prod)


# term = ["+","x",'(',')','a']
# nonterm = ["S","T","F"]
# prod = [["S","S+T"],["S","T"],["T","TxF"],["T","F"],["F","(S)"],["F","a"]]
#
# unitprod(term,nonterm,prod)


