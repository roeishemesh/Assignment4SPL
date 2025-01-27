from asyncio.windows_events import NULL
from itertools import product
from persistence import *

import sys


def main(args : list[str]):
    # inputfilename : str = args[1]
    inputfilename : str = "actiontest.txt"
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            act = Activitie(splittedline[0],splittedline[1],splittedline[2],splittedline[3])
            act_quantity = int(act.quantity)
            if(act_quantity > 0):
                repo.products.update("quantity",act.quantity,act.product_id)
                repo.activitis.insert(act)
            elif(act_quantity < 0):
                product = repo.products.find(id = act.product_id)
                if(len(product) != 0):
                    if(product[0].quantity >= abs(act_quantity)):
                        repo.products.update("quantity",act.quantity,act.product_id)
                        repo.activitis.insert(act)
                





if __name__ == '__main__':
    main(sys.argv)
    