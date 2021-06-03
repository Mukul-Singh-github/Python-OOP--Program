class Multiplex:
    __list_movie_name=["movie1","movie2"]
    __list_total_tickets=[100,60]
    __list_last_seat_number=["M1-2","M2-3"]  #[ last_seat_number_for_mov1 , last_seat_number_for_mov2 ]
    __list_ticket_price=[150,200]
    
    def __init__(self):
      self.__total_price=3456   #any random value
      self.__seat_numbers=1234  #any random value
        

    def calculate_ticket_price(self,movie_index,number_of_tickets):
        self.__total_price = Multiplex.__list_ticket_price[movie_index]*number_of_tickets
        print("Total price is: ",self.__total_price)

    def check_seat_availability(self,movie_index,number_of_tickets):
        if (Multiplex.__list_total_tickets[movie_index]<number_of_tickets):
            return False
        else:
            return True


    def book_ticket(self, movie_name, number_of_tickets):
        if movie_name in Multiplex.__list_movie_name:
            if self.check_seat_availability(Multiplex.__list_movie_name.index(movie_name),number_of_tickets) == True:
                self.__seat_numbers = self.generate_seat_number( Multiplex.__list_movie_name.index(movie_name) , number_of_tickets )
                self.__total_price =  self.calculate_ticket_price(Multiplex.__list_movie_name.index(movie_name) , number_of_tickets)
                return self.__seat_numbers
                
        
    def  generate_seat_number(self,movie_index, number_of_tickets):
        ticket_list = []
        if movie_index == 0:
            if Multiplex.__list_last_seat_number[movie_index] != None:
              print(Multiplex.__list_last_seat_number[movie_index])
              slist = Multiplex.__list_last_seat_number[movie_index].split("-")
              seat_counter = int(slist[1]) 
                
            for i in range(number_of_tickets):
                ticket_list.append( "M1-" + str(seat_counter))
                seat_counter = seat_counter + 1
                
            Multiplex.__list_last_seat_number[movie_index] = ticket_list[-1]
            Multiplex.__list_total_tickets[movie_index] -= number_of_tickets
            return ticket_list
            
        
        elif movie_index == 1:
            if Multiplex.__list_last_seat_number[movie_index] != None:
              slist = Multiplex.__list_last_seat_number[movie_index].split("-")
              seat_counter = int(slist[1])
               
                
            for i in range(number_of_tickets):
                ticket_list.append( "M2-" + str(seat_counter) )
                seat_counter = seat_counter + 1
            
            Multiplex.__list_last_seat_number[movie_index] = ticket_list[-1]
            Multiplex.__list_total_tickets[movie_index] -= number_of_tickets
            return ticket_list


    #getters
    def get_total_price(self):
      return self.__total_price
    
    def get_seat_numbers(self):
        return self.__seat_numbers
        


booking1=Multiplex()
status=booking1.book_ticket("movie1",10)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())
