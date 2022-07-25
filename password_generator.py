#Password Generator Project
import random
letters_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_gen():
  #Password list generate
  password_latters_cap = [random.choice(letters_capital) for _ in range(random.randint(2, 4))]
  password_latters_sm = [random.choice(letters_small) for _ in range(random.randint(2, 4))]
  password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
  password_symbles = [random.choice(symbols) for _ in range(random.randint(2, 4))]

  password_list = password_latters_cap + password_numbers + password_symbles + password_latters_sm
  random.shuffle(password_list)

  #main password generate 
  password = "".join(password_list)
    
  return password