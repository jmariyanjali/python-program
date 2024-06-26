class IT:
    def IT_details(self,name,age,company_name,location):
        print("Name of the employee",name)
        print("Age of the employee",age)
        print("nameof the company",company_name)
        print("location of the company", location)
#child class
class HR(IT):
    def HR_details(self,salary,skill):
        print("salary of the employee",salary)
        print("skill of the employee",skill)
employee = HR()
employee.IT_details("Amit",28,"Apex_code","Hyderabad")
employee.HR_details(65000,"finding,hiring,training and supporting the new employees")