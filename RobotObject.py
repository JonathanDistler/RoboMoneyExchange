#could create an object class with each having a special code that the other needs to verify to pass the crypto cost
#could also figure out how to link "bank accounts" to help the transfer between the robots 
#next step is to add functionality to make sure "transactions" are secure-could look into different cybersecurity protocols
class RecieverRobot:
    def __init__(self, name, account, reciever_id):
        self.name=name
        self.account_amount=account
        #private variable to help in future transactions, to make sure sender and reciever are accurate and no bad "actors" 
        self.__private_id=reciever_id
    #removes money from account based on cost of product
    def account_dec(self,decrease):
        self.account_amount-=decrease
    #returns name
    def robot_name (self):
        return(self.name)
    #returns account amount
    def account_amount(self):
        return(self.account_amount)

class SenderRobot:
    def __init__(self, name, service, service_cost, account,sender_id):
        self.name=name
        self.service=service
        self.service_cost=service_cost
        self.account_amount=account
        self.__private_id=sender_id

    #adds money to account based on how much product costs
    def account_add(self,increase):
        self.account_amount+=increase
    #returns name
    def robot_name(self):
        return(self.name)
    #returns the service of the robot, ie "cleaning"
    def robot_service(self):
        return(self.service)
    #returns the cost of the service, like an appraisal
    def service_cost(self):
        return(self.service_cost)
    #returns the account amount or balance of the sender
    def account_amount(self):
        return(self.account_amount)
    
#name, service action, the cost of the service, account amount, and id number (for future work verifiying transactions)

ex_sender_obj=SenderRobot("SoFi","Car Cleaning",250,0,21929)
ex_reciever_obj=RecieverRobot("SoFi2",500,43348)

#example of setup
service_cost=ex_sender_obj.service_cost
ex_sender_obj.account_add(service_cost)
sender_amount=ex_sender_obj.account_amount
print("Sender amount:",sender_amount)

ex_reciever_obj.account_dec(service_cost)
reciever_amount=ex_reciever_obj.account_amount
print("Reciever", reciever_amount)