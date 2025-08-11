#Goal of this code is a weighted priority for choosing a robot to do a task
import numpy as np
import random
class RecieverRobot:
    #defines functions for accessing robot name, account amount, as well as paying for service 
    #now, I need to implement different service types
    #next step would be converting prices into crypto currency amounts
    def __init__(self, name, account, reciever_id):
        self._name = name
        self._account_amount = account
        self.__private_id = reciever_id
        self._transactions = np.array(
        [["Cost of Transaction", "Service", "Running Account Amount"]],
        dtype=object)

    def account_dec(self, decrease):
        self._account_amount -= decrease

    def robot_name(self):
        return self._name

    def account_amount(self):
        return self._account_amount
    
    def account_transactions(self):
        return self._transactions
    
    def successful_transaction(self,robotObj,Success):
        #if a successful transaction, the success counter increments by 1, else decrements by 2, prioritizes success half as much as failure
        if Success:
            robotObj._success_count+=1
        else:
            robotObj._success_count-=2

class SenderRobot:
    #defines functions fo raccessing robot name, service, and account amount
    #might need a check function to make sure the other is the correct one, too
    def __init__(self, name, service, service_cost, account, sender_id):
        self._name = name
        self.service = service
        self._service_cost = service_cost
        self._account_amount = account
        self._success_count=0
        self.__private_id = sender_id
        self._recieved_transactions = np.array(
        [["Transaction Amount", "Service", "Running Account Amount"]],
        dtype=object)

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
    
    def trade_transactions(self):
        return self._recieved_transactions
    
    def success_count(self):
        return self._success_count

    def trade(self, robotObj, name):
        if name == robotObj.robot_name():

            cost = self.service_cost()
            reciever_start_amount=robotObj.account_amount()
            if (cost<reciever_start_amount):
                #sender actions
                self.account_add(cost)
                sender_account_amount=self.account_amount()

                #reciever actions
                robotObj.account_dec(cost)
                service=self.robot_service()
                reciever_account_amount=robotObj.account_amount()

                #appending to arrays
                self._recieved_transactions=np.vstack([self._recieved_transactions,[cost,service, sender_account_amount]])
                robotObj._transactions=np.vstack([robotObj._transactions,[-cost,service,reciever_account_amount]])
            else:
                print("Not enough money!")

##############################################################################################
#shows how a token is instrumented

reciever1=RecieverRobot("SoFi1", 500, 43345)
reciever2=RecieverRobot("SoFi2", 500, 43346)
reciever3=RecieverRobot("SoFi3", 500, 43347)
reciever4=RecieverRobot("SoFi4", 500, 43348)

#example of a list of recievers, or robots that will recieve a task 
recievers=[reciever1,reciever2,reciever3,reciever4]

sender1=SenderRobot("AdAm1", "Car Cleaning", 250, 0, 21924)
sender2=SenderRobot("AdAm2", "Car Cleaning", 250, 0, 21925)
sender3=SenderRobot("AdAm3", "Car Cleaning", 250, 0, 21926)
sender4=SenderRobot("AdAm4", "Car Cleaning", 250, 0, 21927)
sender5=SenderRobot("AdAm5", "Car Cleaning", 250, 0, 21928)

#example of a list of senders, or robots that will do a task
senders=[sender1,sender2,sender3,sender4,sender5]


#example use case of a sender doing a trade with a reciever, the reciever not liking the trade, and giving a negative success rate 
sender1.trade(reciever1, "SoFi1")

reciever1.successful_transaction(sender1, False)
print(sender1.success_count())

#now, I need to figure out how to parse over the list and use a random.randint() function to randomly select a reciever, and prioritize positive success
#need some time aspect, so multiple robots arent' operating at once 

#https://leetcode.com/problems/random-pick-with-weight/description/
#will resort list so each run, all of them are sorted by their success_index, with the lowest success-rate at the beginning

#bubble sort algorithm
def bubble_sort (senders):
    for i in range (len(senders)):
        swapped=False
        for j in range(0,len(senders)-i-1):
            if senders[j].success_count() > senders[j+1].success_count():
                senders[j+1],senders[j]=senders[j],senders[j+1]
                swapped=True
            if not swapped:
                break

#lower efficiency, but easier to implement
def selection_sort(senders):
    for i in range(len(senders)):
        min_idx=i
        for j in range(i+1,len(senders)):
            if senders[j].success_count()<senders[min_idx].success_count():
                min_idx=j
        senders[i],senders[min_idx]=senders[min_idx],senders[i]
    return(senders)

#will arrange the list in order from lowest to highest success-rate
#now, need a function that will semi-randomly select an integer with corresponding weights on higher indeces
#so if it is a length

#indexing at 0 through length()+1
net_sum=sum(range(1,len(senders)+1))
#divides 100percent proportionally by the sum of each index
index_rate=100/net_sum

#now, I just need to assign a gaussian probability to each index with the index+1 times the rate, then subtract one of the resulting index