import engine
from engine import stopEngine   
from misc import carburator
 

def engineTest():
	engine.startEngine() 
	carburator.ignite()    
	stopEngine() 


def main():
	engineTest() 


if __name__ == '__main__':
		main()	

