f='f'
print(id(f))
print(type(f))
def my_func():
    return "all of it will be better than before i`m sure"
print(my_func())
job_title="Software Engineer"
job_salary=100000
job_location="New York"
print(f"job_title: {job_title}, job_salary: {job_salary}\njob_location: {job_location}")
class Job:
    def __init__(self, title, salary, location):
        self.title=title
        self.salary=salary
        self.location=location
    def display_job_info(self):
        print(f"Job Title: {self.title}, Salary: {self.salary}, Location: {self.location}")

Job("Software Engineer", 100000, "New York").display_job_info()        

job1=Job("Data Scientist", 120000, "San Francisco")
print(job1.salary)
# help(int)
job_salary=10
job_salary.__add__(59)
print("-------------------------------------")
