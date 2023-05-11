# from  introduction_to_oops import *
# class sunbeam_members_with_inheritance(Lms_members):
#     pass

# sunbeam_member2 = sunbeam_members_with_inheritance("Madhura","Temporary")
# sunbeam_member2.get_member_detail()     

from  introduction_to_oops import *
class sunbeam_members(Lms_members):
    
    def __init__(self,member_name,member_status,member_age):
        super().__init__(member_name,member_status)
        self.member_age = member_age
        
    def get_member_detail(self):
        super().get_member_detail()
        print(" " + str(self.member_age))
        
    def get_member_detail(self,honorific_titles):
        print(honorific_titles,end = " ")
        super().get_member_detail()
        print(" " + str(self.member_age))
     
    # operator overloading 
    def  __gt__(self,other_object): 
        return  self.member_age > other_object.member_age      

    def  __le__(self,other_object): 
        return  self.member_age <= other_object.member_age         
    
    def  __eq__(self,other_object): 
        print("eq was invoked ")
        return self.member_age == other_object.member_age
        
sunbeam_member1 = sunbeam_members("Jay","Temporary",22)
sunbeam_member1.get_member_detail("Mr")         

sunbeam_member2 = sunbeam_members("Madhura","Temporary",23)
sunbeam_member3 = sunbeam_member2
sunbeam_member4 = sunbeam_members("Madhura","Temporary",23)
sunbeam_member2.get_member_detail("Ms")         

# if sunbeam_member2 == sunbeam_member1 :
#     print(f" {sunbeam_member2.member_name} is older than {sunbeam_member1.member_name}" )
# else:
#     print(f" {sunbeam_member2.member_name} is younger than {sunbeam_member1.member_name}" )

print(id(sunbeam_member2))
print(id(sunbeam_member3))
print(id(sunbeam_member4))

if sunbeam_member2 == sunbeam_member4 :
    print("Same age")
else:
    print("Different age")    


if sunbeam_member2 is sunbeam_member4 :
    print("Same object")
else:
    print("Different object")    
    
#print(dir(sunbeam_members))
#print(dir(sunbeam_member1))
    

