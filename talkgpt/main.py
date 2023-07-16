import openai

import pyttsx3
engine =pyttsx3.init()

import speech_recognition as sr
listener =sr.Recognizer()
openai.api_key= # add api key created by you
while True:
  model = "text-davinci-003"
  with sr.Microphone() as source:

    print("Speak now..")
    voice=listener.listen(source)
    data= listener.recognize_google(voice)
  if "exit" in data:
    break
  completion = openai.Completion.create( model= "text-davinci-003",
    prompt=  data,
    max_tokens= 1024,
    temperature= 0.5,
    n= 1,
    stop= None)

  response = completion.choices[0].text
  choice=int(input("Enter choice 1 for text or enter 2 for text with voice:"))
  if choice==1:
     print(response)
  else:
    print(response)
    engine.say(response)
    engine.runAndWait()
  repeat= input("Do you want more question?:" )
  if repeat in['NO','no','No']:
     break
