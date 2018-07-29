import pyramid_handlers
from webapp.controllers.base_controller import BaseController
import cgi
import smtplib
import sqlite3
import datetime

class MailSentController(BaseController):

    @pyramid_handlers.action(renderer='templates/mail_sent/mail_sent.pt')
    def index(self):
        self.request = None
        self.load_fresh()
        return{}

    def emailer(self, request):
        if request.method == 'GET':
            name = request.GET.get('name')
            email = request.GET.get('user_email')
            message = request.GET.get('message')
            date = datetime.datetime.today()


            # db = sqlite3.connect('db.sqlite3')
            # cur = db.cursor()
            # cur.execute('''INSERT INTO messages (name, email, message, date_sent)
            #                   VALUES(?,?,?,?)''', (name, email, message, date,))
            # db.commit()
            # cur.close()
            # db.close()

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("vandewynkel@gmail.com", "doeb pgqt fdnw pokc")

            complete_message = '\n'
            complete_message += 'Name: ' + name + '\n'
            complete_message += 'Email: ' + email + '\n'
            complete_message += 'Message: ' + message + '\n'

            server.sendmail("vandewynkel@gmail.com", "vandewynkel@gmail.com", complete_message)
            server.quit()

