# BirthdayReminder

import time 
  

birthday = input("Enter b'day in dd-mm-yyyy format:")
bd = birthday.split("-")


def checkBirthday(): 
    today = time.strftime('%d-%m')
    flag = 0
    
    if today in birthday: 
        flag =1
        print("Your birthday is today")
        
        
    if flag == 0:
        def calculate_days(bd, now):
            if(bd[1] == time.strftime('%m')):
                date1 = int(bd[0])
                date2 = int(time.strftime('%d'))
                if(date1>date2):
                    days = date1 - date2
                    print("You have",days,"day(s) till your birthday")
                elif(date2>date1):
                    days = date2-date1
                    print("Your birthday was",days,"day(s) ago")

                return days
        

            else:
                def calculate_months(bd, now):
                    date1 = int(bd[1])
                    date2 = int(time.strftime('%m'))
                    if(date1>date2):
                        months = date1 - date2
                        print("You have",months,"month(s) till your birthday")
                    elif(date2>date1):
                        months = date2 - date1
                        print("Your birthday was",months,"month(s) ago")

                    return months
                    
                        
                        
            return calculate_months(bd,now)
        return calculate_days(bd,now)
        


        def show_info(self):
            pass
          
if __name__ == '__main__':
    now = time.strftime('%m')
    checkBirthday()
