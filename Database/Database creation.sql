DROP DATABASE IF EXISTS library;
CREATE DATABASE IF NOT EXISTS library;
USE library;

create table person
	(username		VARCHAR(10) NOT NULL,
	 sha224_password		VARCHAR(100)NOT NULL,
	 user_group		ENUM ('librarian','customer')NOT NULL,
	 first_name    VARCHAR(50)NOT NULL,
	 last_name     VARCHAR(50)NOT NULL,
	 contact_no    INT(20)NOT NULL,
	 primary key (username)
	);
	
create table book
	(ISBN13		VARCHAR(13)NOT NULL,
	 title		VARCHAR(1000)NOT NULL,
	 availability		INT(3)NOT NULL,
	 total    int(3)NOT NULL,
	 primary key (ISBN13)
	);
	
create table records
	(id		INT(10) AUTO_INCREMENT NOT NULL ,
	 type		ENUM ('borrow','add')NOT NULL,
	 ISBN13		VARCHAR(13)NOT NULL,
	 username    VARCHAR(10)NOT NULL,
	 quantity    INT(3)NOT NULL,
	 date         DATE NOT NULL,
	 return_status ENUM ('Y','N','NA') NOT NULL,
	 primary key (id),
	 foreign key (ISBN13) references book (ISBN13) on delete cascade,
	 foreign key (username) references person (username) on delete cascade
	);