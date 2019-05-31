import smtplib
carriers = {
    'att':    '@mms.att.net',
    'tmobile':' @tmomail.net',
    'verizon':  '@vtext.com',
    'sprint':   '@messaging.sprintpcs.com'
}


def send(message):
    to_number = '#1234561234#{}'.format(carriers['sprint'])
    auth = ('#email#', '#app password#')

    # Establish a secure session with Gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    server.sendmail(auth[0], to_number, message)


print("What is your message?: ")
message = input()
send(message)
