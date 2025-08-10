#could create an object class with each having a special code that the other needs to verify to pass the crypto cost
class RecieverRobot:
    def __init__(self, name, account, reciever_id):
        self.name=name
        self.account_amount=account
        self.__private_id=reciever_id

    def account_dec(self,decrease):
        self.account_amount-=decrease

    def robot_name (self):
        return(self.name)
    
    def account_amount(self):
        return(self.account_amount)

class senderRobot:
    def __init__(self, name, service, service_cost, account,sender_id):
        self.name=name
        self.service=service
        self.service_cost=service_cost
        self.account_amount=account
        self.__private_id=sender_id

    def account_add(self,increase):
        self.account_amount+=increase

    def robot_name(self):
        return(self.name)
    
    def robot_service(self):
        return(self.service)
    
    def service_cost(self):
        return(self.service_cost)
    
    
