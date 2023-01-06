class Patient:
               
               symptoms = []

               def __init__(self, first_name,  surname, symptom, age, mobile, postcode):
                                """
                                Args:
                                first_name (string): First name
                                surname (string): Surname
                                age (int): Age
                                mobile (string): the mobile number
                                address (string): address
                                """
                            ##initializing the attributes of the class
        
                                self.__first_name = first_name
                                self.__surname = surname
                                self.age = age
                                self.mobile = mobile
                                self.symptom = symptom
                                self.address = postcode
                                self.__doctor = str('None')

               def get_full_name(self) :
                                """full name is first_name and surname"""
                                return  self.__first_name + " " + self.__surname
                           
                               
               def get_doctor(self) :
                                '''return doctors full name '''
                                return self.__doctor
                            
               def link(self, doctor):
                                """Args: doctor(string): the doctor full name"""
                                self.__doctor = doctor

               def print_symptoms(self):
                                """prints all the symptoms"""
                                return self.symptom
                            
               def get_surname(self):
                        return self.__surname

               def __str__(self):
                        return f'{self.get_full_name():^30}|{self.__doctor:^30}|{self.age:^5}|{self.mobile:^15}|{self.address:^10}'
