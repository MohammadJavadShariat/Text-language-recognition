print("Hello! \nAre you ok? \n Please enter a text so that I can tell you whether it is written in English or Farsi.😊")
text = input("Enter your desired text:\n")
#Suggested text:
#سلام من mohammad javad هستم. بنده درحال آموزش زبان python هستم.

def Check_Language(text): #To check the written language
    """
    With the help of this function, you can check what percentage of the entered text is English and what percentage is Fasi.  
    Enter an English or Farsi text or a combination of both.  
    """
    EN = {'9','8','7','6','5','4','3','2','1','0','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    FA = {'۹','۸','۷','۶','۵','۴','۳','ی', 'ه', 'و', 'ن', 'م', 'ل', 'گ', 'ک', 'ق', 'ف', 'غ', 'ع', 'ظ', 'ط', 'ض', 'ص', 'ش', 'س', 'ژ', 'ز', 'ر', 'ذ', 'د', 'خ', 'ح', 'چ', 'ج', 'ث', 'ت', 'پ', 'ب' ,'آ', 'ا','۰','۱','۲'}
    Ch_FA = 0
    Ch_EN = 0
     #It separates Persian and English letters and numbers.    
    for i in text :
        if i in EN :
            Ch_EN += 1
        if i in FA :
            Ch_FA += 1
    #Find the percentage of use of each language    
    percentage1 = round(100 / (Ch_FA + Ch_EN) * Ch_EN , 2)
    percentage2 = round(100 / (Ch_FA + Ch_EN) * Ch_FA , 2)
    return percentage1 , percentage2

percentage3 , percentage4 = Check_Language(text)

#The difference in percentages
difference1 = percentage3 - percentage4
difference2 = percentage4 - percentage3

if percentage3 == percentage4 :
    print("\nThis text surprisingly has English and Persian letters equally!😱")
    
if percentage3 > percentage4 :
    if difference1 == 100 :
        print("\nThe language of this text is completely English.🥇")
    elif difference1 >= 40 :
        print("\nThe dominant language of this text is English🥇")
    elif difference1 < 40 :
        print("\nThere are more English letters in this text than Persian letters🥇")
        
if percentage3 < percentage4 :
    if difference2 == 100 :
        print("\nThe language of this text is completely Farsi.🥇")
    elif difference2 >= 40 :
        print("\nThe dominant language of this text is Farsi.🥇")
    elif difference2 < 40 :
        print("\nThere are more Persian letters in this text than English letters.🥇")

print(f"English letters: %{percentage3}\nPersian letters: %{percentage4}")



