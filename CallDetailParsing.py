class CallDetail:
    def __init__(self,calling_number,called_number,call_duration,call_type):
        self.calling_number = calling_number
        self.called_number = called_number
        self.call_duration = call_duration
        self.call_type = call_type

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        list_of_call_list =[]
        l=[]
 
        for call in list_of_call_string:
            list_of_call_list.append(call.split(","))
        
        for inner_call_list in list_of_call_list:
            l.append(CallDetail(*inner_call_list))  # * operator unpacks the list here in arguments which will be passed in CallDetails
        
        u1.list_of_call_objects = l

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
u1 = Util()
u1.parse_customer(list_of_call_string)
#u1.list_of_call_objects = l
print(u1.list_of_call_objects[0])
