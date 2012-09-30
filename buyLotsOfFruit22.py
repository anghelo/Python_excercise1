fruitPrices = {'appels':2.0,'oranges':1.5,'pears':1.75,'limes':1.75,'strawberries':1.0}

def buyLotsOfFruit(orderList):
 
    totalCost=0.0
    for fruit,quantity in orderList:
         cost1 = existFruit(fruit)
         if cost1 != None:
             totalCost += cost1 * quantity
            
    return totalCost


def existFruit(fruit):

    if fruit not in fruitPrices:
       print "Error we don't have %s"  % (fruit)
       return None
    return fruitPrices[fruit]

if __name__=='__main__':
   orderList = [('appels',2.0),('pears',3.0),('limes',4.0)]
   print 'Cost of',orderList,'is',buyLotsOfFruit(orderList)
