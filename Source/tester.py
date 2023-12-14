import datetime
email="jonni@gmail.com"
email2="@gmail.com"
email3="jonnigmail.com"
email4="jonni@"
email5="jonni@.com"
def email_check(e):
    if " " not in e:
        if "@" in e:
            temp_address=e.split("@")
            if len(temp_address) == 2:

                if temp_address[0] == '':
                    print("you need to write text before the @")
                if "." in temp_address[1]:
                    temp_address_2=temp_address[1].split(".")
                    if temp_address_2[0] == '':
                        print("you need text between @ and .")
                    if temp_address_2[1] == '':
                        print("you need a domain suffix example (.com, .is)")
                else:
                    print("you need to put a domain example ('gmail.com')")
    else:
        print("you can't have spaces in emails")

        elif len(temp_address) > 2:
            print("Only 1 @ allowed in an email")
        else:
            print(email,"an @ is required for email")

email_check(email2)