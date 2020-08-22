import sqlite3
class myconnect:
      
      def __init__(self):
            #4
            self.conn = sqlite3.connect("emp1.db")
            #5      
            try:
                  self.conn.execute('''create table if not exists emp1(name text, salary integer , emp_type char)''')
                  print('table is created')
            except:
                  pass
      
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            self.conn.execute("insert into emp1 values (?,?,?)",(ename,esalary,etype))
            self.conn.commit()
            print("record added")

      def display(self):
            #7
            name = input("Enter the emp name : ")
            data = self.conn.execute("select * from emp1 where name=?",(name,))
            #print(data.fetchall())

            for i in data:
                  print(i[0])
                  print(i[1])
                  print(i[2])