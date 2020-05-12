import news
import send_email as se
import manageData as mg

print("Welcome to Daily Newsletter!")
while(True):
    option = input("Want to input emails?\n(Input anything to continue, Input Q to quit): ")
    if(option != "Q"):
        mg.emailInput() 
    else:
        print("Sending emails.")
        break

# Send Emails
message = news.getNews()
print(message)
email_list = mg.getList()
for i in email_list:
    se.sendEmail(i, message)
