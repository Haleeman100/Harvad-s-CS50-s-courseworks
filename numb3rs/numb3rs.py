"""
Season 5, Episode 23 

An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet,
 akin to a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#. 
But each # should be a number between 0 and 255, inclusive. Suffice it to say 275 is not in that range! 
If only NUMB3RS had validated the address in that scene!
In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input 
as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.
Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other functions
 as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.
"""
import re

def main():
    ip = input("Ipv4 address: ").strip()
    return validate(ip)

# This function returns bool based on if the ip address address is right or wrong
def validate(ip):
    # 25[0-5] uses regex to check and see matching string from 250-255
    # 2[0-4][0-9] checks 200-249
    #[ 01]?[0-9] checks from 0-1 to 199
    return bool(re.search(
        r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})$", ip
    )

    )

if __name__ == "__main__":
    result = main()
    print(result)
