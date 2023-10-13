import inflect


class Convert:
    def __init__(self):
        self.p = inflect.engine()
        
    def convert_number(self, number):
        if number >= 0:
            words = self.p.number_to_words(number, andword="")
            return words        
        else:
            return "Invalid number"
        
class DateToAge:
    def __init__(self):
        self.convert_number = Convert()
        
    
    ...
            
            
if __name__ == "__main__":
    convert = Convert()
    number = 22227777
    new_words = convert.convert_number(number)
    print(new_words)
    

