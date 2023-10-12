

class ListWords:
    def __init__(self):
        self.list_word = ["Zero","One", "Two", "Three", "Four", "Five", "Six", "Seven",
                      "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
                      "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty",
                      "Thirty", "Fourty", "Fifty", "Sisty", "Seventy", "Eighty", "Ninety",  ]
    
    def get_words(self, num):
        if num in self.list_word:
            return self.list_word[num]
        
        elif 0 <= num <= 20:
            return self.list_word[num]
        
        elif 20 <= num <= 99:
            
            ...
...





def main():
    var = (22//10)
    print (var) 
    ...


if __name__ == "__main__":
    main()