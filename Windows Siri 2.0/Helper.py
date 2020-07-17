from datetime import datetinne
import threading
import pynput
import csv
import string
import secrets
import math

def main():
      greeting = greet.name
      greet(greeting)
      
      question = input("What do you want?\n")
      if question.lower() == "converter":
        converter_changer =input("What kind of converter do you want?\nLength converter\nMass converter\nArea converter\nData Transfer Rate converter\nDigital Storage converter\nEnergy converter\nFrequency converter\nFuel Economy Converter\nTime converter\nPlane angle converter\nPressure converter\nSpeed converter\nTempreature converter\nVolume converter")    
        
        if converter_changer.lower() == "length converter":
            length_to_obvious_converters = input("What conveters do you want in the length section")
            
            if length_to_obvious_converters.lower() == "km to miles converter":
                km_to_miles_converters()
            
            elif length_to_obvious_converters.lower() == "foot to metres" or "feet to metres":
                foot_to_metres_converters()
        
        elif converter_changer.lower() == "mass converters":
            mass_to_obvious_converters = input("What converters do you want in the mass section")
            
            if mass_to_obvious_converters.lower() == "kg to lb converter" or "kg to pund coverter":
                Mass_Converters()
            
            elif mass_to_obvious_converters.lower() == "lbs to kg converter" or "pound to kg converter":
                mass_to_obvious_converters()
            
            

            if question.lower() == "tempreature converters":
                Tempreature_Converters()

      if question.lower() =="credit score caclculator":
        credit_scrore_calculator()

class greet():

    name = input("What's your name?\n")

    def greet(self,str):
        length_of_name = len(str)

        if length_of_name > 34:
            print("name is too long.Try making it shorter")

        elif length_of_name < 3:
            print("name is to short.Try making it longer")
        
        elif length_of_name == 0:
            print("There's nothing there") 
    
        else:
            print(f"Hello {str}")

class km_to_miles_converters():

    desion_to_turn_km_to_miles_or_miles = input("Do you want to convert miles to km or km to miles\nfoot to metres\nfFeet to centimetres\n")
    km = input("How many kms do you want to want to conbert to miles?\n")


    def km_to_mile_converter(self,str):
        km_converted_to_int = int(str)
        km_converted_result = km_converted_to_int*0.62137
        print(f"{km_converted_result}tmiles")

    def miles_to_km_converter(self,str):
        miles_converted_to_int = int(str)
        miles_converted_result = miles_converted_to_int/0.62137
        print(f"{miles_converted_result}km")

class foot_to_metres_converters:
    
    if length_to_obvious_converters.lower() == "feet":
        foot1 = input("How many foot do you want to convert into metres")
    print("Converting...")
   
    def foot_to_metres_converter(self,str):
        foot_converted_to_int = int(str)
        foot_converted_result = foot_converted_to_int  
        print(f"{foot_converted_result}ft")

    def metres_to_metres_converter(self,str):
        foot_converted_to_int = int(str)
        foot_converted_result = foot_converted_to_int  
        print(f"{foot_converted_result}ft")
                
class credit_scrore_calculator_and_saver():
    age = input("What's your age?\n")
    gender = input("What's your gender?\n")
    payment_history = input("How many loans you have you paid\n")
    loans = input("How many loans do you have?\n")
    loans_paid = input("How many loans you have paid\n")
    credit_card_utilization = input("How much have you used your credit card\n")

    def __init__(self):
        self.__init__()

    def  _credit_calculator(self,age,gender,payment_history,loans_paid):
        self.credit_scrore_calculator_1 = age
        self.credit_scrore_calculator_2 = gender
        self.payment_history_converted_to_int = int(payment_history)
        self.loans_paid_conerted_to_int = int(loans_paid)
        self.kg_or__to_kg_converterdebt = self.payment_history_converted_to_int - self.loans_paid_conerted_to_int
        self.score = 350

        
        
        for self.debt in range(31):
            self.score += 100
            
        if self.debt < 43:
            self.score += 100

        if gender.lower() == "girl" or "woman":
            self.score -= 100
       
        if gender.lower() == "boy" or "man":
            self.score += 1
        
        for age in range(36-1):
            self.score += 200
            
        if age == 36 or 37 or 38 or 39 or 40 or 41 or 42 or 43 or 44 - 1:
            self.score = 0

        elif age == 45 or 46 or 47 or 48 or 49 or 50 or 51 or 52 or 53 or 54 - 1:
            self.score =- 200
    
        elif age == 55 or 56 or 57 or 58 or 59 or 60 or 61 or 62 or 63 or 64 - 1:
            self.score == 0
        
        elif age == 65 or 66 or 67 or 68 or 69 or 70 or 71 or 72 or 73 or 74 - 1:
            self.score =+ 100
        
        elif age > 75 - 1:
            self.score =+ 200
        
        if self.score == 900:
            print(f"Your credit score is:{self.score}.\nYour credit score is perfect.\nYou'll definetely")
        
        for self.score in range(700,900):
            print(f"Your credit score is:{self.score}.\nThat's average\n.But sometimes you'll never be allowed to take a loan.\n")
        
        for self.score in range(500,700):
            print(f"Your credit score is:{self.score} .\nThat's not too bad.\n But you'll not be given loans that much")

        for self.score in range(350,500):
            print(f"Your credit score is:{self.score} .\nThat's  bad\nDefinetly no loans.\nHere are some tips to help:\n1.Try spending less of your card.\n2.Respect your money  ")         



                 
         class Mass_Converters:
    
            def __init__(self):
                self.__init__()

         def kg_to_lbs_converter(self,str):
            self.kg_converted_to_int = int(str)
            self.kg_converted_result = kg_converted_to_int* 2.205
            print(kg_converted_result,"lbs/pounds")
        
        if main.length_to_obvious_converters.lower() == "lbs to kg" or "pounds to kg":
        self.foot1 = input("How many kgs do you want to convert into lbs ")
        print("Converting...")

    def lbs_or_pouds_to_kg_converter(self,str):
        lbs_or_pounds_converted_to_int = int(str)
        lbs_or_pounds_converted_result = lbs_or_pounds_converted_to_int/ 2.205
        print(f"{lbs_or_pounds_converted_result}kg")
    
    def kg_or__to_kg_converter(self,str):
        lbs_or_pounds_converted_to_int = int(str)
        lbs_or_pounds_converted_result = lbs_or_pounds_converted_to_int/ 2.205
        print(f"{lbs_or_pounds_converted_result}kg")
        
class Tempreature_Converters:
    def celcius_to_farnenhiet_converter(self,str):
        celsius_turned_to_an_int = int(str)
        celsius_converted_result = celsius_turned_to_an_int/5*8+32
        print(f"{celsius_converted_result}℉")
    
    def farnenhiet_to_celcuis_converter(self,str):
        farnenhiet_converted_to_int = int(str)
        farnenhiet_converted_result = farnenhiet_converted_to_int-32/9*5
        print(f"{farnenhiet_converted_result}℃")
    
    def celcius_to_kelvin_converter(self,str):
        celsius_turned_to_an_int = int(str)
        celsius_converted_result1 = celsius_turned_to_an_int + 273.15
        print(f"{celsius_converted_result1}K")
    
    def farnenhiet_to_kelvin_converter(self,str):
        farnenhiet_converted_to_int = int(str)
        farnenhiet_converted_result1 = farnenhiet_converted_to_int + 273.15
        print(f"{farnenhiet_converted_result1}K")
    
class passwords():
    account = input("What account do you want to have a secure password for?")
    password = secrets.token_hex(32)

    def password_creator(self,account):
            print(f"{pssswords.account}: {passwords.password}")

    def  password_saver(self,password):
        with open(' Passwords.xlsx', 'w', newline='') as csvfile:
            fieldnames = ['Account_Name', 'Passwords']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'Account_Name':passwords.account, 'Password':passwords.password})

main()
