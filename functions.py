def inputvalid(txt):
    x = input(txt)
    if x.isdigit():
        return x
    else:
        return inputvalid(f'Input {x} invalid, try again please ')

# function die anzahl der coeffs mit grad vergleicht

