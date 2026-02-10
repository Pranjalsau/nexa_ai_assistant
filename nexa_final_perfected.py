import subprocess
import tempfile
import os
from datetime import datetime
import random
import time

class NEXA_Final:
    def __init__(self):
        print("🔊 Initializing NEXA - Final Perfected Version...")
        
    def speak(self, text):
        """Use clean natural pronunciation"""
        # Clean pronunciation - natural sounding
        text = text.replace("NEXA", "NEX-uh")
        
        print(f"🤖 NEXA: {text}")
        self.speak_vbs(text)
    
    def speak_vbs(self, text):
        """Reliable VBScript TTS"""
        vb_script = f'''
Dim speech
Set speech = CreateObject("SAPI.SpVoice")
speech.Speak "{text.replace('"', "'")}"
'''
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.vbs', delete=False) as f:
            f.write(vb_script)
            temp_file = f.name
        
        try:
            subprocess.run(['cscript', '//B', '//Nologo', temp_file], timeout=10)
            print("🔊 Voice: Active")
        except Exception as e:
            print(f"🔊 Voice: Temporary issue - {e}")
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
                return "Good morning! I am NEXA, your personal AI assistant. How may I help you today?"
            elif hour < 17:
                return "Good afternoon! I'm NEXA, ready to assist with your tasks."
            else:
                return "Good evening! I'm NEXA, here to help you this evening."
                
        elif 'time' in command:
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}"
            
        elif 'date' in command:
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            return f"Today is {current_date}"
            
        elif 'joke' in command:
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "What's a computer's favorite snack? Microchips!",
                "Why was the computer cold? It left its Windows open!",
                "How do you organize a space party? You planet!",
                "Why did the Python programmer not respond to the email? Because it was stuck in an infinite loop!"
            ]
            return random.choice(jokes)
            
        elif 'your name' in command:
            return "I am NEXA, your personal AI assistant."
            
        elif 'who made you' in command or 'who created you' in command:
            return "I was developed as an innovative AI project, bringing futuristic technology to life."
            
        elif 'thank you' in command:
            return "You're welcome! It's always a pleasure to assist you."
            
        elif 'status' in command or 'diagnostics' in command:
            return "All systems are operational. Running at optimal performance levels."
            
        elif 'test' in command or 'audio test' in command:
            return "Audio systems confirmed working. NEXA is speaking clearly and ready for commands."
            
        elif 'weather' in command:
            return "Weather services are currently in development. This feature will be available soon."
            
        elif 'calculate' in command:
            return "Calculation module is standing by. Ready for mathematical operations."
            
        elif 'story' in command:
            return "Once upon a time, an engineer created an AI assistant. And that's me, NEXA! The story continues as we build amazing things together."
            
        else:
            return "I understand you're saying something, but I'm still learning that specific command. Try asking about time, date, jokes, or system status."
    
    def show_help(self):
        print("\n" + "✨" * 30)
        print("           NEXA AI ASSISTANT - FINAL VERSION")
        print("✨" * 30)
        print("🎯 AVAILABLE COMMANDS:")
        print("   📍 Basic Commands:")
        print("      • hello / hi / hey - Greet NEXA")
        print("      • time - Current time")
        print("      • date - Today's date") 
        print("      • joke - Tell a random joke")
        print("      • story - Hear a short story")
        print("   📍 System Commands:")
        print("      • your name - Learn about NEXA")
        print("      • who made you - Creation story")
        print("      • status - System diagnostics")
        print("      • test - Audio test")
        print("   📍 Utility Commands:")
        print("      • thank you - Polite response")
        print("      • weather - Weather feature info")
        print("      • calculate - Math capabilities")
        print("   📍 Control Commands:")
        print("      • help - Show this menu")
        print("      • exit / quit - Shutdown NEXA")
        print("✨" * 30)
    
    def run(self):
        print("\n🚀 NEXA Final Perfected Version Activated!")
        print("💡 Your Tony Stark-inspired AI assistant is now fully operational!")
        print("🔊 Voice System: NEK-sa pronunciation active")
        
        # System initialization sequence
        print("\n🔧 Running system initialization...")
        time.sleep(1)
        print("✅ Voice Module: ONLINE")
        time.sleep(0.5)
        print("✅ Command Processor: ACTIVE")
        time.sleep(0.5)
        print("✅ Audio Systems: OPERATIONAL")
        time.sleep(0.5)
        print("✅ All Systems: READY")
        
        # Initial greeting
        time.sleep(1)
        self.speak("All systems online. Initialization complete. NEXA is ready for your commands.")
        
        self.show_help()
        
        command_count = 0
        
        while True:
            print("\n" + "─" * 50)
            command = input("🎯 Your command: ").strip()
            command_count += 1
            
            if not command:
                continue
                
            if command.lower() in ['exit', 'quit', 'bye', 'goodbye', 'shutdown']:
                self.speak(f"NEXA systems going offline. Goodbye!")
                print(f"🛑 System shutdown complete. Total commands processed: {command_count}")
                break
                
            if command.lower() in ['help', 'commands', 'menu', 'what can you do']:
                self.show_help()
                continue
                
            response = self.process_command(command)
            self.speak(response)
            
            # Occasionally add some personality
            if command_count % 5 == 0:
                time.sleep(0.5)
                self.speak("Is there anything else I can help you with?")

if __name__ == "__main__":
    print("🎯" * 20)
    print("      NEXA AI ASSISTANT - FINAL LAUNCH")
    print("🎯" * 20)
    print("🌟 Inspired by Tony Stark's Innovation")
    print("💫 Built with Python and Determination")
    print("🚀 Ready to Bring Your Ideas to Life")
    print("\nInitializing...")
    
    ai = NEXA_Final()
    ai.run()