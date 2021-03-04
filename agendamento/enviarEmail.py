from mail_templated import EmailMessage


def EnviarEmail(nome,estado, emailCliente):
    message = EmailMessage('paginas/email.html', {'usuario': nome, 'agendamento': estado}, 'styleOnline@gmail.com', to=[emailCliente])
    # TODO: Add more useful commands here.
    message.send()
