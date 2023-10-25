# luca weisman

def decode(encoded_password):
  original_password = ""
  for digit in encoded_password:
    temp = int(digit) - 3
    if temp < 0:
      temp += 10
      original_password += str(temp)
    else:
      original_password += str(temp)
  return original_password
