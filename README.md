# Cyber-Security-Base-Project-1

Here I have developed a quick project to demonstrate some of the most common cyber-security flaws in websites today. I have implemented 5 out of the 10 most common cyber-security flaws according to [OWASP Top Ten](https://owasp.org/www-project-top-ten/) (2022). This has been a part of the course [Cyber Security Base 2022](https://cybersecuritybase.mooc.fi/module-3.1). The project is very bare bones as the focus is on demonstrating issues and not on the project itself.

## The application

The application which I have developed is the beginning to an online banking service. Currently there aren't many features present as this was not the focus. There is the possibility to create accounts of either normal or admin status. 

#### Features

- Create an account of either normal or admin status.
- Get information about all accounts.

#### Flaws

- Flaw 1: CSRF flaw. When registering an account there is a vulnerability of SQL-injection.
  - Solution: Parameterize all user inputed data.

- Flaw 2: Identification and Authentication Failures. When checking the passwords given when creating an account there should also be some encryption done. This is not the case.
  - Solution: Implement proper password quality testing like length, include both uppercase and lowercase, numbers. 
  - Solution 2: Implement password encryption. Passwords are currently stored unencrypted in the database.
  
- Flaw 3: Security Logging and Monitoring Failures. At certain points in the applications user activity should be logged so that in case of malicious activity there can be better forensics. This is currently not done at all.
  - Solution: Use the "document_to_log" function which is present in database_handler
  
- Flaw 4: Broken Access Control. This flaw consits of no check that user who calls this method is actually a superuser. Although there is no button to click to call this function currently it can still be hardwritten into the url: /account_information
  - Sollution: Implement superuser check before querying for accounts.
               Implement @login_required
    example: if request.user.is_superuser:
                  Only if this is true execute the code which fetches all account_information.
                  
- Flaw 5: Security Misconfiguration. Specifically: Default accounts and their passwords are still enabled and unchanged.
  - Solution: Default test accounts with very simple passwords have not been removed.
  
## Installing Instructions

- Clone the repository to your local machine
- Perform database migrations:
  - python3 manage.py makemigrations
  - python3 manage.py migrate

- Run server:
  - python3 manage.py runserver
  
- Paste 127.0.0.1:8000/ into url.
