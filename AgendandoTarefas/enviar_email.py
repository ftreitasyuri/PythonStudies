from smtplib import SMTP
import email.message
import os


# Importando variáveis de ambiente
# remetente = os.getenv(MAIL_USERNAME)

def enviar_email():
    corpo_email = "Messagem que vai ser enviada no corpo do email!"

    msg = email.message.Message()
    msg["Subject"] = "Mensagem título"
    msg["From"] = os.getenv("MAIL_USERNAME")
    msg["To"] = os.getenv("MAIL_USERNAME")
    senha = os.getenv("MAIL_PASSWORD")

    msg.add_header("Content-Type", 'text/html')
    msg.set_payload(corpo_email)

    envia = SMTP("smtp.gmail.com: 587")
    envia.starttls()
    envia.login(msg["From"], senha)
    envia.sendmail(msg["From"],[msg["To"]], msg.as_string().encode('utf-8'))
    print("Email enviado!")


enviar_email()