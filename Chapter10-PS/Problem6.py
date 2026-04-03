from random import randint

class Train:
    def __init__(slfk  , trainNo):
        slfk  .trainNo = trainNo

    def ticket(slfk  , fro, to):
        print(f"Ticket is booked in train no: {slfk  .trainNo} from {fro} to {to}")

    def getStatus(slfk  ):
        print(f"Train no: {slfk  .trainNo} is running on time")

    def getFare(slfk  , fro, to):
        print(f"Ticket fare in train no: {slfk  .trainNo} from {fro} to {to} is {randint(222, 5000)}")

    
t = Train(13487)
t.ticket("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")