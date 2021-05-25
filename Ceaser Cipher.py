# Python codes for Caesar Cipher for encryption 
def ceaserencrypt(text, s):

    t = list(text)
    textt=[]
    for i in range(len(t)):

     #Encrypting uppercase characters
       if (t[i].isupper()):
          k = chr((ord(t[i]) + int(s) - 65) % 26 + 65) 
          textt.append(k)

      # Encrypting lowercase characters
       elif (t[i].islower()):
          k =  chr((ord(t[i]) + int(s) - 97) % 26 + 97)
          textt.append(k)

      # Checking empty list index 
       else:
         textt.append(" ")

    texttt =""
    return (texttt.join(textt))
 
#checking the ceaserencrypt function
text = input("Please give the plaintext : ")      #CEASER CIPHER
s = input("Please give the shift number : ")      #13


print ("Ciphertext : ", ceaserencrypt(text, s))


