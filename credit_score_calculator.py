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