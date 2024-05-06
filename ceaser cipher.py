alphabet =['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

start_text = input("DO you want to 'encode' or 'decode'?")
text = input("Enter the text").lower()
shift_amount = int(input("What is the shift amount you want to use"))



def ceaser(start_text, shift_amount, direction):
    end_text = ""
    if direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Here is the {direction}d result: {end_text}")

   def encode(text, shift_amount):
            encoded_text = ""
            for i in text:
                position = alphabet.index(i)
                new_position = position + shift_amount
                encoded_text += alphabet[new_position]
            print(encoded_text)


        def decode(text, shift_amount):
            decoded_text = ""
            for i in text:
                position = alphabet.index(i)
                new_position = position - shift_amount
                decoded_text += alphabet[new_position]
            print(decoded_text)