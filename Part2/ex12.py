str1 = 'The'
str2 = 'Thumbs up'
str3 = 'Theatre can be boring'

def check_string(text):
    if "The" in (text):
        return "Found it!"
    
    else:
        return "None!"
    
print(check_string(str1))
print(check_string(str2))
print(check_string(str3))