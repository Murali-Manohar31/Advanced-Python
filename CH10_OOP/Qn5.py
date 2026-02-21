from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
        
    def book(self,fro,to):
        print(f"The train {self.trainNo} is from {fro} to {to}")
        
    def status(self):
        print(f"The train {self.trainNo} is running on time")
        
    def fare(self,fro,to):
        print(f"The fair of train {self.trainNo} from {fro} to {to} is {randint(100,5000)} rupees")
        
t=Train(23667)
t.book("bbsr","trd")
t.status()
t.fare("bbsr","trd")