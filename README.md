To compile the program:

    make
    
To run the program:

    ./stockholm [-hvrs]
    
When running, the key will be stored in .key. If there is no .key before running, a new key will be created. If there is a key before running, the present key in .key will be used.
    
The meaning of the flags are:
- h/help: to get help about the flags
- v/version: to get the version of the program
- r/reverse key: to decrypt the messages with the given key
- s/silent: to mute file message during encryptation
