import os
import email.message, smtplib, random

def email_function(mail_subject, mail_body, mail_to):

    sender = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    msg = email.message.Message()
    msg['Subject'] = mail_subject
    msg['From'] = sender
    msg['To'] = mail_to
    password = password
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(mail_body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

def random_vars(input, ntest):

    list = [input[0]+(input[1]-input[0])*(i+1)/ntest for i in range(ntest)]

    indx = random.sample(range(0,ntest),ntest)

    output_list = [round(list[u],2) for u in indx]

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

    indx = alphabet_list.index(option)

    feedback = var[indx]

    return feedback

def string_format(string):

    string = string.replace('[', '').replace(']', '').replace('\cdot', 'cdot')
    string = string.replace('x0c','f').replace('x0b','v').replace('x07','a').replace('x08','b')
    string = string.replace('\r', 'r').replace('\lambda', 'lambda').replace('\phi','phi')
    string = string.replace('\Delta', 'Delta').replace('\int', 'int').replace('\m', 'm')
    string = string.replace('\Phi', 'Phi').replace('\h', 'h').replace('\pi', 'pi').replace('\o', 'o')
    string = string.replace('\s', 's').replace('\g', 'g')

    list = string.split(',')

    return list