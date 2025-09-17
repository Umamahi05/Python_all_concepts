#Encapsulation
class Order:
    def __init__(self,custname,items,total_amt,discount):
        self.customername = custname
        self.citems = items
        self.__totalamt = total_amt
        self.__discount = discount

    def __calc_final(self):
        return self.__totalamt - self.__discount
    
    def _get_admin_view(self): #protected method
        return {
            "Cust" : self.customername,
            "Items" : self.citems,
            "Total Amount" : self.__totalamt,
            "Discount" : self.__discount,
            "Final Bill" : f"{self.__calc_final()}"
        }
    
    def customer_view(self): #public method
        return {
            "Cust" : self.customername,
            "Items" : self.citems,
            "Final Bill" : f"{self.__calc_final()}"
        }
    
class AdminPortal():
    def show_order(self,order):
        return order._get_admin_view()
    
class CustomerApp():
    def show_order(self,order):
        return order.customer_view()
    
pobj = Order("AAA",["pizza","burger"],1040.0,200)
ap = AdminPortal()
ca = CustomerApp()

print(ap.show_order(pobj))
print(ca.show_order(pobj))




