from playsound import playsound
import eel 
#playing Assistant sound
@eel.expose
def playAssistantSound():
    music_dir="C:\\Users\\Dell Guna\\OneDrive\\Desktop\\jarvis\\www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)