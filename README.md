# Library Access Management App :school:
This Applicatoion was created as a part of Hackathon conducted in IIITB. This demonstrates the use of Library Management app which utilizes Sqlite3 to store books and maintaining them.

- Team Leader : Saikiran
- Team CoLeader : Srihari

## Dependencies 🗃
<p><img src="https://img.shields.io/badge/python-<=2.7.18-FF0000?style=for-the-badge&amp;logo=python" alt="python" class="screenshot"><br/>
  <img src="https://img.shields.io/badge/pandas-0.24.2-yellow?style=for-the-badge&amp;logo=python" alt="pandas" class="screenshot"><br/>
  <img src="https://img.shields.io/badge/xlrd-1.2.0-blue?style=for-the-badge&amp;logo=python" alt="xlrd" class="screenshot"></p>

Sqlite should also be compiled with `ENABLE_UPDATE_DELETE_LIMIT` flag which enables an optional `ORDER BY` and `LIMIT` clause on UPDATE and DELETE statements. 

## Creating Database :ledger:
To create the database we can utilize the `initializer.py` to parse info from xlsx sheet and store it in database file `books.db`

## Usage :books:
The `server.py` will present three scenario to request and retrieve info of books.

In **Scenario 1** we input books Reference ID and if the books are left and are not taken by you( your username) then it updates the database or prints apporirate Response.

In **Scenario 2** we can search for books using authors,book name or genre using special characters.
For Searching based on author we give input in form of `/[Author Name Here]` and for book name `//[Book Name Here]` and for genre we directly input the genre.
