# coding=utf-8
# -*- coding:utf-8 -*-

class Employee :
    
    '''doc test'''
    
    empCount = 0
    __hideAttr = 5
    
    def __init__(self,name):
        self.name = name
        Employee.empCount += 1
    
    def getEmpCount(self):
        return Employee.empCount
    
    def getEmpName(self):
        return self.name
    
    def __del__(self):
        className = self.__class__.__name__
        print('destroy ============== ',className)

if __name__ == '__main__' :
    emp = Employee('Bob')
    print('Total Employee Count: %d' % emp.getEmpCount())
    print('Current Employee\'s Name: %(empName)s' % {'empName':emp.getEmpName()})
    emp.age = 1
    emp.age = 2
    print(emp.age)
    print(hasattr(emp,'age'))
    print(getattr(emp,'age'))
    setattr(emp,'age',8)
    print(emp.age)
    del emp.age
    print(hasattr(emp,'age'))
    emp2 = Employee('Python')
    print(hasattr(emp2,'age'))
    
    print(emp._Employee__hideAttr)
    
    del emp
    del emp2
    
    print(Employee.__doc__)
    print(Employee.__dict__)
    print(Employee.__name__)
    print(Employee.__module__)
    print(Employee.__bases__)
    