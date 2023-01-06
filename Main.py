# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB')# username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 'Malaria', 20, '07012345678','B1 234'), Patient('Mike','Jones', 'Malaria', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 'Fever',  15, '07123456789','C1 ABC')]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Group Patients')
        print(' 6- Request Management Report ')
        print(' 7- Update admin detais')
        print(' 8- Store into CSV / Load patients into a CSV file  ')
        print(' 9- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
         
            admin.doctor_management(doctors)
          

        elif op == '2':

                # 2- View or discharge patients
                
                while True:
                        op = input('Do you want to discharge a patient(Y/N):   ').lower()


                        if op == 'yes' or op == 'y':
                           
                            admin.discharge(patients, discharged_patients)

                        elif op == 'no' or op == 'n':
                            break

                        # unexpected entry
                        else:
                            print('Please answer by yes or no.')
        
        elif op == '3': 
                
                admin.view_discharge(discharged_patients)
            # 3 - view discharged patients
            
            

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)
        elif op == '5':
            admin.group_patients(patients)
        elif op == '6':
            admin.management_report(patients, doctors)
        elif op == '7':
            # 5- Update admin detais
            admin.update_details()


        elif op == '8':
            #load the patients into a csv file 
            #importing the python csv library 
            print("1- Load into csv file.")
            print("2- Store from a csv file.")
            op = input("Enter Operation ; ")
            import csv 

            if op == '1':
                    with open('patients_list', 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow("patient details")
                        for patient in patients:
                            writer.writerow(patient.__str__())
                

                
                    print("CHECK THE FOLDER, PATIENTS DETAILS HAVE BEEN SUCCESSFUL STORED INTO 'patients.py' ")

            elif op == '2':
                file_name = input("Enter the file name in the right case including: ")
                try: 
                    with open(file_name, 'r') as csvfile:
                                # Create the reader object
                                reader = csv.reader(csvfile)
                                
                                # Skip the header row
                                next(reader)
                                
                                # Iterate through the rows in the CSV file
                                for row in reader:
                                    # Get the data from the row
                                    first_name = row[0]
                                    surname = row[1]
                                    symptom = row=[2]
                                    age = row[3]
                                    mobile = row[4]
                                    postcode = row[5]

                                    
                                    # Create a patient object and add it to the list declared globally 
                                    patient = Patient(first_name, surname, symptom, age, mobile, postcode)
                                    patients.append(patient)
                except:
                    print("The file wasnt found.Please enter a valid file")


        elif op == '9':
            print("Exited successfully ")
            import sys 
            sys.exit()


        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()

