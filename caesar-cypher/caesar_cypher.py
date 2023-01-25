from caesar_cypher_art import logo

print(logo)

end_of_game = False

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amt, cipher_direction) :
    end_text = ""
    if cipher_direction == "decode" :
        shift_amt *= -1
    for character in start_text :
        if character in alphabet :
            position = alphabet.index(character)
            new_position = (position + shift_amt) % 26
            end_text += alphabet[new_position]
        else :
            end_text += character
    print(f"The {cipher_direction}d message is {end_text}")

while not end_of_game :
    direction = input("Enter 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Enter your message:\n").lower()
    shift = int(input("Enter the shift number:\n"))
    caesar(text, shift, direction)
    choice = input("Enter 'yes' to continue or 'no' to end :\n")
    if choice == "no" :
        end_of_game = True