class User:
    def __init__(self, user_id, name, email, mobile, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.mobile = mobile

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password

class SimpleApp:
    def __init__(self):
        self.users = []
        self.admin = Admin("admin", "admin@12")

    def run(self):
        while True:
            print("Welcome to Simple App")
            print("1. User Signup")
            print("2. User Login")
            print("3. Admin Login")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.signup()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.admin_login()
            elif choice == "4":
                exit()
            else:
                print("Invalid choice..try again.")
        print("Thank you ")

    def signup(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        mobile = input("Enter your mobile number: ")
        user_id = len(self.users) + 1
        new_user = User(user_id, name, email, mobile,password)
        self.users.append(new_user)
        print("Registration successful!")
        print()

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for user in self.users:
            if user.email == email and user.password == password:
                print("Login successful!")
                self.user_menu()
                break
        else:
            print("Invalid email or password")

    def user_menu(self):
        print("-----------------------")
        print("User Menu")
        print("-----------------------")

    def admin_login(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")

        if self.admin.login(username, password):
            print("Admin login successful!")
            self.admin_menu()
        else:
            print("Invalid admin username or password.")

    def admin_menu(self):
        print("-------------------")
        print("Admin Menu")
        print("-------------------")


app = SimpleApp()
app.run()