class RecieverRobot:
    #defines functions for accessing robot name, account amount, as well as paying for service 
    #could also add logs of which services were provided and how much they cost, as well as different service types
    def __init__(self, name, account, reciever_id):
        self._name = name
        self._account_amount = account
        self.__private_id = reciever_id

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


# Example of usage
ex_sender_obj = SenderRobot("SoFi", "Car Cleaning", 250, 0, 21929)
ex_reciever_obj = RecieverRobot("SoFi2", 500, 43348)

ex_sender_obj.trade(ex_reciever_obj, "SoFi2")

print("Receiver amount:", ex_reciever_obj.account_amount())
print("Sender amount:", ex_sender_obj.account_amount())
