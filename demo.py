# made for a VRChat player usernamed Cachie~
from speech_recognition import Microphone, Recognizer, UnknownValueError as error
from pythonosc.udp_client import SimpleUDPClient


udp = SimpleUDPClient("127.0.0.1", 9000)
rec = Recognizer()
mic = Microphone()


def send_to_vrc():

    try:

        with mic as source:
            speech = rec.listen(source)

            text = rec.recognize_google(speech)

            udp.send_message("/chatbox/input", [text, True])
    #   #
    except error:

        pass
    #
#


while True:

    send_to_vrc()
#
