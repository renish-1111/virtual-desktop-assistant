import speech_recognition as sr
import pyttsx3
import datetime
from controller.weather import get_weather
from controller.web import handle_web_commands
from controller.task import handle_task_commands
from controller.joke import tell_joke
from controller.app import close_current_app
from controller.music import play_on_spotify, play_local_file, stop_music
from controller.volume import set_volume, get_volume, increase_volume, decrease_volume, mute_volume, unmute_volume

# Initialize the recognizer and engine
r = sr.Recognizer()
engine = pyttsx3.init()

# User information
user_name = "Mr.Smile"  # Default name, can be personalized later
previous_volume = get_volume()

# Task list
task_list = []

# Function to convert text to speech
def SpeakText(command):
    engine.say(command)
    engine.runAndWait()

# Function to respond based on recognized commands
def respond_to_command(command):
    command = command.lower()
    global previous_volume

    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}."
        print(response)
        SpeakText(response)

    elif "weather" in command:
        city = "Rajkot"  # Default city
        response = get_weather(city)
        print(response)
        SpeakText(response)

    elif "search" in command or "open" in command:
        response = handle_web_commands(command)
        print(response)
        SpeakText(response)

    elif "joke" in command:
        response = tell_joke()
        print(response)
        SpeakText(response)
    
    elif "close" in command:
        response = close_current_app()
        print(response)
        SpeakText(response)

    elif "task" in command:
        response = handle_task_commands(command, task_list)
        print(response)
        SpeakText(response)

    elif "name" in command:
        global user_name
        user_name = command.split("name")[-1].strip()
        response = f"Hello {user_name}, how can I help you?"
        print(response)
        SpeakText(response)
        
    elif  "play" in command:
        if "spotify" in command:
            song = command.replace("play", "").replace("on spotify", "").strip()
            response = play_on_spotify(song)
        else:
            song = command.replace("play", "").strip()
            response = play_local_file("/path/to/your/music/folder", song)  # Replace with your music folder path

    elif "stop music" in command:
        response = stop_music()
    
    elif "volume" in command:
        if "increase" in command:
            response = increase_volume()
            print(response)
            SpeakText(response)
        elif "decrease" in command:
            response = decrease_volume()
            print(response)
            SpeakText(response)
        elif "mute" in command:
            response = mute_volume()
            print(response)
            SpeakText(response)
        elif "unmute" in command:
            response = unmute_volume(previous_volume)
            print(response)
            SpeakText(response)
        elif "set volume" in command:
            # Example command: "set volume 50"
            level = int(command.split(" ")[-1].strip().rstrip("%")) / 100
            response = set_volume(level)
            print(response)
            SpeakText(response)
        else:
            current_volume = get_volume()
            response = f"The current volume level is {current_volume * 100:.0f}%."
            print(response)
            SpeakText(response)
    
    elif "how are you" in command:
        response = "I'm doing great! How can I assist you today?"
        print(response)
        SpeakText(response)

    elif "thank you" in command:
        response = "You're welcome! If you have more questions, feel free to ask."
        print(response)
        SpeakText(response)

    elif "help" in command:
        response = "I can tell you the time, weather, search the web, open websites, tell jokes, manage tasks, and more. How can I assist you today?"
        print(response)
        SpeakText(response)

    elif "who are you" in command:
        response = "I am a virtual desktop assistant created by you. How can I assist you today?"
        print(response)
        SpeakText(response)

    elif "exit" in command or "stop" in command:
        response = "Goodbye!"
        print(response)
        SpeakText(response)
        return True  # Signal to exit the main loop

    else:
        response = "I didn't quite get that. Can you please repeat?"
        print(response)
        SpeakText(response)
    
    if "mute" not in command:
        previous_volume = get_volume()

    return False  # Continue listening

def main():
    listening = False

    while True:
        try:
            with sr.Microphone() as source2:
                if not listening:
                    print("Say 'wake up' to start listening...")
                    SpeakText("Say 'wake up' to start listening...")
                else:
                    print("Listening... Say 'stop listening' to stop.")

                # Adjust for ambient noise
                r.adjust_for_ambient_noise(source2, duration=0.5)

                print("Listening for audio...")
                audio2 = r.listen(source2)
                print("Audio captured, recognizing...")

                # Using Google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print(f"Recognized text: {MyText}")

                if "wake up" in MyText and not listening:
                    listening = True
                    print("Wake up command recognized.")
                    SpeakText(f"{user_name}, I am listening.")
                elif "stop listening" in MyText and listening:
                    listening = False
                    print("Stop listening command recognized.")
                    SpeakText("I have stopped listening.")
                elif listening:
                    # Process the recognized text
                    if respond_to_command(MyText):
                        break  # Exit the main loop if exit command is given

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            SpeakText("Sorry, I am having trouble connecting to the service.")
        except sr.UnknownValueError:
            print("I didn't catch that. Could you please repeat?")
            SpeakText("I didn't catch that. Could you please repeat?")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            SpeakText("An unexpected error occurred. Please try again.")

if __name__ == "__main__":
    main()
