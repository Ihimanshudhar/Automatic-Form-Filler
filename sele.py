from selenium import webdriver
import xlrd
import re
#option = webdriver.EdgeOptions()
#option.add_argument("-incognito")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
def check(email):  
  
    if(re.search(regex,email)):  
        return 1  
          
    else:  
        return 0
loc = "FormFiller\Datasheet.xls"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
sheet.cell_value(0, 0)

print("who is filling the form?") 
print("1 --> Himanshu")
print("2 --> Alak")
print("3 --> Krishna")
print("4 --> Eshan")
print("5 --> Avneesh")
choice  = int(input("Enter the number associated: "))
lst = sheet.row_values(choice)
driver = webdriver.Edge(executable_path='FormFiller\edgedriver_win64 (1)\msedgedriver.exe')
#driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfMgT75Amlf6aIGDlwZGCCwalCh4TEJyP7e0TeVbcNg-J7JpQ/viewform")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc92YUbE3MsJuwtbtz2v3_4wUPsZ5qU-h0wauavRwvUO2C4lg/viewform")
textboxes = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
counter = 1
textcounter = 0


for i in range(len(textboxes) + 1):   
    id = "i"
    id = id + str(counter)
    #print(id)
    elements = driver.find_element_by_id(id)
    # print(elements.text)
    if elements.text == "Name":
        textboxes[textcounter].send_keys(lst[0])
    elif elements.text == "E-mail":
        if check(lst[2]) == 1:
            textboxes[textcounter].send_keys(lst[2])
        else:
            print("E-mail NULL or faulty")
    elif elements.text == "Last name":
        textboxes[textcounter].send_keys(lst[1])
    elif elements.text == "Contact number":
        if len(str(lst[3])) == 12:
            textboxes[textcounter].send_keys(int(lst[3]))
        else:
            print("Phone number NULL or faulty")
    counter = counter + 4
    textcounter = textcounter + 1
a = input("press any key to continue...")
# elements = driver.find_element_by_id("i1")
# #print(len(textboxes))
# if elements.text == "Name":
#     textboxes[0].send_keys("Him")
# elif elements.text == "E-mail":
#     textboxes[0].send_keys("H@.com")
# elif elements.text == "Last name":
#     textboxes[0].send_keys("Dhar")
# elif elements.text == "Contact number":
#     textboxes[0].send_keys("7889796972")
# elements = driver.find_element_by_id("i5")
# if elements.text == "Name":
#     textboxes[1].send_keys("Him")
# elif elements.text == "E-mail":
#     textboxes[1].send_keys("H@.com")
# elif elements.text == "Last name":
#     textboxes[1].send_keys("Dhar")
# elif elements.text == "Contact number":
#     textboxes[1].send_keys("7889796972")
# elements = driver.find_element_by_id("i9")
# if elements.text == "Name":
#     textboxes[2].send_keys("Him")
# elif elements.text == "E-mail":
#     textboxes[2].send_keys("H@.com")
# elif elements.text == "Last name":
#     textboxes[2].send_keys("Dhar")
# elif elements.text == "Contact number":
#     textboxes[2].send_keys("7889796972")
# elements = driver.find_element_by_id("i13")
# if elements.text == "Name":
#     textboxes[3].send_keys("Him")
# elif elements.text == "E-mail":
#     textboxes[3].send_keys("H@.com")
# elif elements.text == "Last name":
#     textboxes[3].send_keys("Dhar")
# elif elements.text == "Contact number":
#     textboxes[3].send_keys("7889796972")
# a = input("press any key to continue...")

