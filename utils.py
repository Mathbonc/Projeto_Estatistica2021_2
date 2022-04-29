def parseToNum(num_string):
    if (num_string) and ('.' in num_string) and (not '?' in num_string):
        return float(num_string)
    elif (num_string) and (not '?' in num_string):
        return int(num_string)
