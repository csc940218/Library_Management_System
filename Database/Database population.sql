USE library;
DELETE FROM person;
DELETE FROM book;
DELETE FROM records;
INSERT INTO person 
VALUES("user1",
"6650f85110dedebf06929caf8b52f0d05bf2afd15c8462fe33ff88c9",
"customer",
"John",
"Doe",
"12345678"
);


INSERT INTO person 
VALUES("lib123",
"9ecc80ae6ace5ab6ff04a3180672f19779681f60db60229ab119832d",
"librarian",
"Micky",
"Mouse",
"99998888"
);


INSERT INTO book 
VALUES("9780132350884",
"Clean Code",
10,
10
);

INSERT INTO book 
VALUES("9780137081073",
"The Clean Coder",
5,
5
);

INSERT INTO book 
VALUES("9780201633610",
"Design Patterns",
22,
22
);

INSERT INTO records 
VALUES(1,
"borrow",
"9780201633610",
"user1",
1,
"2022-06-01",
"Y"
);

INSERT INTO records 
VALUES(2,
"borrow",
"9780132350884",
"user1",
1,
"2022-06-01",
"Y"
);