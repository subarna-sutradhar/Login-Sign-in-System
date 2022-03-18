import pickle
import os

print('CREDITS: SUBARNA SUTRADHAR\n')
#-----------------------------------------------

pass_l=[]
username=''
password=''
usertype=''
name=[]
pas_sgn=[]


def dashes():
    print('---------------------------------------------')

class sign_det:
    def details(self):
        global username
        self.username=input('ENTER THE USERNAME: ')
        self.usertype=input('ENTER THE USER-TYPE(OWNER/CSUTOMER): ')
        name.append(self.username)
        
    def password_log(self):
        self.password=input('ENTER THE LOG-IN PASSWORD: ')
        pas_sgn.append(self.password)
    def pass_sign(self):
        self.password=input('ENTER THE PASSWORD: ')
        pass_l.append(self.password)

    def disp(self):
        print(self.username,self.usertype,self.password)

sg=sign_det()

"""class opn_fl(sign_det):
    av01=None
    def cret(self):
        dt01='{}.dat'.format(self.username)
        self.av01=open(dt01,'wb+')
        
        

    def pck_un(self):
        pickle.dump(username,self.av01)
        pickle.dump(password,self.av01)

on=opn_fl()"""



#main prog---------------------------------------------------

while True:
    ans01=input('CONTINUE? ')
    if ans01=='N' or ans01=='n':
        break
    else:
        print('\n1.LOG IN')
        print('2.SIGN IN\n')

        dashes()

        log_sign=int(input('ENTER THE CHOICE: '))
        if log_sign==1:
            print('\nLOGGING-IN')
            sg.details()
            sg.password_log()
            for l in pas_sgn:
                l1=l
            for i in name:
                nm=i
            dt01='{}.dat'.format(nm)
            if(os.path.exists(dt01)):
                av01=open(dt01,'rb+')
                print('ALREADY A MEMBER\n')
                try:
                    while True:
                        ld01=pickle.load(av01)
                except EOFError:
                    pass
                for k in ld01:
                    if k==l1:
                        print('LOGGED IN SUCCESSFULLY\n')
                        print('YOU HAVE ENTERED THE SYSTEM')
                        dashes()

                    else:
                        print('PLEASE ENTER CORRECT PASSWORD\n')
                av01.close()
            else:
                print('PLEASE SIGN-IN')
                    
            


            dashes()
        else:
            print('\nSIGNNING-IN')

            dashes()

            sg.details()
            sg.pass_sign()
            for i in name:
                nm=i
            dt01='{}.dat'.format(nm)
            for j in pass_l:
                pas=j
            av01=open(dt01,'wb+')
            pickle.dump(pass_l,av01)
            av01.close()
            