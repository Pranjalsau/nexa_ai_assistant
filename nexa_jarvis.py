import subprocess
import tempfile
import os
from datetime import datetime, timedelta
import random
import time
import json
import threading

class NEXA_Proper:
    def __init__(self):
        print("🔊 Initializing NEXA Systems...")
        self.voice_index = 1
        self.user_name = ""  # Will ask for your name
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
            print("✅ Data loaded")
        except:
            print("📁 Starting fresh session")
    
    def save_data(self):
        """Save NEXA data"""
        data = {
            "reminders": self.reminders,
            "alarms": self.alarms
        }
        with open("nexa_data.json", "w") as f:
            json.dump(data, f, indent=2)
    
    def speak(self, text):
        """NEXA speaking - clean and professional"""
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
    
    def get_user_name(self):
        """Get your name for personalization"""
        print("\n💬 Before we begin...")
        name = input("What should I call you? ").strip()
        return name if name else "there"
    
    def get_voice_command(self):
        """Simple voice command input"""
        print(f"\n🎤 Ready for command...")
        
        input("🔊 Press ENTER and speak... ")
        command = input("📝 You said: ").strip().lower()
        return command
    
    # NEXA FEATURES
    def system_status(self):
        """Simple system status"""
        return "Systems are ready and waiting for your command."
    
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
        """Process commands for NEXA"""
        if not command:
            return "I didn't hear that. Could you try again?"
        
        # NEXA RESPONSES
        if any(word in command for word in ['system', 'status', 'diagnostic']):
            return self.system_status()
        
        elif any(word in command for word in ['reminder', 'remember']):
            if 'tomorrow' in command:
                time_str = (datetime.now() + timedelta(days=1)).strftime("%I:%M %p")
                task = command.replace('reminder', '').replace('remember', '').replace('tomorrow', '').strip()
                return self.set_reminder(task, time_str)
            return "What would you like me to remind you about?"
        
        elif any(word in command for word in ['alarm', 'wake']):
            if '5' in command and 'am' in command:
                return self.set_alarm("5:00 AM")
            return "What time should I set the alarm for?"
        
        elif 'time' in command:
            return f"The time is {datetime.now().strftime('%I:%M %p')}"
        
        elif 'date' in command:
            return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}"
        
        elif any(word in command for word in ['thank you', 'thanks']):
            return "You're welcome!"
        
        elif any(word in command for word in ['how are you']):
            return "I'm functioning well, thank you for asking!"
        
        elif any(word in command for word in ['stop', 'exit', 'shutdown']):
            return "stop"
        
        else:
            return f"I understand you said '{command}'. How can I help with that?"
    
    def show_nexa_capabilities(self):
        print("\n" + "🌟" * 25)
        print("       NEXA CAPABILITIES")
        print("🌟" * 25)
        print("🎯 Available Commands:")
        print("   • System status")
        print("   • Set reminders") 
        print("   • Set alarms")
        print("   • Check time/date")
        print("   • General assistance")
        print("🌟" * 25)
    
    def run(self):
        print("\n🚀 NEXA Assistant Starting...")
        
        # Get user's name
        self.user_name = self.get_user_name()
        
        # Clean startup
        self.speak(f"Hello! I'm NEX-uh, ready to assist you.")
        
        self.show_nexa_capabilities()
        
        while True:
            print(f"\n" + "─" * 40)
            command = self.get_voice_command()
            
            if not command:
                continue
                
            response = self.process_command(command)
            
            if response == "stop":
                self.speak("NEX-uh signing off. Take care!")
                print("🛑 NEXA Offline")
                break
            
            self.speak(response)

if __name__ == "__main__":
    print("🎯 Starting NEXA Assistant...")
    nexa = NEXA_Proper()
    nexa.run()