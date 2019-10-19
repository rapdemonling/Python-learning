__author__ = "George Ling"

class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students =[]
        self.staffs =[]
    def enroll(self,stu_obj):
        print("为学员%s 办理注册手续"%stu_obj.name )
        self.students.append(stu_obj)
    def hire(self,staff_obj):
        self.staffs.append(staff_obj)
        print("雇佣新员工%s" % staff_obj.name)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course
    def tell(self):
        print('''
        ---- info of Teacher:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print("%s is teaching course [%s]" %(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade
    def tell(self):
        print('''
        ---- info of Student:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))
    def pay_tuition(self,amount):
        print("%s has paid tution for $%s"% (self.name,amount) )


school = School("Basketball","美国")

t1 = Teacher("Jordan",45,"PG",200000,"Dunk")
t2 = Teacher("Kobe",32,"PG",30000,"")

s1 = Student("Geogre",22,"SF",1001,"3 Points")
s2 = Student("Geogre",22,"PG",1002,"Dunk")


t1.tell()
s1.tell()
school.hire(t1)
school.enroll(s1)
school.enroll(s2)

print(school.students)
print(school.staffs)
school.staffs[0].teach()

for stu in school.students:
    stu.pay_tuition(5000)