import requests

def send_simple_message():
	return requests.post(
            "https://api.mailgun.net/v3/sandboxcca97f11898a4e9f8f15e2779848b3c5.mailgun.org/messages",
          		auth=("api", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"),
          		data={"from": "Mailgun Sandbox <postmaster@sandboxcca97f11898a4e9f8f15e2779848b3c5.mailgun.org>",
                            "to": "peter chen <meiguo1969@gmail.com>",
                            "subject": "Hello peter chen",
                            "text": "Congratulations peter chen, you just sent an email with Mailgun!  You are truly awesome!"})
