# IAM-592-Final-Project
In this project, I write a basic game including historical cryptography ciphers and
their analyses to find plaintexts and ciphertexts with keys. To do this, I used all historical ciphers such as ceaser cipher, shift cipher, affine cipher, hill cipher, vigenere cipher, substitution cipher, permutation cipher. This game has mainly steps of their encryptions, decryptions and cryptographic analyses. 

## Shift Cipher 
Shift Cipher is one of the most widely known cryptographic technique which is based on modular arithmetic. In shift cipher, each letter in the plaintext is replaced by left or right n.letter. 

In encrytion, the letter x is shifted to n step right, 
$$E_{n}(x)=(x + n)\mod {26}$$

In decryption, the letter x is shifted to n step left,
$$D_{n}(x)=(x - n)\mod {26}$$ 


## Ceaser Cipher
This is the special shift cipher. Only difference is n is fixed number 3. This means that, 

In encrytion, the letter x is shifted to n step right, 
$$E_{3}(x)=(x + 3)\mod {26}$$

In decryption, the letter x is shifted to n step left,
$$D_{3}(x)=(x - 3)\mod {26}$$ 


## Hill Cipher 

The Hill cipher is a polygraphic substitution cipher based on linear algebra in classical cryptography. Each letter (in english alphabet) is represented by a number modulo 26.
A = 0 , B = 1 , C = 2, D = 3, ...... X = 23, Y = 24, Z = 25.
For example, in Turkish alphabet, there are 29 letter so if we use this alphabet, we must look at the modulo 29.
In encryption part, each block of n letters (considered as an n-component vector) is multiplied by an invertible n × n matrix, against modulus 26. In dencryption part, each block is multiplied by the inverse of the matrix used for encryption. The matrix used for encryption is the cipher key, and it should be chosen randomly from the set of invertible n × n matrices (modulo 26).



## Vigenere Cipher




## Affine Cipher 







