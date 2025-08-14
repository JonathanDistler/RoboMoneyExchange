#Goal of this code is a weighted priority for choosing a robot to do a task
import numpy as np
import random
from RobotObject import RecieverRobot
from RobotObject import SenderRobot

##############################################################################################
####Shows how a token is instrumented####

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
value=random.randint(0,100)
#now, to figure out which range it fits in 

sum=0

chosen_index = None
i = 0
while i < len(senders) and chosen_index is None:
    sum +=i * index_rate
    if value <= sum:
        chosen_index = i
    i += 1

if chosen_index is None:
    chosen_index=len(senders)-1

print(chosen_index)
print(value)

