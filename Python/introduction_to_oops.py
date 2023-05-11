class Lms_members():
    organisation_name = "CDAC" # class variable 
    
    @classmethod
    def get_organisation_name(cls):
        print("Organisation name is " , cls.__organisation_name)
        
    @classmethod
    def set_organisation_name(cls,rcvd_val):
        cls.__organisation_name = rcvd_val
    
    # instance variables 
    def __init__(self,rcv_member_name,rcv_member_status,rcv_member_sal = 0 ,rcv_bank_locker_key = 99999):
        self.member_name = rcv_member_name
        self.member_status = rcv_member_status
        self.__member_salary = rcv_member_sal
        self._bank_locker_key = rcv_bank_locker_key
        
    # instance methods
    def get_membership_status(self):
        print("Membeship status for the object " , self.member_status)

    def set_membership_status(self,rcv_new_val):
        self.member_status = rcv_new_val
        
    def get_member_detail(self):
        print( self.member_name  + " " + self.member_status + " " + str(self.__member_salary) + " " + str(self._bank_locker_key ) , end = "")    
    
    @staticmethod
    def print_temperature():
        print("I am a static method")
    

# create an object 
# my_first_custom_object_ref = Lms_members("gaurav","permanent")
# print(type(my_first_custom_object_ref))
# print(id(my_first_custom_object_ref))

# print(Lms_members.organisation_name)
# Lms_members.get_organisation_name()
# Lms_members.set_organisation_name("NEW VALUE")
# Lms_members.get_organisation_name()


# print(my_first_custom_object_ref.member_status)
# print(my_first_custom_object_ref.member_name)
# my_first_custom_object_ref.get_membership_status()
# my_first_custom_object_ref.set_membership_status("My updated status")
# my_first_custom_object_ref.get_membership_status()

# Lms_members.print_temperature()


# my_second_custom_object_ref = Lms_members("pratik","temporary")

# print(Lms_members.organisation_name)
# Lms_members.set_organisation_name("SUNBEAM")
# print("I changed to SUNBEAM using Class reference and calling set_organisation_name() ")
# print("Class Organisation name" , end = "-----")
# print(Lms_members.organisation_name)
# print(" Gaurav's Organisation name" , end = "-----")
# print(my_first_custom_object_ref.organisation_name)
# print(" Pratik's Organisation name ", end = "-----")
# print(my_second_custom_object_ref.organisation_name)

# my_first_custom_object_ref.set_organisation_name("CDAC")
# print("I changed to CDAC using Gaurav's reference and calling set_organisation_name()")
# print("Class Organisation name" , end = "-----")
# print(Lms_members.organisation_name)
# print(" Gaurav's Organisation name" , end = "-----")
# print(my_first_custom_object_ref.organisation_name)
# print(" Pratik's Organisation name ", end = "-----")
# print(my_second_custom_object_ref.organisation_name)

# my_first_custom_object_ref.organisation_name ="NEW_ORGANISATION"
# print("I changed to NEW_ORGANISATION using Gaurav's reference but using public access to Class variable ")
# print("Class Organisation name ", end = "-----")
# print(Lms_members.organisation_name)
# print(" Gaurav's Organisation name ", end = "-----")
# print(my_first_custom_object_ref.organisation_name)
# print(" Pratik's Organisation name ", end = "-----")
# print(my_second_custom_object_ref.organisation_name)


# del (my_first_custom_object_ref.organisation_name)
# print(" Gaurav's Organisation name ", end = "-----")
# print(my_first_custom_object_ref.organisation_name)


# #del (my_first_custom_object_ref.member_status)
# #del (my_first_custom_object_ref)
# # print(" Pratik's member_status ", end = "-----")
# # print(my_second_custom_object_ref.member_status)

# # print(" Gaurav's member_status ", end = "-----")
# # print(my_first_custom_object_ref.member_status)

# print("Before --> " , dir(Lms_members))
# print("I am deleting class variable using class reference ")
# #del (Lms_members.organisation_name)
# #Lms_members.get_organisation_name()
# #Lms_members.set_organisation_name("TEST")
# Lms_members.organisation_name = "TEST"
# print("After --> " , dir(Lms_members))

# print("Class Organisation name ", end = "-----")
# print(Lms_members.organisation_name)
# print(" Gaurav's Organisation name ", end = "-----")
# print(my_first_custom_object_ref.organisation_name)
# print(" Pratik's Organisation name ", end = "-----")
# print(my_second_custom_object_ref.organisation_name)

# print("Before removing class variable (organisation_name)--> " , dir(Lms_members))
# print("I am delete a class variable (organisation_name) using class reference ")
# del (Lms_members.organisation_name)
# print("After removing class variable (organisation_name)--> --> " , dir(Lms_members))

# print("Before removing class method (get_organisation_name)--> " , dir(Lms_members))
# print("I am delete  a class method (get_organisation_name) using class reference ")
# del (Lms_members.get_organisation_name)
# print("After removing class method (get_organisation_name) --> " , dir(Lms_members))

# print("Before removing instance method (get_membership_status)--> " , dir(my_first_custom_object_ref))
# print("I am delete  a instance method (get_membership_status)  using gaurav reference ")
# #del (my_first_custom_object_ref.get_membership_status)
# print("After removing instance method (get_membership_status)--> " , dir(my_first_custom_object_ref))

# print("Before removing instance method (get_membership_status)--> " , dir(my_first_custom_object_ref))
# print("I am delete  a instance method (get_membership_status)  using CLASS reference ")
# del (Lms_members.get_membership_status)
# print("After removing instance method (get_membership_status)--> " , dir(my_first_custom_object_ref))

my_third_custom_object_ref = Lms_members("Deepak","temporary",1000000,7777777)

# print(my_third_custom_object_ref.__member_salary)
#print(Lms_members.organisation_name)

# print("Before --> " , dir(Lms_members))
# Lms_members.set_organisation_name("providing a value ")
# print("After --> " , dir(Lms_members))

# name mangling
# print(my_third_custom_object_ref._Lms_members__member_salary)

# print("Deepak's Object" , dir(my_third_custom_object_ref))
# print("Protected member from Deepak's Object has value " , my_third_custom_object_ref._bank_locker_key)

# print(my_third_custom_object_ref.organisation_name)


