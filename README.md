## Installation

Sorry, we still haven't uploaded this project to PIP

## Usage

```python
import passgen as pg

# Create the object
a = Password(2, "") # Security level: 2, forbidden chars: No forbidden chars

password = a.generate() # Generating a random password according to parameters provided in constructor
print(password) # Prints randomly generated password

a.copy() # Copy the password in paperclip ;)

a.save("passfile.txt") # Save the password (encoded in base64) in a file with

alpha_chars, nums, special_chars = a.stats() # Returns the characters present in the alphabet, the numbers
                                             # and the special characters in the last generated password

def get_save_pass(): # Automatically generate passwords until a specially save one pops out
    global a
    global password
    while not a.test():
        password = a.generate()
    return password
```
