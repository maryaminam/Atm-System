import pandas as pd
import tkinter as tk
from tkinter import *
import customtkinter as ctk
from tkinter import Canvas, Text
from tkinter import messagebox
# calling recogniser from face_recog for login
from recogniser import *

root = ctk.CTk()
root.title("Kashkoal Banking System Project")

canvas = tk.Canvas(root, height=700,width=700,bg='#212325')
canvas.pack()

df=pd.read_csv(r'project.csv')


class Pin:
    def pinLogin():
        canvas.delete('all')
        canvas.create_text(300, 40, text="Enter ID and PIN", fill="#b2bec3", font=('Symbola 20 bold'))
        canvas.pack()

        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

        

        player_name = Entry(frame, bg='#4b4b4b', fg='white',font='Symbola 10')
        player_name.pack(pady=20)

        Label(frame,text="ID", pady=10, fg='white',bg='#2a2d2e').pack()

        player_name2 = Entry(frame, bg='#4b4b4b', fg='white',font='Symbola 10')
        player_name2.pack(pady=20)
        Label(frame,text="PIN", pady=10, fg='white',bg='#2a2d2e').pack()
        

        def LoginFile():
            verified=False
            try:
                id = int(player_name.get())
                pin = int(player_name2.get())

            except:
                tk.messagebox.showinfo("Error", "Enter The Id and Pin in Digits")


            for i in range(3):
                if id==df.loc[i,"Acc. No"] and pin==df.loc[i,"Password"]:
                    print("Welcome ",(df.loc[i,"Name"]))
                    global balance
                    balance=(df.loc[i,"Balance"])
                    name=(df.loc[i,"Name"])
                    verified = True
                    
                    

            if verified != True:
                tk.messagebox.showinfo("Error", "You've entered the wrong id or password!")
                exit()
                
            canvas.delete('all')
            canvas.create_text(300, 40, text="Welcome "+name, fill="#b2bec3", font=('Symbola 20 bold'))
            canvas.pack()

            frame = tk.Frame(root, bg='#2a2d2e')
            frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

            ctk.CTkButton(frame,text="Continue", padx=10, pady=25,command=pageThree.ThirdPage).pack()
        ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=LoginFile).pack()






class Process:
    def Login():
        canvas.delete('all')
        canvas.create_text(300, 40, text="Enter ID", fill="#b2bec3", font=('Symbola 20 bold'))
        canvas.pack()

        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

        

        player_name = Entry(frame, bg='#4b4b4b', fg='white',font='Symbola 10')
        player_name.pack(pady=50)

        

        def LoginFile():
            verified=False
            try:
                pin = int(player_name.get())

            except:
                tk.messagebox.showinfo("Error", "Enter The Pin in Digits")
                
            for i in range(3):
                if pin==df.loc[i,"Acc. No"]:
                    print("Welcome ",(df.loc[i,"Name"]))
                    global balance

                    balance=(df.loc[i,"Balance"])
                    
                    verified = True
                    
                    

            if verified != True:
                tk.messagebox.showinfo("Error", "Id doesn't exist")
                exit()
                    
            
            recognise.login()
            canvas.delete('all')
            canvas.create_text(300, 40, text="Press Continue", fill="#b2bec3", font=('Symbola 20 bold'))
            canvas.pack()

            frame = tk.Frame(root, bg='#2a2d2e')
            frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

            ctk.CTkButton(frame,text="Continue", padx=10, pady=15,command=pageThree.ThirdPage).pack()
        ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=LoginFile).pack()
    


class Withdrawing(Process):
    def withdrawAmount():
        canvas.delete('all')
        canvas.create_text(300, 40, text="Enter The Amount", fill="#b2bec3", font=('Symbola 20 bold'))
        canvas.pack()


        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)
        def withdraw():
            try:
                amount = int(player_name.get())

            except:
                tk.messagebox.showinfo("Error", "Enter The Amount in Digits")
                
            if amount>=500 and amount<50000 and amount<balance:
                canvas.delete('all')
                canvas.create_text(300, 40, text="Enter The Amount", fill="#b2bec3", font=('Symbola 20 bold'))
                canvas.pack()


                frame2 = tk.Frame(root, bg='#2a2d2e')
                frame2.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

                Label(frame2, text=f'{amount}rs Withdrawn!', pady=20, fg='white',bg='#2a2d2e').pack()
                new_balance=balance-amount
                df.replace (to_replace= balance, value=new_balance, inplace=True)
                df.to_csv(r'project.csv', index=False)  


                FinishButton = ctk.CTkButton(frame2, text="Finish",pady=30, padx=10 , bg="#16a085", command=Ty.ThankYou)
                FinishButton.pack()

                PerformButton = ctk.CTkButton(frame2, text="Perform another transaction",pady=30, padx=10 , bg="#16a085", command=PageFour)
                PerformButton.pack()



            elif amount>50000:
                Label(frame,text="Maximum Amount to withdraw is 50,000\n Enter the amount again!", pady=20, fg='white',bg='#2a2d2e').pack()


            elif amount<500:
                Label(frame,text="Enter the amount more than 500!", pady=20, fg='white',bg='#2a2d2e').pack()

                
            elif amount<balance:
                Label(frame,text="Insufficient Balance!", pady=20, fg='white',bg='#2a2d2e').pack() 
            
            

        player_name = Entry(frame, bg='#4b4b4b', fg='white',font='Symbola 10')
        player_name.pack(pady=50)

        ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=withdraw).pack()
 



class Ty:
    def ThankYou():
        canvas.delete('all')
        canvas.create_text(300, 40, fill="#b2bec3", font=('Symbola 20 bold'))
        canvas.pack()


        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)


        Label(frame,text="Thankyou!\n for trusting\n and \nusing our atm \n;)", pady=200, fg='white',bg='#2a2d2e',font=('Symbola 20 bold')).pack()




class Transfering(Process):
    def person():
        canvas.delete('all')
        canvas.create_text(300, 40, text="Enter The Id you want to send Money", fill="#b2bec3", font=('Symbola 20 bold'))
        canvas.pack()


        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)
        def id():
            personId= int(player_name.get())
            verified=False
            for i in range(3):
                if personId==df.loc[i,"Acc. No"]:
                    namePerson=(df.loc[i,"Name"])
                    global transferPerson_balance
                    transferPerson_balance=(df.loc[i,"Balance"])

                    ask=tk.messagebox.askquestion("Error", "Are you sure you want transfer money to "+ namePerson)
                    if ask=='yes':
                        canvas.delete('all')
                        canvas.create_text(300, 40, text="Enter The Id you want to send Money", fill="#b2bec3", font=('Symbola 20 bold'))
                        canvas.pack()


                        frame = tk.Frame(root, bg='#2a2d2e')
                        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

                        nextButton = ctk.CTkButton(frame, text="Next",pady=30, padx=10 , bg="#16a085", command=Transfering.moneyTransfer)
                        nextButton.pack()


                    if ask=='no':
                        exit()

                    
                    verified = True
                    
                    

            if verified != True:
                tk.messagebox.showinfo("Error", "Id doesn't exist")
                exit()
        



        player_name = Entry(frame, bg='#4b4b4b', fg='white',font='Symbola 10')
        player_name.pack(pady=50)

        ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=id).pack()




    def moneyTransfer():

        canvas.delete('all')
        canvas.create_text(300, 40, text="Enter The Amount", fill="#b2bec3", font=('Symbola 20 bold'))
        canvas.pack()


        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

        def transfer():
            try:
                amount = int(player_name.get())

            except:
                Label(frame,text="Enter the Amount in Digits!", pady=20, fg='white',bg='#2a2d2e').pack()


            if amount>=500 and amount<50000 and amount<balance:
                canvas.delete('all')
                canvas.create_text(300, 40, text="Select", fill="#b2bec3", font=('Symbola 20 bold'))
                canvas.pack()


                frame2 = tk.Frame(root, bg='#2a2d2e')
                frame2.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)


                Label(frame2, text=f'{amount}rs Transferred!', pady=20, fg='white',bg='#2a2d2e').pack()
                new_balance=balance-amount
                add_balance=amount+transferPerson_balance

                df.replace (to_replace= transferPerson_balance, value=add_balance, inplace=True)
                df.to_csv(r'project.csv', index=False)

                df.replace (to_replace= balance, value=new_balance, inplace=True)
                df.to_csv(r'project.csv', index=False)
                

                FinishButton = ctk.CTkButton(frame2, text="Finish",pady=30, padx=10 , bg="#16a085", command=Ty.ThankYou)
                FinishButton.pack()

                PerformButton = ctk.CTkButton(frame2, text="Perform another transaction",pady=30, padx=10 , bg="#16a085", command=PageFour)
                PerformButton.pack()


            elif amount>50000:
                Label(frame,text="Maximum Amount to Transfer is 50,000 \n Enter the amount again!", pady=20, fg='white',bg='#2a2d2e').pack()



            elif amount<500:
                Label(frame,text="Enter the amount more than 500!", pady=20, fg='white',bg='#2a2d2e').pack()

                
            elif amount<balance:
                Label(frame,text="Insufficient Balance!", pady=20, fg='white',bg='#2a2d2e').pack()  

            

        player_name = Entry(frame, bg='#4b4b4b', fg='white',font='Symbola 10')
        player_name.pack(pady=50)

        ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=transfer).pack()



class Depositing(Process):
    def moneyDeposit():

        canvas.delete('all')
        canvas.create_text(300, 40, text="Enter The Amount", fill="#b2bec3", font=('Symbola 20 bold'))
        canvas.pack()


        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)
        def deposit():
            try:
                amount = int(player_name.get())

            except:
                Label(frame,text="Enter the Amount in Digits!", pady=20, fg='white',bg='#2a2d2e').pack()

                
            if amount>=500 and amount<50000:
                canvas.delete('all')
                canvas.create_text(300, 40, text="Select", fill="#b2bec3", font=('Symbola 20 bold'))
                canvas.pack()


                frame2 = tk.Frame(root, bg='#2a2d2e')
                frame2.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)
    

                Label(frame2, text=f'{amount}rs Deposited!', pady=20, fg='white',bg='#2a2d2e').pack()
                new_balance=balance+amount
                df.replace (to_replace= balance, value=new_balance, inplace=True)
                df.to_csv(r'project.csv', index=False)
                

                FinishButton = ctk.CTkButton(frame2, text="Finish",pady=30, padx=10 , bg="#16a085", command=Ty.ThankYou)
                FinishButton.pack()

                PerformButton = ctk.CTkButton(frame2, text="Perform another transaction",pady=30, padx=10 , bg="#16a085", command=PageFour)
                PerformButton.pack()


            elif amount>50000:
                Label(frame,text="Maximum Amount to Deposit is 50000, Enter the amount again!", pady=20, fg='white',bg='#2a2d2e').pack()


            elif amount<balance:
                Label(frame,text="Insufficient Balance!", pady=20, fg='white',bg='#2a2d2e').pack()
                

                
            
            

        player_name = Entry(frame, bg='#4b4b4b', fg='white',font='Symbola 10')
        player_name.pack(pady=50)

        ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=deposit).pack()


class Balance(Process):
    def balanceInquiry():
        canvas.delete('all')
        canvas.create_text(300, 40, text="Balance", fill="#b2bec3", font=('Symbola 20 bold'))
        canvas.pack()


        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

        Label(frame,text='Current Balance is: ' + str(balance), pady=20, fg='white',bg='#2a2d2e',font=('Symbola 15 bold') ).pack()
        FinishButton = ctk.CTkButton(frame, text="Finish",pady=30, padx=10 , bg="#16a085", command=Ty.ThankYou)
        FinishButton.pack()

        PerformButton = ctk.CTkButton(frame, text="Perform another transaction",pady=30, padx=10 , bg="#16a085", command=PageFour)
        PerformButton.pack()



    
# defining page four

def PageFour():
    canvas.delete('all')
    canvas.create_text(300, 40, text="Select The Action To Perform", fill="#b2bec3", font=('Symbola 20 bold'))
    canvas.pack()


    frame = tk.Frame(root, bg='#2a2d2e')
    frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)



    withdrawButton = ctk.CTkButton(frame, text="Cash Withdrawal",pady=30, padx=10 , bg="#16a085", command=Withdrawing.withdrawAmount)
    withdrawButton.pack()


    transferButton = ctk.CTkButton(frame, text="Transfer Money",pady=30, padx=10 , bg="#16a085", command=Transfering.person)
    transferButton.pack()


    depositButton = ctk.CTkButton(frame, text="Deposit Money",pady=30, padx=10 , bg="#16a085", command=Depositing.moneyDeposit)
    depositButton.pack()


    balanceButton = ctk.CTkButton(frame, text="Balance inquiry",pady=30, padx=10 , bg="#16a085", command=Balance.balanceInquiry)
    balanceButton.pack()







# defining page one

class PageOne:
    canvas.create_text(300, 40, text="Choose Login Method", fill="#b2bec3", font=('Symbola 25 bold'))
    canvas.pack()


    frame = tk.Frame(root, bg='#2a2d2e')
    frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)



    PinButton = ctk.CTkButton(frame, text="PIN", pady=10, padx=10 , bg="#16a085", command=Pin.pinLogin)
    PinButton.place(x=100 ,y=130)



    FaceButton = ctk.CTkButton(frame, text="Biometric",pady=10, padx=10 , bg="#16a085", command=Process.Login)
    FaceButton.place(x=100,y=200)

# defining page three

class pageThree:
    def ThirdPage():
        canvas.delete('all')
        canvas.create_text(300, 40, text="Choose Your Account Type:", fill="#b2bec3", font=('Symbola 25 bold'))
        canvas.pack()


        frame = tk.Frame(root, bg='#2a2d2e')
        frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)



        savingButton = ctk.CTkButton(frame, text="Saving Account", pady=10, padx=10 , bg="#16a085", command=PageFour)
        savingButton.place(x=100 ,y=130)


        currentButton = ctk.CTkButton(frame, text="Current Account",pady=10, padx=10 , bg="#16a085", command=PageFour)
        currentButton.place(x=100,y=200)


root.mainloop()