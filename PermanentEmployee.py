class Per_Emp:

      basic_salary = 5000
      def calculatesalary(self,exp):
            #2
            if exp >= 15:
                  self.basic_salary= self.basic_salary + ((self.basic_salary*20)/100)
                  return self.basic_salary
            elif exp >=10 or exp < 15: 
                  self.basic_salary= self.basic_salary + ((self.basic_salary*10)/100)
                  return self.basic_salary
            elif exp >=5 or exp <10:
                  self.basic_salary= self.basic_salary + ((self.basic_salary*5)/100)
                  return self.basic_salary
            else:
                  return self.basic_salary

                  
                  
            
