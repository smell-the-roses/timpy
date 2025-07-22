"""
timpy is a library for sanitizing numeric inputs.
Written by Tim Warner in 2025
"""

def get_float(prompt) -> float:
    """
    Sanitizes the input and returns a float.
    Truncates all values smaller than 10**-8 to zero.
    I leave it to the developer to deal with rounding issues.
    """
    # I truly hate floating-point inputs.
    while True:
        try:
            out = input(prompt)

            if not out.replace(".", "", 1).replace("-", '', 1).isdigit():
                raise ValueError

            out = float(out)

            if abs(out) < 10**-8:
                out = 0
                
        except ValueError:
            print("\nValue Error. Not a float.\n")
            continue
        except EOFError: # so we can just leave.
            print("\nEOF detected. Quitting.")
            quit() # generic case to drop out of the current prompt
        except: # catch random garbage
            print("\n\nYour code is ~broken~.\n\n")
            continue
        else:
            return out

        
def get_int(prompt) -> int:
    """
    Sanitizes the input and returns an int.
    """
    while True:
        try:
            out = int(input(prompt))

            if out != out: # Hack to check if out is NaN.
                raise ValueError
            
        except ValueError:
            print("\nValue Error. Not an int.\n")
            continue
        except EOFError: # so we can just leave.
            print("\nEOF detected. Quitting.")
            quit() # generic case to drop out of the current prompt
        except: # catch random garbage
            print("\n\nYour code is ~broken~.\n\n")
            continue
        else:
            return out

