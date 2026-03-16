# ------------------------------------------------------
# Text to Speech Application using pyttsx3
# ------------------------------------------------------

import pyttsx3
import time

# Initialize engine
engine = pyttsx3.init()

# Display available voices
voices = engine.getProperty('voices')

print("Available Voices:")
for index, voice in enumerate(voices):
    print(index, voice.name)

# Function to speak text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to set voice
def set_voice(choice):
    engine.setProperty('voice', voices[choice].id)

# Function to set speech rate
def set_rate(rate):
    engine.setProperty('rate', rate)

# Function to set volume
def set_volume(volume):
    engine.setProperty('volume', volume)

# Greeting message
def greeting():
    speak_text("Welcome to the text to speech system")

# Speak current time
def speak_time():
    current_time = time.strftime("%H:%M:%S")
    message = "The current time is " + current_time
    speak_text(message)

# Save speech to file
def save_audio(text, filename):
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print("Audio saved to", filename)

# Repeat speech multiple times
def repeat_speech(text, count):
    for i in range(count):
        speak_text(text)

# Countdown speech
def countdown(number):
    for i in range(number, 0, -1):
        speak_text(str(i))
        time.sleep(1)

# Simple menu
def menu():
    print("\n--- Text to Speech Menu ---")
    print("1. Speak text")
    print("2. Change voice")
    print("3. Change speed")
    print("4. Change volume")
    print("5. Speak time")
    print("6. Repeat speech")
    print("7. Countdown")
    print("8. Save speech to file")
    print("9. Exit")

# Program start
greeting()

while True:

    menu()

    choice = input("Enter your choice: ")

    # Speak text
    if choice == "1":
        text = input("Enter text to speak: ")
        speak_text(text)

    # Change voice
    elif choice == "2":
        print("Select voice number")
        for index, voice in enumerate(voices):
            print(index, voice.name)

        voice_choice = int(input("Enter voice index: "))
        set_voice(voice_choice)
        speak_text("Voice changed successfully")

    # Change speech rate
    elif choice == "3":
        rate = int(input("Enter speech rate (100-200): "))
        set_rate(rate)
        speak_text("Speech rate updated")

    # Change volume
    elif choice == "4":
        volume = float(input("Enter volume (0.0 - 1.0): "))
        set_volume(volume)
        speak_text("Volume level updated")

    # Speak time
    elif choice == "5":
        speak_time()

    # Repeat speech
    elif choice == "6":
        text = input("Enter text: ")
        count = int(input("Repeat how many times? "))
        repeat_speech(text, count)

    # Countdown
    elif choice == "7":
        number = int(input("Enter countdown number: "))
        countdown(number)

    # Save speech to file
    elif choice == "8":
        text = input("Enter text: ")
        filename = input("Enter filename (example: speech.mp3): ")
        save_audio(text, filename)

    # Exit program
    elif choice == "9":
        speak_text("Goodbye. Program exiting.")
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
        speak_text("Invalid choice. Please try again")

# Additional example functions

def read_file():
    filename = input("Enter file name: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            speak_text(content)
    except:
        speak_text("Error reading file")

def speak_numbers():
    for i in range(1, 11):
        speak_text(str(i))

def motivational_message():
    messages = [
        "Believe in yourself",
        "Stay positive",
        "Never give up",
        "Work hard for success"
    ]

    for message in messages:
        speak_text(message)

def spelling_mode():
    word = input("Enter a word: ")

    for letter in word:
        speak_text(letter)

# Example demonstrations
print("\nAdditional Features Demonstration")

speak_numbers()
motivational_message()
spelling_mode()

print("Program completed")