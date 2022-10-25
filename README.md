# Library Management System
![Final-outcome](.\Pictures\Final-outcome.png)
# Objective
Create a web based user interface for library kiosk. This kiosk provides 4 types of services to Customer and Librarian;
- **Search Book** This function allows Librarian and Customer to Search for a particular book in the database. Search criteria can be ISBN or Keyword in the book title
- **Borrow Book** This function allow Customer(Only Customer) to borrow book. Customer have to enter the book ISBN number to borrow the book, and they will be directed to an authentication page to confirm their identity.Once their identity is confirmed, the database will insert a borrow record in the database.
- **Borrow Book** This function allow Customer(Only Customer) to return book. Customer have to enter the book ISBN number to return the book, and they will be directed to an authentication page to confirm their identity. Once their identity has been confirmed, the database will find their rental record and update the record
- **Add Book** This function allow Librarian (Only Librarian) to add new book to the database. It takes in 3 input parameters, ISBN, book title and quantity. Librarian will be directed to an authentication page to confirm their identity. If the ISBN of the book already exist in the library database, the system will update the 
# Project Break Down
The project consists of 3 parts, Front-end, Back-end and Database
## **Front-end**
Using **React Framework**. Front end will look like the wire-frame in the document. It gathers user input and pass it as a message to the server. The server will process it at the Back-end.

## **Back-end**
Using **Flask Framework** Based on the incoming message from Front-end, the back end will call different functions to interact with the database and pass the output to the Front-end.

## **Database**
The Database store 3 sets of information, Book, Transaction Record and Users.


# Wire-frame
![Wire-frame](.\Pictures\wireframe.png)

# Activity Diagram
![Activity Diagram](.\Pictures\activity-diagram.png)

# Use Case Diagram
![Use Case Diagram](.\Pictures\use-case.png)

# Entity Relationship Diagram
![Entity Relationship Diagram](.\Pictures\ER-Diagram.png)

# How to set up

## Windows

### **Front-end**
Install Node and navigate to **.\Frontend** folder.
Run NPM install
Run NPM start

### **Back-end**
Activate Python virtual environment
Pip installl -r requirements.txt
navigate to **.\Backend\Root** folder.
Python main.py


### **Database**
Install Maria DB and execute the SQL statement in **.\Database** Folder

*need to change the connector setting in 
**.\Backend\Root\Database\mariadb_context.py**

## Windows
Docker file building, please refer to other repo