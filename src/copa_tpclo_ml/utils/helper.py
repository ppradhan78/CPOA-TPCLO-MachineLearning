import os
import random
import string
import time

class Helper:
    def GetfileName(path):
        return os.path.basename(path)
    
    def GetfileNameWithouExtension(path):
        return os.path.splitext(os.path.basename(path))[0]
    
    def GetUniquefileName(filename):
        return time.strftime("%Y%m%d-%H%M%S") +"_"+filename
    
    def generate_random_string(length):
        """Generate a random string of lowercase letters and digits."""
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for _ in range(length))

def generate_random_file(filename, num_lines, line_length):
    """Generate a file of random lines with the given number and length."""
    with open(filename, 'w') as f:
        for i in range(num_lines):
            random_line = Helper.generate_random_string(line_length) + '\n'
            f.write(random_line)