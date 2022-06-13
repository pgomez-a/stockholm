# stockholm

<img width="1163" alt="stockholm" src="https://user-images.githubusercontent.com/74931024/166300457-d3465ac4-13b6-4d84-ab8a-8a9097fac736.png">

**If you want to learn more about IT topics, [I invite you to join my Patreon channel](https://www.patreon.com/pgomeza) and visit my website:** [**IA Notes**](https://ia-notes.com/)

**stockholm** is made to allow us to enter the world of ransomware. We will try to implement a program that can infect a specific directory on a **Debian** system. The infection will encrypt all files, in **/home/infection/**, with the extensions that were used in the Wannacry attack. To find out if the encryption has been done consistently, we will also implement a decryption function to see if we recover the encrypted data.<br>

Clone the repository:

    git clone https://github.com/pgomez-a/stockholm.git ; cd ./stockholm/

Compile the program:

    make
    
Run the program:

    ./stockholm [-hvrs]
    
If the *.key file* doesn't exist before running the program, a new key will be created. If there is a key before execution, the key present in *.key* will be used.
    
The meaning of the activated flags are:
- **h/help:** to display help about the program.
- **v/version:** to get the version of the program.
- **r/reverse key:** to decrypt the messages with the given key.
- **s/silent:** to silence messages during encryption and decryption.

### What is ransomware?
**Ransomware** is a type of malware that **prevents users from accessing their system** or personal files and that requires the payment of a ransom to access them again. There are three main types of ransomware:

- **Scareware:** fake pop-up messages informing you that your system has been infected with malware and that you need to make a payment. These messages pose as security companies claiming to have detected malware. If you don't pay the ransom, you will probably have to get used to these messages.
- **Screen lockers:** you will not be able to use your computer at all. When you open your computer, you will see a full screen message asking you to make a payment. These messages might say they are from the FBI or Department of Justice so you can trust them. But the thing is, this is just a way of trying to persuade you to pay.
- **Encrypting Ransomware:** obtains and encrypts all your files, asking for payment in order to decrypt them and gain access to them again.

### Encryption
An encrypted message is a message made up of letters, symbols, and numbers that can only be understood if we have the right key to decrypt it. When it comes to data encryption, we usually talk about:
- **Symmetric encryption:** the same key is used to encrypt and decrypt data. This allows quick access to the information, although we must ensure that the key is only known by authorized users.
- **Asymmetric encryption:** these algorithms use two interrelated mathematical keys, one public and one private. The public key is used to encrypt the data, while the private key is used to decrypt the data.
