import sys
import inflect
import datetime


class Convert:
    def __init__(self):
        self.p = inflect.engine()
        
    def convert_number(self, number):
       if number >= 0:
            if number < 10**12:
                words = self.p.number_to_words(number, andword="").capitalize()
                return words
            else:
                return "Number is too large to convert"
       else:
            return "Invalid number"
        
class DateToAge:
    def __init__(self):
        self.convert_number = Convert()
        
    def convert_date_to_age(Self, str): 
       # date_format = "%Y-%m-%d"
        dob_date = datetime.datetime.strptime(str, "%Y-%m-%d").date()
        today_date = datetime.date.today()
        get_age_in_days = (today_date - dob_date).days
        get_age_in_minutes = get_age_in_days * 24*60
        return get_age_in_minutes     
    
    def convert_age_to_number(self, str):
        if not self.check_format(str):
            sys.exit("Invalid date format")
        
        get_age_in_minutes = self.convert_date_to_age(str)
        age_words = self.convert_number.convert_number(get_age_in_minutes)
        return age_words
    
    def check_format(self, str):
        date_format = "%Y-%m-%d"
        try:
            datetime.datetime.strptime(str, date_format)
            return True
        except ValueError:            
            return False
        
        ...
    ...
 #Pr user for their date of birth
dob = input("Enter your date of birth (YYYY-MM-DD): ")

#date_to_age_converter = DateToAge()
           
            
if __name__ == "__main__":
    date_to_age_converter = DateToAge()
    age_converter_to_words = date_to_age_converter.convert_age_to_number(dob)
    print(age_converter_to_words)


    

