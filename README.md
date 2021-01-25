# Vulnerable Web App Penetration Testing

### Repository consists of 4 simple python scripts which task is to find vulnerabilities in web apps.

Notice that all of the scripts had been run on locally hosted web application which can be found [here](https://github.com/bkimminich/juice-shop) and was created for educational purposes.

#### Screenshot of all python scripts outputs:
![](https://i.ibb.co/pQWy6Th/Zrzut-ekranu-2021-01-25-023021.png)

#### Findings
The running of scripts 01 and 02 did not reveal anything noteworthy.
Script 03 hints at possible vulnerabilities to XSS (due to lack of X-XSS-Protection) and MITM attacks (due to lack of the HSTS header). It also revealed the lack of Content-Security-Policy.
The fourth script doesn't seem to be compatible with the Web App we chose.
