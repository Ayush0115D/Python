from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Brewing chai for {name}")
    time.sleep(2)  # Simulate time taken to brew chai
    print(f"Chai for {name} is ready!")
if __name__ == "__main__":
    chai_makers=[
        Process(target=brew_chai, args=(f"chai_maker_{i+1}",)) 
        for i in range(3)
    ]
    
    #statrt all processes
    for p in chai_makers:
        p.start()   
    #wait for all to finish
    for p in chai_makers:
        p.join()
        
    print("All chai brewed!") 