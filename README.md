## Installation

pip install passfactory

## Usage

```python
import passfactory as pf

# Create the object
root = pf.Password(2, "") # Security level: 2, forbidden chars: No forbidden chars
other_root = pf.Password(2, "")
password = root.generate() # Generating a random password according to parameters provided in constructor
print(password) # Prints randomly generated password

root.copy() # Copy the password in paperclip ;)

root.save("passfile.txt") # Save the password (encoded in base64) in a file with

alpha_chars, nums, special_chars = root.stats() # Returns the characters present in the alphabet, the numbers
                                             # and the special characters in the last generated password

difference_between_passwords = root - other_root # Stores difference between 2 passwords (only different chars)

def get_save_pass(): # Automatically generate passwords until a specially save one pops out
    global root
    global password
    while not root.test():
        password = root.generate()
    return password
```
