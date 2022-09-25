# made for a vrchat player usernamed Cachie~
from speech_recognition import Microphone, Recognizer, UnknownValueError
from pythonosc.udp_client import SimpleUDPClient
from os.path import basename
from keyboard import wait


vrchat = SimpleUDPClient("127.0.0.1", 9000)
engine = Recognizer()
mic = Microphone()


print(f"\n{basename(__file__)} is now running\n\nbe silent for a moment to set the mic sensitivity\n")
with mic as back_ground_noise: engine.adjust_for_ambient_noise(back_ground_noise, duration=2)
print(f"mic sensitivity set to: {engine.energy_threshold}\n\npress \"F\" to speak!\n")


def speech_to_chatbox():
    print("listening now...\n")
    with mic as voice: speech = engine.listen(voice)
    try:
        text = engine.recognize_google(speech)
        print(f"speech recognized as: {text}. sent to vrchat!\n")
        vrchat.send_message("/chatbox/input", [text, True]) # True to send and display, False to send only
    except UnknownValueError:
        print("didn't quite get that, try again...\npress \"F\" to speak!")
        text = ""
    #
#


while True:
    wait("f")
    speech_to_chatbox()
#
