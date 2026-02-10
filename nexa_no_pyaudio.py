import subprocess
import tempfile
import os
from datetime import datetime, timedelta
import random
import time
import json

class NEXA_No_PyAudio:
    def __init__(self):
        print("🔊 Initializing NEXA - No PyAudio Needed!")
        self.voice_index = 1
        self.reminders = []
        self.alarms = []
        
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
    
    def voice_command_simulation(self):
        """Simulate voice commands without PyAudio"""
        print("\n🎤 VOICE COMMAND SIMULATION")
        print("💡 This feels like voice input but doesn't need PyAudio")
        print("1. Think of your command")
        print("2. Press Enter")
        print("3. Type what you said")
        
        input("🔊 Press ENTER when ready to speak... ")
        command = input("📝 Your voice command: ").strip().lower()
        
        # Add voice processing simulation
        print("🔍 Processing voice...")
        time.sleep(1)
        print(f"✅ Recognized: '{command}'")
        
        return command
    
    def set_reminder(self, reminder_text, time_str):
        """Set a reminder"""
        reminder = {
            "text": reminder_text,
            "time": time_str,
            "created": datetime.now().isoformat()
        }
        self.reminders.append(reminder)
        return f"I'll remind you: '{reminder_text}' at {time_str}"
    
    def set_alarm(self, alarm_time):
        """Set an alarm"""
        alarm = {
            "time": alarm_time,
            "active": True
        }
        self.alarms.append(alarm)
        return f"Alarm set for {alarm_time}"
    
    def process_command(self, command):
        """Process voice commands"""
        if not command:
            return "I didn't hear anything. Please try again."
        
        if any(word in command for word in ['hello', 'hi', 'hey', 'nexa']):
            return "Hello! I'm listening to your voice commands!"
        
        elif any(word in command for word in ['time']):
            return f"The time is {datetime.now().strftime('%I:%M %p')}"
        
        elif any(word in command for word in ['date']):
            return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}"
        
        elif any(word in command for word in ['joke']):
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "What's a computer's favorite snack? Microchips!",
                "Why was the computer cold? It left its Windows open!"
            ]
            return random.choice(jokes)
        
        elif any(word in command for word in ['reminder', 'remember']):
            if 'tomorrow' in command:
                time_str = (datetime.now() + timedelta(days=1)).strftime("%I:%M %p")
                task = command.replace('reminder', '').replace('remember', '').replace('tomorrow', '').strip()
                return self.set_reminder(task, time_str)
            return "What would you like me to remind you about?"
        
        elif any(word in command for word in ['alarm']):
            if '5' in command and 'am' in command:
                return self.set_alarm("5:00 AM")
            return "What time should I set the alarm for?"
        
        elif any(word in command for word in ['stop', 'exit', 'quit']):
            return "stop"
        
        else:
            return f"I heard: '{command}'. Try: time, date, joke, reminder, or alarm."
    
    def show_commands(self):
        print("\n" + "🎯" * 25)
        print("   NEXA VOICE COMMANDS")
        print("🎯" * 25)
        print("Try these voice commands:")
        print("• 'Hello NEXA'")
        print("• 'What time is it'")
        print("• 'What's the date'")
        print("• 'Tell me a joke'")
        print("• 'Remind me to study tomorrow'")
        print("• 'Set alarm for 5 AM'")
        print("• 'Exit'")
        print("🎯" * 25)
    
    def run(self):
        print("\n🚀 NEXA Voice Assistant - No PyAudio Needed!")
        print("💡 Voice simulation mode activated")
        
        self.speak("Hello! I'm NEX-uh. Voice commands are now active!")
        
        self.show_commands()
        
        while True:
            print(f"\n" + "─" * 50)
            
            # Get voice command through simulation
            command = self.voice_command_simulation()
            
            if not command:
                continue
                
            response = self.process_command(command)
            
            if response == "stop":
                self.speak("Goodbye! Voice commands working perfectly!")
                break
            
            self.speak(response)

if __name__ == "__main__":
    print("🎯 Starting NEXA - No PyAudio Version...")
    nexa = NEXA_No_PyAudio()
    nexa.run()