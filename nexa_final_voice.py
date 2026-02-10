import subprocess
import tempfile
import os
from datetime import datetime
import random
import time

class NEXA_Final:
    def __init__(self):
        print("🔊 Initializing NEXA with Voice Index 1...")
        self.voice_index = 1  # Your confirmed working voice
        
    def speak(self, text):
        """Speak with Voice Index 1"""
        text = text.replace("NEXA", "NEX-uh")
        print(f"🤖 NEXA: {text}")
        
        # Simple and reliable VBS script
        vb_script = f'''
Dim speech
Set speech = CreateObject("SAPI.SpVoice")

' Use Voice Index 1 directly
If speech.GetVoices.Count > {self.voice_index} Then
    Set speech.Voice = speech.GetVoices.Item({self.voice_index})
End If

speech.Speak "{text.replace('"', "'")}"
'''
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.vbs', delete=False) as f:
            f.write(vb_script)
            temp_file = f.name
        
        try:
            subprocess.run(['cscript', '//B', '//Nologo', temp_file], timeout=30)
        except:
            pass  # Ignore timeouts - speech usually works
        finally:
            try:
                os.unlink(temp_file)
            except:
                pass
    
    def process_command(self, command):
        command = command.lower()
        
        if any(word in command for word in ['hello', 'hi', 'hey']):
            hour = datetime.now().hour
            if hour < 12:
                return "Good morning! I am NEX-uh with Voice Index 1."
            elif hour < 17:
                return "Good afternoon! This is NEX-uh speaking."
            else:
                return "Good evening! I'm NEX-uh, ready to help."
                
        elif 'time' in command:
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The time is {current_time}"
            
        elif 'date' in command:
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            return f"Today is {current_date}"
            
        elif 'your name' in command:
            return "I am NEX-uh, your personal AI assistant."
            
        elif 'voice' in command:
            return "I'm using Voice Index 1, which you selected as the best sounding voice!"
            
        elif 'joke' in command:
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "What's a computer's favorite snack? Microchips!",
                "Why was the computer cold? It left its Windows open!"
            ]
            return random.choice(jokes)
            
        elif 'thank you' in command:
            return "You're welcome! Happy to help."
            
        else:
            return "I'm listening. Try: time, date, joke, or ask about my voice."
    
    def run(self):
        print("\n🚀 NEXA Final with Voice Index 1")
        print("💡 Voice confirmed working - Ready for commands!")
        
        self.speak("Hello! I am NEX-uh with Voice Index 1. All systems operational!")
        
        while True:
            print("\n" + "─" * 40)
            command = input("🎯 Your command: ").strip()
            
            if command.lower() == 'exit':
                self.speak("NEX-uh signing off. Goodbye!")
                break
                
            response = self.process_command(command)
            self.speak(response)

if __name__ == "__main__":
    print("🎯 Launching NEXA Final with Voice Index 1...")
    ai = NEXA_Final()
    ai.run()