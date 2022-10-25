from Object_template.Add import add_book
from Object_template.Borrow import borrow_book
from Object_template.Return import return_book
from Object_template.book import book
from Database import mariadb_context as rdbms
import json
import hashlib
import datetime
from Database.Encoder import DeptDetailsEncoder


class Database_handler():

    def __init__(self):
        self.pw="root"
        self.database="library"


    def insert_records(self,record_type,ISBN13,username,quantity,date,return_status):
        SQLstatement="INSERT INTO records (type, ISBN13, username, quantity,date,return_status) VALUES (%s,%s,%s,%s,%s,%s);"
        values=(record_type,ISBN13,username,quantity,date,return_status)
        return[[SQLstatement,values]]

    def update_records(self,ISBN13,username):
        SQLstatement='''update records set return_status ="Y" where id =(SELECT MIN(id) FROM records WHERE ISBN13=%s AND  username=%s  AND return_status="N" );'''
        values=(ISBN13,username)
        return[[SQLstatement,values]]

    def update_book(self,quantity, ISBN13):
        SQLstatement="UPDATE book SET availability= %s WHERE ISBN13=%s;"
        values=(quantity,ISBN13)
        return[[SQLstatement,values]]
    
    def update_book_full(self,availability,total,ISBN13):
        SQLstatement="UPDATE book SET availability= %s, total=%s WHERE ISBN13=%s;"
        values=(availability,total,ISBN13)
        return[[SQLstatement,values]]



    def insert_book(self,ISBN13,title,total):
        SQLstatement='''INSERT INTO book 
                        VALUES(%s,%s,%s,%s
                        );'''
        values=(ISBN13,title,total,total)
        return[[SQLstatement,values]]



    def Qurery(self,SQLQuery,inputs):
        with rdbms.MariaDBCursor(password=self.pw, database=self.database) as rdbms_cursor:
            rdbms_cursor.execute(SQLQuery,inputs)
            rows = rdbms_cursor.fetchall()
            return rows


    def Change(self,sqlqurylist:list):
        with rdbms.MariaDBCursor(password=self.pw, database=self.database) as rdbms_cursor:
            for list in sqlqurylist:
                rdbms_cursor.execute(list[0],list[1])

    def search_by_keyword(self,keyword):
        book_list=[]
        book_json=""

        book_SQL_records= self.Qurery("""SELECT ISBN13,title,availability,total FROM book WHERE title LIKE %s;""",('%' + keyword + '%',))
        if not book_SQL_records:
            return None
        for book_record in book_SQL_records:
            book_list.append(book(book_record))
        
        book_json =json.dumps(book_list, indent=4, cls=DeptDetailsEncoder)
        return book_json


    def search_by_ISBN(self,ISBN13):
        book_list=[]
        book_json=""
        ISBN13=str(ISBN13)

        book_SQL_records= self.Qurery("SELECT ISBN13,title,availability,total FROM book WHERE ISBN13=%s;", (ISBN13,) )
        if not book_SQL_records:
            return None
        for book_record in book_SQL_records:
            book_list.append(book(book_record))
        
        book_json =json.dumps(book_list, indent=4, cls=DeptDetailsEncoder)
        return book_json


    def authenticate(self,username,password):
        book_SQL_records=self.Qurery("SELECT sha224_password,user_group FROM person where username =%s;", (username,) )
        if book_SQL_records:
            sha224_input_password=hashlib.sha224(bytes(password)).hexdigest()
            return (book_SQL_records[0][0]==sha224_input_password,book_SQL_records[0][1])
        return None

    def Borrow(self,Borrow_obj:borrow_book):
        message=""
        #check user exist
        if self.authenticate(Borrow_obj.username,Borrow_obj.password)==None:
            message=f"User {Borrow_obj.username} does not exists"
            return json.dumps({"message":message})
        # check user password
        elif self.authenticate(Borrow_obj.username,Borrow_obj.password)[0]==False:
            message=f"Wrong password"
            return json.dumps({"message":message})
        #check user group
        elif self.authenticate(Borrow_obj.username,Borrow_obj.password)[1]=="librarian":
            message=f"User {Borrow_obj.username} is a librarian, only customer account can borrow book"
            return json.dumps({"message":message})
        # check book identity
        elif self.search_by_ISBN(Borrow_obj.ISBN13)==None:
            message=f"{Borrow_obj.ISBN13} is not in our database"
            return json.dumps({"message":message})
        #check stock
        elif self.Qurery("SELECT availability FROM book WHERE ISBN13=%s;", (Borrow_obj.ISBN13,))[0][0]==0:
            message=f"{Borrow_obj.ISBN13} stock is 0"
            return json.dumps({"message":message})
        else:
            currentstock=self.Qurery("SELECT availability FROM book WHERE ISBN13=%s;", (Borrow_obj.ISBN13,))[0][0]

            Action_list1=self.insert_records("borrow",Borrow_obj.ISBN13,Borrow_obj.username,1,datetime.datetime.now().date().strftime("%Y-%m-%d"),"N")
            Action_list2=self.update_book(currentstock-1,Borrow_obj.ISBN13)
            Final_Action_list=Action_list1+Action_list2
            try:
                self.Change(Final_Action_list)
            except:
                message="Database does not allow this action, please contact database manager"
                return json.dumps({"message":message})
            else:
                message="Recored updated"
                return json.dumps({"message":message})




    def Return(self,Return_obj:return_book):
            message=""
            #check user exist
            if self.authenticate(Return_obj.username,Return_obj.password)==None:
                message=f"User {Return_obj.username} does not exists"
                return json.dumps({"message":message})
            #check user password
            elif self.authenticate(Return_obj.username,Return_obj.password)[0]==False:
                message=f"Wrong password"
                return json.dumps({"message":message})
            # check user group
            elif self.authenticate(Return_obj.username,Return_obj.password)[1]=="librarian":
                message=f"User {Return_obj.username} is a librarian, only customer account can return book"
                return json.dumps({"message":message})
            # check book identity
            elif self.search_by_ISBN(Return_obj.ISBN13)==None:
                message=f"{Return_obj.ISBN13} is not in our database"
                return json.dumps({"message":message})
            # check book stock
            elif self.Qurery("SELECT availability FROM book WHERE ISBN13=%s;", (Return_obj.ISBN13,))[0][0]==self.Qurery("SELECT total FROM book WHERE ISBN13=%s;", (Return_obj.ISBN13,))[0][0]:
                message=f"{Return_obj.ISBN13} stock at max, please return to the right library"
                return json.dumps({"message":message})
            #check record
            elif self.Qurery(('''SELECT MIN(id) FROM records WHERE ISBN13=%s AND username=%s AND return_status="N"'''),(Return_obj.ISBN13,Return_obj.username))[0][0]==None:
                message=f"no rental record for book{Return_obj.ISBN13} under user {Return_obj.username}"
                return json.dumps({"message":message})
            else:
                Action_list1=self.update_records(Return_obj.ISBN13,Return_obj.username)
                currentstock=self.Qurery("SELECT availability FROM book WHERE ISBN13=%s;", (Return_obj.ISBN13,))[0][0]
                Action_list2=self.update_book(currentstock+1,Return_obj.ISBN13)
                Final_Action_list=Action_list1+Action_list2

                try:
                    self.Change(Final_Action_list)
                except:
                    message="Database does not allow this action, please contact database manager"
                    return json.dumps({"message":message})

                else:
                    message=f"1 copy of {Return_obj.ISBN13} returned"
                    return json.dumps({"message":message})


    def Add(self,Add_obj:add_book):
        message=""
        #check user exist

        if self.authenticate(Add_obj.username,Add_obj.password)==None:
            message=f"User {Add_obj.username} does not exists"

            return json.dumps({"message":message})
        #check user password
        
        if self.authenticate(Add_obj.username,Add_obj.password)[0]==False:
            message=f"Wrong password"

            return json.dumps({"message":message})
        # check user group
        if self.authenticate(Add_obj.username,Add_obj.password)[1]=="customer":
            message=f"User {Add_obj.username} is a customer, only librarian account can add book"

            return json.dumps({"message":message})
        # check book identity
        # if such record does not exist
        if not self.search_by_ISBN(Add_obj.ISBN13):

            try:
                Action_list1=self.insert_records("add",Add_obj.ISBN13,Add_obj.username,Add_obj.quantity,datetime.datetime.now().date().strftime("%Y-%m-%d"),"NA")
                Action_list2=self.insert_book(Add_obj.ISBN13,Add_obj.title,Add_obj.quantity)
                Final_Action_list=Action_list2+Action_list1
                self.Change(Final_Action_list)
            except:
                message=f"Database does not allow this action, please contact database manager"
                return json.dumps({"message":message})
            else:
                message=f"Newbook added. {Add_obj.quantity} copy of {Add_obj.ISBN13} added"
                return json.dumps({"message":message})
        else :
            current_stock ,current_total=self.Qurery("SELECT availability,total FROM book WHERE ISBN13=%s;", (Add_obj.ISBN13,))[0]
            Action_list1=self.insert_records("add",Add_obj.ISBN13,Add_obj.username,Add_obj.quantity,datetime.datetime.now().date().strftime("%Y-%m-%d"),"NA")
            Action_list2=self.update_book_full(current_stock+int(Add_obj.quantity),current_total+int(Add_obj.quantity),Add_obj.ISBN13)
            Final_Action_list=Action_list2+Action_list1
            try:
                self.Change(Final_Action_list)
            except:
                message=f"Database does not allow this action, please contact database manager"
                return json.dumps({"message":message})
            else:
                message=f"Stock topped up. {Add_obj.quantity} copy of {Add_obj.ISBN13} added"
                return json.dumps({"message":message})



                


# borrow1=borrow_book(("978-0132350884","friedrice1990","123"))

# borrow_message=Database_handler().Borrow(borrow1)
# print(borrow_message)

            
# return1=return_book(("978-0132350884","friedrice1990","123"))

# return_message=Database_handler().Return(return1)
# print(return_message)

# Add_obj=add_book(("978-0132350184","random",10,"lib123",888))
# add_message=Database_handler().Add(Add_obj)
# print(add_message)


# Action_list2=Database_handler().update_book_full(current_stock+int(Add_obj.quantity),current_total+int(Add_obj.quantity),Add_obj.ISBN13)
# Database_handler().Change(Action_list2)