## PWD_Encrypted
_Password Generator with Fernet Encryption_
```
       ##############################################################################
       ##############################################################################
       ##  ______        ______     _____                             _           _##
       ##|  _ \ \      / /  _ \   | ____|_ __   ___ _ __ _   _ _ __ | |_ ___  __| |##
       ##| |_) \ \ /\ / /| | | |  |  _| | '_ \ / __| '__| | | | '_ \| __/ _ \/ _` |##
       ##|  __/ \ V  V / | |_| |  | |___| | | | (__| |  | |_| | |_) | ||  __/ (_| |##
       ##|_|     \_/\_/  |____/___|_____|_| |_|\___|_|   \__, | .__/ \__\___|\__,_|##
       ##                    |_____|                     |___/|_|                  ##
       ##############################################################################
       ##############################################################################
```

### SUMMARY
PWD_Encrypted is a very basic password generator written in python including Fernet.
Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography.
Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key.

### FEATURES
| PASSWORD         |       YES       |       NO      |
|:-----------------|:---------------:| -------------:|
| letters_min_MAJ  |        V        |               |
| digits           |        V        |               |
| special_char     |        V        |               |
| length_limit     |                 |       X       |
| length_choice    |        V        |               |
| single _rep.     |                 |       X       |

### SCREENSHOTS
![Screenshot](https://github.com/gelndjj/PWD_Encrypted/blob/main/img/pwd_gen.png)
![Screenshot](https://github.com/gelndjj/PWD_Encrypted/blob/main/img/pwd_dec.png)

### HOW IT WORKS - GENERATE AND ENCODE
* First off, create a token. It'll be found inside your user path and be named **pass.key**.
  1. ***note: The token MUST be present right before the password is encoded***
* Generate the password you want with the options included by clicking on **Generate**.

  1. Check off **Digits** and pick a number to include it in the password.
  2. Check off **Specials** and pick a number to include it in the password.
  3. If none of them is checked, the password will be only with letters** min/MAJ** (checked by default).
  4. ***You can erase the number inside the drop down menu and put your own.***
  
* Once created the token and generated a password, you can **Encode** it and save it wherever you want to.
   1. ***note: The token and the 'encoded password' will be asked in order to decode the password.***
* The **Clear** button clears "Your password field" and "Password encoded" field.
* The **Reset** button sets up the drop down menus to '0'

### HOW IT WORKS - DECODE
* Having the token and the "password encoded file" at hand, go to the **Decode** tab
* Load both files using the buttons, the "encoded password" will be automatically paste in the field.
* Click on **Decode** and the password will be shown in the "Password Decoded" field

### REQUIREMENTS
Librairies require to run pwd.encrypted.py

```
pip3 install tk
pip3 install itertools
pip3 install cryptography
pip3 install fernet

```
