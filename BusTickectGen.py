class Ticket:
    
    #Static Variables
    __counter = 0
    __destination_list = ["Mumbai", "Pune","Kolkata","Chennai"]
    
    
    def __init__(self):
        self.__ticket_id = None
        self.__passenger_name = None
        self.__source = None
        self.__destination = None
    
    #Validaters
    def validate_source(self):
        if self.__source == "Delhi":
            return True
        else: return False
    
    
    def validate_destination(self):
        for _ in range(len(Ticket.__destination_list)):
            if self.__destination in Ticket.__destination_list:
                return True
            else: return False
    
    
    def validate_source_destination(self):
        if self.validate_source() == True   and  self.validate_destination() == True:
            return True
        else: return False 
        
        
    #Setters
    def set_passneger_name(self,value):
        self.__passenger_name = value
    
    def set_source(self,value):
        self.__source = value
    
    def set_destination(self,value):
        self.__destination = value
    
    
    #Getters
    def get_passneger_name(self):
        return self.__passenger_name
    
    def get_source(self):
        return self.__source
    
    def get_destination(self):
        return self.__destination
    
    def get_ticket_id(self):
        return self.__ticket_id

        
    def generate_ticket(self):
        if self.validate_source_destination() == True:
            Ticket.__counter += 1
            self.__ticket_id = self.__source[0] + self.__destination[0] + "%02d" % Ticket.__counter
            
        else:
            print("Destination or source not available")

t1 = Ticket()
t1.set_passneger_name("Mukul")
t1.set_source("Delhi")
t1.set_destination("Mumbai")
t1.generate_ticket()
print(t1.get_ticket_id())
