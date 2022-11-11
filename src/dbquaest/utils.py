import email.message, smtplib

def email_function(mail_subject, mail_body, mail_to):

    msg = email.message.Message()
    msg['Subject'] = mail_subject
    msg['From'] = 'flavianowilliams@gmail.com'
    msg['To'] = mail_to
    password = 'epyauccqvbscutmr'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(mail_body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

def evaluate(var, option):

    alphabet_list = 'A B C D E F G H I J'.split()

    var = var.replace('[', '').replace(']', '').replace(' ', '')
    var = var.split(',')

    point_list = [float(u) for u in var]

    indx = alphabet_list.index(option)

    feedback = point_list[indx]

    return feedback
