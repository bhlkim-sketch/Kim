# Byoung Hartzel L. Kim        9 - Beryllium
# activity number 4
class Patient: # the main patient class
    def __init__(self, patientname, patientbill_amount):
        self.patientname = patientname
        self.patientbill_amount = patientbill_amount
    # self explanatory, gets and sets the patient's name and bill
    def getpatientsname(self):
        return self.patientname

    def setpatientname(self, newname):
        self.patientname = newname
    
    def getthebillamount(self):
        return self.patientbill_amount

    def setthebillamount(self, newbillamount):
        self.patientbill_amount = newbillamount

    def calculatebill(self):
        return self.patientbill_amount

# new senior subclass from the main patient class
class Senior(Patient):
    def __init__(self, patientname, patientbill_amount, discount): # get methods from the main class
        super().__init__(patientname, patientbill_amount)
        self.discount = discount

    def calculatebill(self):
        discounted_amount = self.patientbill_amount * (1 - self.discount) # calculations
        return discounted_amount

    def displaypatienttype(self):
        return "Senior Citizen" # only and only returns its own patientdisplay, which is Senior Citizen


class PhilHealth(Patient):
    def __init__(self, patientname, patientbill_amount, philhealth_discount): # same here
        super().__init__(patientname, patientbill_amount)
        self.philhealth_discount = philhealth_discount

    def calculatebill(self):
        discounted_amount = self.patientbill_amount * (1 - self.philhealth_discount) # this calculates bill, same as the one in Senior
        return discounted_amount

    def displaypatienttype(self):
        return "PhilHealth Member" # returns philhealth member

# main code that was shown on sg11
patient = Patient("Juan Dela Cruz", 15000)
philhealth = PhilHealth("Maria Santos", 15000, 0.2)
senior = Senior("Pedro Reyes", 15000, 0.15)

print("Hospital Billing System")
print("------------------------")

print(f"Patient: {patient.getpatientsname()}")
print("Type: Regular Patient") # the sg did not say that i must add one to the Patient class, so i just printed it like so
print(f"Bill Amount: {patient.getthebillamount():,.2f}")
print(f"Final Bill: {patient.calculatebill():,.2f}")

print()
# philhealth patient
print(f"Patient: {philhealth.getpatientsname()}") #name
print(f"Type: {philhealth.displaypatienttype()}") #type
print(f"Bill Amount: {philhealth.getthebillamount():,.2f}") #original bill
print(f"Final Bill: {philhealth.calculatebill():,.2f}") #discounted bill

print()
# senior citizen
print(f"Patient: {senior.getpatientsname()}") #same goes for every one
print(f"Type: {senior.displaypatienttype()}")
print(f"Bill Amount: {senior.getthebillamount():,.2f}")
print(f"Final Bill: {senior.calculatebill():,.2f}")
