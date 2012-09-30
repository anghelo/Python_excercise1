import shop


def shopSmart(orderList,fruitShop):
     less=99999.0;
     fruitShopLess = fruitShop[0]
     for shopp in fruitShop:
        cost = shopp.getPriceOfOrder(orderList)
        if cost < less:
            fruitShopLess = shopp
            less=cost 
        
     return  fruitShopLess



if __name__=='__main__':

    
    orders1 =[('apples',1.0),('oranges',3.0)]
    orders2 = [('apples',3.0)]
    dir1 = {'apples':2.0,'oranges':1.0}
    shop1 = shop.FruitShop('shop1',dir1)
    dir2 = {'apples':1.0,'oranges':5.0}
    shop2 = shop.FruitShop('shop2',dir2)
    shops=[shop1,shop2]
    print "For orders",orders1,",the best shop is",shopSmart(orders1,shops).getName()
    print "For orders",orders2,",the best shop is",shopSmart(orders2,shops).getName()