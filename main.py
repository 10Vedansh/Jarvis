import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
# from gtts import gTTS
# import pygame
# import os

r= sr.Recognizer()
engine = pyttsx3.init()
# newsapi = ""
def speak(text):
    engine.say(text)
    engine.runAndWait()

# def speak(text):
#  tts = gTTS(text)
#  tts.save('temp.mp3') 
 
#  # Initialize the mixer module
# pygame.mixer.init()

# # Load the MP3 file
# pygame.mixer.music.load("temp.mp3")

# # Play the MP3 file
# pygame.mixer.music.play()

# # Keep the program running until the music stops playing
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)   

# os.remove("temp.mp3")   = THIS IS ALSO FREE FOR ONLY SOME TIME

# # def aiProcess(command):
# #     client = OpenAI(
# #   api_key= ""
# # )
# # completion = client.chat.completions.create(
# #   model="gpt-3.5-turbo",
# #   messages=[
# #     {"role": "system", "content": "You are a virtual assistant name Jarvis who is best in performing general tasks same as alexa but best.Give short responses please."},
# #     {"role": "user", "content": "what is coding"}
# #   ]
# # ) 

# print(completion.choices[0].message) = THIS WONT WORK AS OPEN AI API IS PAID


def processCommand(c):
        if "open google" in c.lower():
            webbrowser.open("https://www.google.com")

        elif "open facebook" in c.lower():
            webbrowser.open("https://www.facebook.com")

        elif "open youtube" in c.lower():
            webbrowser.open("https://www.youtube.com")

        elif "open instagram" in c.lower():
            webbrowser.open("https://www.instagram.com")

        elif "open discord" in c.lower():
            webbrowser.open("https://www.discord.com")

        elif "open gmail" in c.lower():
            webbrowser.open("https.//gmail.com")

        elif c.lower().startswith("play"):
             song = c.lower().split(" ")[1]
             link = musiclibrary.music[song]
             webbrowser.open(link)
        elif "news" in c.lower():
             r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=821000adf11c4d7ba2253d04cba5c5fa")

             if r.status_code == 200:
            # Extract titles from the JSON response
                data = r.json()
                articles = data["articles"]
            
            # Print titles of all articles
                for article in articles:
                 speak(article["title"])


                    

        else:
            webbrowser.open(f"https://www.google.com/search?q={command}")
            #Let OPENAI handle the request       
         

  
if __name__=="__main__":
    speak("Intializing Jarvis ....")
    while True:

    #Listen for the wake word jarvis
    #obtain audio from microphone
    
        r= sr.Recognizer()
       
       

        print("recognizing...")
        try: 
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source , timeout=2,phrase_time_limit=2)

                word = r.recognize_google(audio)
                if(word.lower()== "jarvis"):
                    speak("Sup")
                #LISTEN FOR COMMAND
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
                print("Error; {0}".format(e))   

                
