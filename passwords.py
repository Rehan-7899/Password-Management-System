import json
import os

class Passwords:
    def __init__(self):
        self.passwords={}
        self.load_passwords()
        
            
    def save_passwords(self):
        with open ("Passwords.json", "w") as f:
            json.dump(self.passwords, f, indent=4)
    
    def load_passwords(self):
        if os.path.exists("Passwords.json"):
            with open ("Passwords.json", "r") as f:
                self.passwords=json.load(f)
                
        else:
            self.passwords={}
            
    def encrypt_password(self,password):
        x=""
        for ch in password:
            x += chr(ord(ch) + 4)
        return x
    
    def decrypt_password(self,password):
        y=""
        for ch in password:
            y += chr(ord(ch) - 4)
        return y
            
    def add_password(self):
        account=input("Enter Account Name: ")
        if account in self.passwords:
            print("Account already Exists")
            return
        
        id=input("Enter ID: ")
        password=input("Enter Password: ")
        
        enc_pass=self.encrypt_password(password)
        
        self.passwords[account]={"ID": id, "Password": enc_pass}
        self.save_passwords()
        print("Password added successfully.")
        
    def delete_password(self):
        account=input("Enter Account Name to Delete: ")
        if account not in self.passwords:
            print("Account does not exist.")
            return
        
        del self.passwords[account]
        self.save_passwords()
        print("Account deleted successfully.")
    
    def view_password(self):
        account=input("Enter Account name to view password: ")
        if account not in self.passwords:
            print("Account does not exists!")
            return
        
        id=self.passwords[account]["ID"]
        passwrd=self.passwords[account]["Password"]
        dec_pass=self.decrypt_password(passwrd)
        
        print(f"ID: {id} | Password: {dec_pass}")
        
    def update_password(self):
        account=input("Enter Account name to view password: ")
        if account not in self.passwords:
            print("Account does not exists!")
            return
        
        new_pass=input("Enter New Password: ")
        enc_pass=self.encrypt_password(new_pass)
        
        self.passwords[account]["Password"] = enc_pass
        print("Password updated successfully.")
        self.save_passwords()
        
        
        
        
        
        
MASTER_PASSWORD="Rehan123"
mp=input("Enter Master Password: ")
if MASTER_PASSWORD != mp:
    print("Wrong Password! Access Denied!")
    exit()
    
print("Access Granted.")


p=Passwords()

while True:
    print("\n1.Add Password")
    print("2.Delete Password")
    print("3.View Password")
    print("4.Update Password")
    print("5.Exit")
    
    try:
        choice=int(input("Enter Choice:"))
        
    except ValueError:
        print("Invalid input!")
        continue
        
    if choice==1:
        p.add_password()
        
    elif choice==2:
        p.delete_password()
    
    elif choice==3:
        p.view_password()
        
    elif choice==4:
        p.update_password()
    
    elif choice==5:
        print("Exiting Program...")
        break
        
    else:
        print("Invalid Choice!!")

    
        