# Made by Parker Cranfield
import yagmail

email = input("persons email: ")
subject = input("subject of email: ")
contents = input("what do you want to say: ")

yag = yagmail.SMTP('(your email)', '(your password)')
yag.send(to = str(email), subject = str(subject), contents = str("contents"))
