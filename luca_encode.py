# luca weisman

# def decode(encoded_password):
 # original_password = ""
  #for digit in encoded_password:
   # temp = int(digit) - 3
   # if temp < 0:
    #  temp += 10
    #  original_password += str(temp)
    #else:
    #  original_password += str(temp)
  #return original_password

def decode(number):
  decoded_num = ""
  for digit in number:
    temp = int(digit) - 3
    if temp < 0:
      decoded_num += str(10 - temp)
    else:
      decoded_num += str(temp)
    return decoded_num

