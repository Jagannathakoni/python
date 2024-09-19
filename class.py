class Branch:
    def get_branch_data(self):
        self.bcode=int(input("Enter branch code:"))
        self.bname=input("Enter branch name:")
        self.baddress=input("Enter branch address:")

    def display_branch_data(self):
        print("Branch code is:",self.bcode)
        print("Branch name is:",self.bname)
        print("Branch address is:",self.baddress)

class Employee(Branch):
    def get_emp_data(self):
        self.empid=int(input("Enter empid:"))
        self.ename=input("Enter ename")
        self.eaddress=input("Enter eaddress:")

    def display_emp_data(self):
        print("Emp id is:",self.empid)
        print("Emp name is:",self.ename)
        print("Emp address is:",self.eaddress)

e = Employee()
e.get_branch_data()
e.get_emp_data()
e.display_branch_data()
e.display_emp_data()
