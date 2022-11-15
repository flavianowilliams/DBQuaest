import email.message, smtplib, random

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

def random_vars(input, ntest):

    list = [input[0]+(input[1]-input[0])*(i+1)/ntest for i in range(ntest)]

    indx = random.sample(range(0,10),10)

    output_list = [list[u] for u in indx]

    return output_list
    
def eval_float(var, option):

    alphabet_list = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()

    var = var.replace('[', '').replace(']', '').replace(' ', '')
    var = var.split(',')

    point_list = [float(u) for u in var]

    indx = alphabet_list.index(option)

    feedback = point_list[indx]

    return feedback

def eval_string(var, option):

    alphabet_list = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()

    var = var.replace('[', '').replace(']', '')
    var = var.split(',')

#    point_list = [float(u) for u in var]

    indx = alphabet_list.index(option)

    feedback = var[indx]

    return feedback
