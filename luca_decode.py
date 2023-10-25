# luca weisman

def encode(original_password):
   encoded_password = ""
   for digit in original_password:
      temp = int(digit) + 3
      if temp >= 10:
         temp -= 10
         encoded_password += str(temp)
      else: 
         encoded_password += str(temp)
   return encoded_password

# mia shin

def decode(number):
  decoded_num = ""
  for digit in number:
    temp = int(digit) - 3
    if temp < 0:
      decoded_num += str(10 - temp)
    else:
      decoded_num += str(temp)
  return decoded_num

# luca weisman

if __name__ == "__main__":
   while True:
      print('Menu')
      print('-------------')
      print('1. Encode')
      print('2. Decode')
      print('3. Quit')
      print()

      menu_selection = int(input('Please enter an option: '))

      if menu_selection == 1:
         original_password = input('Please enter your password to encode: ')
         encoded_password = encode(original_password)
         print('Your password has been encoded and stored!')

      elif menu_selection == 2:
         original_password = decode(encoded_password)
         print(f'The encoded password is {encoded_password}, and the original password is {original_password}.')

      elif menu_selection == 3:
         break






