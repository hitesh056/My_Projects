#Threading for timeout
#GUI for good Interface


import time
import datetime
import re
import random
#import send_email

print (' Welcome to Net Banking ')

class bank:
    def rtc(self):
        time_now = str(datetime.datetime.now())
        time_now = re.split(' ',time_now)
        return time_now
    def email(self):
        while True:
            e_mail = input('Enter your E-mail: ')
            co = ['.','@']
            e_list = list(e_mail)
            if co[0] in e_mail:
                if co[1] in e_mail:
                    break
                else:
                    print ('Email ID is not correct')
            else:
                 print ('Email ID is not correct')
        mail = e_mail
        return mail
        
    def reset_password(self):
        while True:         #To check confirm password
            a1 = 0
            b1 = 0
            c1 = 0
            d1 = 0
            while (a1!=1 or b1!=1 or c1!=1 or d1!=1):
                
                    
                print ('Password must contain upper/lower case Character,Numberic and Special character.')
                pa_password = input('Enter password: ')
                co1 = ['!','@','#','$','%','^','&','*']
                co2 = ['1','2','3','4','5','6','7','8','9','0']
                
                for a in co1:
                    b = pa_password.count(a)
                    if b>0:
                        a1 = 1
                        break
                else:
                    print ('Special character is not present')
                for a in co2:
                    b = pa_password.count(a)
                    if b>0:
                        b1 = 1
                        break
                else:
                    print ('Number is not present')

                for a in pa_password:
                    
                    if a.isupper():
                        c1 = 1
                        break
                else:
                    print ('Upper character is not present')
                for a in pa_password:
                    
                    if a.islower():
                        d1 = 1
                        break
                else:
                    print ('Lower character is not present')
            self.c_password = input('Enter password again to confirm: ')
            if pa_password == self.c_password:
                break
            else:
                print ('Wrong password')
        password = pa_password
        return password
    
    def signup(self):
        print ('     SIGNUP      ')
        print (' Press "e" to Exit ')
        print (' Enter details : ')
        self.f_name=input(' Enter your first name: ')
        if self.f_name ==' e ':
            return
        
        self.l_name = input('enter your last name: ')
        self.u_name = input('Enter User name: ')
        self.p_password = self.reset_password()
        self.e_mail = self.email()
        date_time = self.rtc()
        c_id = open('Customer_Details.csv','a')
        c_id.write('\n')
        c_id.write(self.f_name+','+self.l_name+','+self.u_name+','+self.p_password+','+self.e_mail+','+date_time[0]+','+date_time[1])
        c_id.close()
        
        A_detail = open('Account_Details.csv','a')
        A_detail.write('\n')
        A_detail.write(self.u_name+',New Account,-,10000,10000')
        A_detail.close()
        print ('Signup Successful')
        print ('Account has been credited with 10000 rupees')
            
    def login(self):
        print ('LOGIN')
        self.flag = [0]
        ct=1
        while ct<4:
            if self.flag[0] == 1:
                break
            else:
                
                ct+= 1
                c_user = input('Enter User_ID: ')
                c_password = input('Enter Password: ')
                c_id = open('Customer_Details.csv','r')
                self.get = (c_id.read().split('\n'))
                c_id.close()
                
                for a1 in self.get:     #Store Customer Details
                    b = a1.split(',')
                    if len (b)>1:
                        if c_user == b[2] and c_password == b[3]:
                            print (c_user , c_password)
                            self.flag[0] = 1
                            self.flag.append(b[0])
                            self.flag.append(b[1])
                            self.flag.append(b[2])
                            self.flag.append(b[3])
                            self.flag.append(b[4])
                            print ('Welcome',b[0],b[1])
                            break
                else:
                    print ('Wrong User_ID/Password')
        else:
            print ('Forget User-ID/Password')
            self.flag = [2]
        return self.flag           
    def account(self):
        self.a1_select = int(input('Select option to open:\n1.Account Balance\t2.Transcation \n3.Change Password\t4.Log Out\nEnter number:  '))
        A_detail = open('Account_Details.csv','r')
        self.get1 = A_detail.read().split('\n')
        A_detail.close()
        for a2 in self.get1:
            b = a2.split(',')
            if len (b)>1:
                if b[0] == self.flag[3]: 
                    self.a_balance = str(b[4])
        #else:
         #   print 'No account details'
        if self.a1_select == 1:
            print ('Account Balance' )
            print ('User=', self.flag[3],'Amount= ',self.a_balance)   
            time.sleep(0.5)
            return 1
        elif self.a1_select == 4:
            print ('Log Out')
            return 0
        elif self.a1_select == 3:
            print ('Change Password')
            
            p_pass = input('Enter previous password: ')
            if p_pass == self.flag[4]:
                self.flag[4] = self.reset_password()
            else:
               print ('Wrong Password')
            
            c_id = open('Customer_Details.csv','r')
            self.p_change = c_id.read().split('\n')
            c_id.close()
            file_data2 = []
            date_time = self.rtc()
            for a3 in self.p_change:
                b = a3.split(',')
                if len (b)>1:
                    if b[2] == self.flag[3]:
                        index = self.p_change.index(a3)
                        b = self.flag[1:]
                        b+= date_time
                file_data1=",".join(b)
                file_data2.append(file_data1)
                
            file_data3="\n".join(file_data2)
            c_id = open('Customer_Details.csv','w')
            c_id.write('\n')
            c_id.write(file_data3)
            c_id.close()
            return 0
           
                
        elif self.a1_select == 2:
            t_type = int(input('Enter transaction type:\n1.Debit\t2.Credit\t3.Exit\nEnter number: '))
            date_time = self.rtc()
            if t_type == 1:                
                print ('Account balance= ',self.a_balance)
                d_amount = int(input('Enter amount to be debit: '))
                self.a_balance = int(self.a_balance)
                if d_amount <= self.a_balance:
                    self.a_balance-= d_amount
                    print ('\n Remaining balance = ',self.a_balance)
                    
                    A_detail = open('Account_Details.csv','a')
                    A_detail.write('\n')
                    A_detail.write(self.flag[3]+',Debit,'+str(d_amount)+',-,'+str(self.a_balance)+','+date_time[0]+','+date_time[1])
                    A_detail.close()
                    return 1
            elif t_type == 2:
                print ('Account balance= ',self.a_balance)
                d_amount = int(input('Enter amount to be credit: '))
                self.a_balance=int(self.a_balance)
                self.a_balance+=d_amount
                print ('\n Remaining balance = ',self.a_balance)
                
                A_detail = open('Account_Details.csv','a')
                A_detail.write('\n')
                A_detail.write(self.flag[3]+',Credit,'+str(d_amount)+',-,'+str(self.a_balance)+','+date_time[0]+','+date_time[1])
                A_detail.close()
                return 1
            elif t_type == 3:
                print ('Exit')
                return 1
            else:
                print ('Wrong Input')
                return 1
        else:
            print ('Wrong input')
            return 1
    
    def forget_password(self):
        print ('OTP will send to your mail ID to reset password')
        while True:
            
            rand1 = random.random()
            rand1 = int(100000*rand1)
            
            self.r_email = self.email()
            
            c_id = open('Customer_Details.csv','r')
            self.get = (c_id.read().split('\n'))
            c_id.close()
            s_flag=0
            for a1 in self.get:     #Check Customer Email
                b = a1.split(',')
                if len (b)>1:
                    if self.r_email == b[4]:
                        s_flag = 1
                        break
                    else:
                        s_flag = 0
                        
            if s_flag == 1:
                send_email.sendpass('OTP:\t'+str(rand1))
                #print rand1
                
                OTP = input('Enter OTP : ')
                if OTP == rand1:
                    re_password = self.reset_password()
                    c_id = open('Customer_Details.csv','r')
                    self.p_change = c_id.read().split('\n')
                    c_id.close()
                    file_data2 = []
                    date_time = self.rtc()
                    for a3 in self.p_change:
                        b = a3.split(',')
                        if len (b)>1:
                            
                            if b[4] == self.r_email:
                                index = self.p_change.index(a3)
                                b[3] = re_password
                                b[5] = date_time[0]
                                b[6] = date_time[1]
                        file_data1 = ",".join(b)
                        file_data2.append(file_data1)
                        
                    file_data3="\n".join(file_data2)
                    c_id = open('Customer_Details.csv','w')
                    c_id.write('\n')
                    c_id.write(file_data3)
                    c_id.close()
                    break
                else:
                    print ('Wrong OTP')      
            else:
                print ('Incorrect Email')

bank = bank()       
while True:     #To open Bank account
    L_select = int(input('Select option to open account\n 1.Login\t 2.Signup\n Enter number: '))
    if L_select == 2:
        bank.signup()
    elif L_select == 1:
        a = bank.login()
        if a[0] == 2:
            bank.forget_password()
        while a[0] == 1:     #time out 5 minutes
            #time1=time.clock()
            #print time1
            #if time1>300.0:
            
               # break
            a[0] = bank.account()      
    else:
        print ('Wrong Input')
        
        
