from winotify import Notification, audio

notificaçao = Notification(app_id="GIT HUB", title="GIT HUB", msg="CLIQUE NO BOTÃO ABAIXO PARA IR AO GIT", duration="short")

notificaçao.set_audio(audio.Mail, loop=False)
notificaçao.add_actions(label="Aprenda Python", launch="https://github.com/MaykonOliveiraC")

#icon = imagens na notificação
                           
notificaçao.show()