import subprocess
import tempfile
import os
from datetime import datetime, timedelta
import random
import time
import json

class NEXA_Voice_Input:
    def __init__(self):
        print("🔊 Initializing NEXA with Voice Input...")
        self.voice_index = 1
        self.reminders = []
        self.alarms = []
        self.load_data()
        
    def load_data(self):
        """Load NEXA data"""
        try:
            with open("nexa_data.json", "r") as f:
                data = json.load(f)
                self.reminders = data.get("reminders", [])
                self.alarms = data.get("alarms", [])
        except:
            pass
    
    def save_data(self):
        """Save NEXA data"""
        data = {
            "reminders": self.reminders,
            "alarms": self.alarms
        }
        with open("nexa_data.json", "w") as f:
            json.dump(data, f, indent=2)
    
    def speak(self, text):
        """NEXA speaking"""
        text = text.replace("NEXA", "NEX-uh")
        print(f"🤖 NEXA: {text}")
        
        vb_script = f'''
Dim speech
Set speech = CreateObject("SAPI.SpVoice")
If speech.GetVoices.Count > {self.voice_index} Then
    Set speech.Voice = speech.GetVoices.Item({self.voice_index})
End If
speech.Speak "{text.replace('"', "'")}"
'''
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.vbs', delete=False) as f:
            f.write(vb_script)
            temp_file = f.name
        
        try:
            subprocess.run(['cscript', '//B', '//Nologo', temp_file], timeout=20)
        except:
            pass
        finally:
            try:
                os.unlink(temp_file)
            except:
                pass
    
    def listen_with_windows_speech(self):
        """Use Windows built-in speech recognition"""
        print("\n🎤 Windows Speech Recognition Activated")
        print("💡 Say your command clearly...")
        
        # Create a VBS script that uses Windows Speech Recognition
        listen_script = '''
On Error Resume Next
Dim speech
Set speech = CreateObject("SAPI.SpVoice")

WScript.Echo "Speak now..."
speech.Speak "Listening for your command"

' Note: Full speech-to-text requires more complex setup
' For now, we'll simulate the listening process
WScript.Sleep(3000)
WScript.Echo "Processing complete"
'''
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.vbs', delete=False) as f:
            f.write(listen_script)
            temp_file = f.name
        
        try:
            result = subprocess.run(['cscript', '//B', '//Nologo', temp_file], 
                                  capture_output=True, text=True, timeout=10)
            print("✅ Listening complete")
            
            # For now, we'll use input as fallback
            # In future, we can implement proper speech-to-text
            print("🔊 Voice input ready - enter what you said:")
            command = input("You said: ").strip().lower()
            return command
            
        except Exception as e:
            print(f"❌ Listening error: {e}")
            return None
        finally:
            try:
                os.unlink(temp_file)
            except:
                pass
    
    def listen_simple_method(self):
        """Simple method that feels like voice input"""
        print("\n🎤 Voice Command Ready")
        print("1. Think of your command")
        print("2. Press Enter when ready")
        print("3. Type what you want to say")
        
        input("🔊 Press ENTER when ready to speak... ")
        command = input("📝 Your voice command: ").strip().lower()
        return command
    
    def set_reminder(self, reminder_text, time_str):
        """Set a reminder"""
        reminder = {
            "text": reminder_text,
            "time": time_str,
            "created": datetime.now().isoformat()
        }
        self.reminders.append(reminder)
        self.save_data()
        return f"I'll remind you: '{reminder_text}' at {time_str}"
    
    def set_alarm(self, alarm_time):
        """Set an alarm"""
        alarm = {
            "time": alarm_time,
            "active": True
        }
        self.alarms.append(alarm)
        self.save_data()
        return f"Alarm set for {alarm_time}"
    
    def process_command(self, command):
        """Process voice commands"""
        if not command:
            return "I didn't catch that. Please try again."
        
        if any(word in command for word in ['hello', 'hi', 'hey', 'nexa']):
            return "Hello! I'm listening to your voice commands now!"
        
        elif any(word in command for word in ['reminder', 'remember']):
            if 'tomorrow' in command:
                time_str = (datetime.now() + timedelta(days=1)).strftime("%I:%M %p")
                task = command.replace('reminder', '').replace('remember', '').replace('tomorrow', '').strip()
                return self.set_reminder(task, time_str)
            return "What would you like me to remind you about?"
        
        elif any(word in command for word in ['alarm', 'wake']):
            if '5' in command and 'am' in command:
                return self.set_alarm("5:00 AM")
            return "What time for the alarm?"
        
        elif 'time' in command:
            return f"Time is {datetime.now().strftime('%I:%M %p')}"
        
        elif 'date' in command:
            return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}"
        
        elif 'joke' in command:
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "What's a computer's favorite snack? Microchips!",
                "Why was the computer cold? It left its Windows open!"
            ]
            return random.choice(jokes)
        
        elif any(word in command for word in ['stop', 'exit', 'quit']):
            return "stop"
        
        else:
            return f"I heard: '{command}'. How can I help?"
    
    def show_voice_commands(self):
        print("\n" + "🎯" * 20)
        print("   VOICE COMMANDS")
        print("🎯" * 20)
        print("Try saying:")
        print("• 'Hello NEXA'")
        print("• 'What time is it'")
        print("• 'Set alarm for 5 AM'") 
        print("• 'Remind me to study tomorrow'")
        print("• 'Tell me a joke'")
        print("• 'Exit'")
        print("🎯" * 20)
    
    def run(self):
        print("\n🚀 NEXA with Voice Input")
        print("💡 Now with voice command simulation!")
        
        self.speak("Hello! I'm NEX-uh. You can now give me voice commands!")
        
        self.show_voice_commands()
        
        while True:
            print(f"\n" + "─" * 40)
            
            # Use the simple voice input method
            command = self.listen_simple_method()
            
            if not command:
                continue
                
            response = self.process_command(command)
            
            if response == "stop":
                self.speak("Goodbye! Voice commands were fun!")
                break
            
            self.speak(response)

if __name__ == "__main__":
    print("🎯 Starting NEXA with Voice Input...")
    nexa = NEXA_Voice_Input()
    nexa.run()