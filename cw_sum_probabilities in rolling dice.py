import itertools
def rolldice_sum_prob(sum_,dice_amount):
    den=6**dice_amount+0.0
    L=[range(1,7)]*dice_amount
    combos=itertools.product(*L)
    main=[x for x in combos if sum(x)==sum_]
    return len(main)/den
    
