class RecieverRobot:
    #defines functions for accessing robot name, account amount, as well as paying for service 
    #now, I need to implement different service types
    #next step would be converting prices into crypto currency amounts
    #could also have a running total of the sum
    def __init__(self, name, account, reciever_id):
        self._name = name
        self._account_amount = account
        self.__private_id = reciever_id
        self._transactions=[]

    def account_dec(self, decrease):
        self._account_amount -= decrease

    def robot_name(self):
        return self._name

    def account_amount(self):
        return self._account_amount


class SenderRobot:
    #defines functions fo raccessing robot name, service, and account amount
    #could change the function so the other has to have more than enough money
    #might need a check function to make sure the other is the correct one, too
    def __init__(self, name, service, service_cost, account, sender_id):
        self._name = name
        self.service = service
        self._service_cost = service_cost
        self._account_amount = account
        self.__private_id = sender_id
        self._recieved_transactions=[]

    def account_add(self, increase):
        self._account_amount += increase

    def robot_name(self):
        return self._name

    def robot_service(self):
        return self.service

    def service_cost(self):
        return self._service_cost

    def account_amount(self):
        return self._account_amount

    def trade(self, robotObj, name):
        if name == robotObj.robot_name():
            cost = self.service_cost()
            self.account_add(cost)
            robotObj.account_dec(cost)
            service=self.robot_service()
            self._recieved_transactions.append([cost,service])
            robotObj._transactions.append([-cost,service])


# Example of usage
ex_sender_obj = SenderRobot("SoFi", "Car Cleaning", 250, 0, 21929)
ex_reciever_obj = RecieverRobot("SoFi2", 500, 43348)

ex_sender_obj.trade(ex_reciever_obj, "SoFi2")

print("Receiver amount:", ex_reciever_obj.account_amount())
print("Sender amount:", ex_sender_obj.account_amount())
