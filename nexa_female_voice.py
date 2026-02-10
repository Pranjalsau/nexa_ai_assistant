import subprocess
import tempfile
import os
from datetime import datetime
import random
import time

class NEXA_Female_Voice:
    def __init__(self):
        print("🔊 Initializing NEXA with Female Voice...")
        
    def speak(self, text):
        """Female voice TTS with NEX-uh pronunciation"""
        text = text.replace("NEXA", "NEX-uh")  # Changed to NEX-uh
        print(f"🤖 NEXA: {text}")
        
        # Female voice VBS script
        vb_script = '''
Dim speech
Set speech = CreateObject("SAPI.SpVoice")

' Try to set female voice
For Each voice in speech.GetVoices
    If InStr(voice.GetDescription, "Female") > 0 Or _
       InStr(voice.GetDescription, "Zira") > 0 Or _
       InStr(voice.GetDescription, "David") = 0 Then
        Set speech.Voice = voice
        Exit For
    End If
Next

speech.Speak "''' + text.replace('"', "'") + '''"
'''
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.vbs', delete=False) as f:
            f.write(vb_script)
            temp_file = f.name
        
        try:
            subprocess.run(['cscript', '//B', '//Nologo', temp_file], timeout=30)
            print("🔊 Female Voice: Active")
        except subprocess.TimeoutExpired:
            print("🔊 Voice: Slow but working")
        except Exception as e:
            print(f"🔊 Voice: Issue - {e}")
        finally:
            try:
                os.unlink(temp_file)
            except:
                pass
    
    def process_command(self, command):
        command = command.lower()
        
        if any(word in command for word in ['hello', 'hi', 'hey']):
            return "Hello! I am NEX-uh with my new female voice. How can I assist you?"
        elif 'time' in command:
            return f"The current time is {datetime.now().strftime('%I:%M %p')}"
        elif 'voice' in command:
            return "This is my new female voice! Do you like how I sound now?"
        elif 'your name' in command:
            return "I am NEX-uh, your personal AI assistant."
        elif 'test' in command:
            return "This is a voice test. NEX-uh is speaking with female voice."
        else:
            return "I'm NEX-uh with my new voice! Try asking for the time or my name."
    
    def run(self):
        print("\n🚀 NEXA Female Voice Test Ready!")
        print("💡 Now pronounced: NEX-uh")
        
        self.speak("Hello! This is NEX-uh with my new female voice. Ready for your commands!")
        
        while True:
            print("\n" + "─" * 40)
            command = input("🎯 Test command (or 'exit'): ").strip()
            
            if command.lower() == 'exit':
                self.speak("NEX-uh female voice test complete. Goodbye!")
                break
                
            response = self.process_command(command)
            self.speak(response)

if __name__ == "__main__":
    print("🎯 Testing NEXA with NEX-uh pronunciation...")
    ai = NEXA_Female_Voice()
    ai.run()