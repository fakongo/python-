#!/usr/bin/python
#--coding: utf-8 --
class person(object):
    def __init__(self,name='',age=20,sex='man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self,name):
        if not isinstance(name,str):
            raise Exception('name必须为字符串 ')
        self.__name = name

    def setAge(self,age):
        if type(age) != int:
            raise Exception('age必须为字符串 ')
        self.__age = age

    def setSex(self,sex):
        if sex not in('man','woman'):
            raise Exception('sex必须为字符串 ')
        self.__sex = sex
    def show(self):
        print(self.__name,self.__age,self.__sex,sep='\n')

class Teacher(person):
    def __init__(self,name='',age=30,sex='man',department='computer'):
        #super(Teacher,self).__init__(name,age,sex)
        person.__init__(self,name,age,sex)
        self.setDepartment(department)
    def setDepartment(self,department):
        if type(department)!=str:
            raise Exception('department必须为字符串')
        self.__department=department
    def show(self):
        super(Teacher,self).show()
        print(self.__department)
if __name__=='__main__':
    zhangsan=person('zhang san',19,'man')
    zhangsan.show()
    print('='*30)
    lisi = Teacher('li si',32,'man','math')
    lisi.show()
    lisi.setAge(40)
    lisi.show()


    