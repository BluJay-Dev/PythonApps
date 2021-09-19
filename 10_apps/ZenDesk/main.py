from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket, User, Comment
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv('email')
token = os.getenv('token')
subdomain = os.getenv('subdomain')

creds = {
    'email': email,
    'token': token,
    'subdomain': subdomain
}

zenpy_client = Zenpy(**creds)

for user in zenpy_client.users():
    print(user.name)

for comment in zenpy_client.tickets.comments(ticket=2):
    print(comment.body)


zenpy_client.tickets.create(
     Ticket(description='Some description',
            requester=User(name='bob', email='bob@example.com'))
 )

ticket = zenpy_client.tickets(id=14)
ticket.comment = Comment(body="Python kinda sus", public=False)
zenpy_client.tickets.update(ticket)
