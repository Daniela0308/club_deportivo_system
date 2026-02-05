from club_poo.config.messages import MESSAGES

def get_message(code):
    """MAP entre códigos internos del sistema y mensajes para el usuario"""
    return MESSAGES.get(code, None)
