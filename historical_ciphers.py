# Python codes for Substituion Cipher encryption
def substituion_cipher_encrypt(text, shift):

    t = list(text)
    textt=[]
    for i in range(len(t)):

     #Encrypting uppercase characters
       if (t[i].isupper()):
          k = chr((ord(t[i]) + int(shift) - 65) % 26 + 65) 
          textt.append(k)

      # Encrypting lowercase characters
       elif (t[i].islower()):
          k =  chr((ord(t[i]) + int(shift) - 97) % 26 + 97)
          textt.append(k)

      # Checking empty list index 
       else:
         textt.append(" ")

    texttt =""
    return (texttt.join(textt))
 
#checking the substituion_cipher_encrypt function  
substituion_text = input("Please give the plaintext : ")      # input: naz
substituion_shift = input("Please give the shift number : ")  # input: 11


print ("The Ciphertext : ", substituion_cipher_encrypt(substituion_text, substituion_shift)) #output: ylk

# Python codes for Substituion Cipher decryption

def substituion_cipher_decrypt(text, shift):

    t = list(text)
    textt=[]
    for i in range(len(t)):

     #Encrypting uppercase characters
       if (t[i].isupper()):
          k = chr((ord(t[i]) - int(shift) - 65) % 26 + 65) 
          textt.append(k)

      # Encrypting lowercase characters
       elif (t[i].islower()):
          k =  chr((ord(t[i]) - int(shift) - 97) % 26 + 97)
          textt.append(k)

      # Checking empty list index 
       else:
         textt.append(" ")

    texttt =""
    return (texttt.join(textt))

decryption = substituion_cipher_encrypt(substituion_text, substituion_shift)

print ("The Plaintext : ", substituion_cipher_decrypt(decryption, substituion_shift))












