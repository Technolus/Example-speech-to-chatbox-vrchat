# made for a vrchat player usernamed Cachie~
from speech_recognition import Microphone, Recognizer, UnknownValueError
from pythonosc.udp_client import SimpleUDPClient
from time import sleep


vrchat = SimpleUDPClient("127.0.0.1", 9000)
engine = Recognizer()
mic = Microphone()


while True:
    try:
        print(f"{__file__} is now running\n\nbe silent for a moment to improve your experience")
        sleep(1)
        with mic as back_ground_noise: engine.adjust_for_ambient_noise(back_ground_noise, duration=1)
        print(f"minimum energy threshold set to: {engine.energy_threshold}\n\nyou're good to speak!")
        with mic as voice: speech = engine.listen(voice)
        try:
            text = engine.recognize_google(speech)
            print(f"speech recognized as: {text}. sending it to vrchat...")
            vrchat.send_message("/chatbox/input", [text, True]) # True to send and display, False to send only
        #
        except UnknownValueError: print("didn't quite get that, say it again please...")
    #
    except KeyboardInterrupt: pass
#
