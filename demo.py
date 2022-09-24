from speech_recognition import Microphone as micro, Recognizer as rec
from pythonosc.udp_client import SimpleUDPClient as udp


client = udp("127.0.0.1", 9000)
recognizer = rec()
mic = micro()


def send_to_vrc():

    with mic as source:

        audio = recognizer.listen(source)
    #
    output = recognizer.recognize_google(audio)
    
    client.send_message("/chatbox/input", [output, True])
#


while True:

    send_to_vrc()
#
