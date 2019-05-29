import smtplib
import urllib3.request
import time

#FILLOUT
GMAIL_SENDER = 'kwasiky@gmail.com'
GMAIL_PASSWORD = '' #get password if use 2factor from google
RECIPIENTS = ['kwasiky@gmail.com', 'wmstens@gmail.com', 'jtollefson8@gmail.com']
SUBJECT = 'Potm.Rocks Heartbeat alert'
CHECK_STRING = 'pumpin still'
URL_CHECK= 'https://potm.rocks/heartbeat'
#FILLOUT


def email_users(message):
    gmail_user = GMAIL_SENDER
    gmail_password = GMAIL_PASSWORD

    sent_from = gmail_user
    to = RECIPIENTS
    subject = SUBJECT
    body = message

    email_text = """  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
    except Exception as e:
        print(e)

        print('Something went wrong...')

def run():
    emailed = 0
    counter = 0
    while True:
        try:
            http = urllib3.PoolManager()
            url = URL_CHECK
            response = http.request('GET', url)
            if CHECK_STRING in str(response.data):
                counter = 0
                if emailed != 0:
                    email_users('service to potm.rocks has been restored')
                    emailed = 0
            else:
                counter += 1
            if counter >= 48 and emailed == 0:
                email_users('https://potm.rocks/heartbeat \n has not responded in the last 4 minutes, may be down due to power outage or a loss in connectivity')
                emailed = 1
            if counter >= 720 and emailed == 1:
                email_users('https://potm.rocks/heartbeat \n has not been up for over 1 hr, this sugggest that there is something wrong with the server')
                emailed = 2
        except:
            counter += 1
        finally:
            time.sleep(5)


if __name__ == '__main__':
    run()

