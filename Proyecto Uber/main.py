from cars.cars import Car
from account.account import Account

def run():
    
    
    car1 = Car("AWW212", Account("Roberto Ayala", 1242155123))
    car1.passengers = 4
    car1.id = 212

    print(car1.passengers, car1.id)

if __name__=='__main__':
    run()