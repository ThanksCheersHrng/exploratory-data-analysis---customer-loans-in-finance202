class RDSDatabaseConnector: 
    def __init__(self, param1, param2): 
        self.param1 = param1
        self.param2 = param2 
        self.param3 = param2*param2
        self.param4 = "cats, man, dude!"
        
    def method1(self, external_input): 
        return #some func to do with param1+external_input 


import yaml #this will allow us to read credentials.yaml as a dict

def load_credentials(file): #loads file and returns dictionary contained within
	dictionary = yaml.load(open(file, 'r')
	return(dictionary)


