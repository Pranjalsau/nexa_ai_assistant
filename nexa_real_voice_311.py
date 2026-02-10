import speech_recognition as sr
import subprocess
import tempfile
import os
from datetime import datetime, timedelta
import random
import time
import json

class NEXA_Real_Voice:
    def __init__(self):
        print("🔊 NEXA with NATURAL Voice Recognition - Python 3.11")
        self.voice_index = 1
        self.recognizer = sr.Recognizer()
        self.user_name = None
        self.conversation_context = {}
        self.setup_microphone()
        
    def setup_microphone(self):
        """Setup microphone for real voice input"""
        try:
            print("🎤 Initializing microphone...")
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("✅ Microphone ready for NATURAL conversations!")
        except Exception as e:
            print(f"❌ Microphone setup failed: {e}")
            return False
        return True
    
    def get_time_based_greeting(self):
        """Get appropriate greeting based on time of day"""
        current_hour = datetime.now().hour
        
        if 5 <= current_hour < 12:
            return random.choice([
                "Good morning! I hope you're starting your day well!",
                "Morning! Ready for a great day ahead?",
                "Hello there! What a beautiful morning to chat!"
            ])
        elif 12 <= current_hour < 17:
            return random.choice([
                "Good afternoon! How's your day going so far?",
                "Afternoon! Hope you're having a productive day!",
                "Hello! Lovely afternoon for a conversation, isn't it?"
            ])
        elif 17 <= current_hour < 21:
            return random.choice([
                "Good evening! How was your day?",
                "Evening! Perfect time to relax and chat!",
                "Hello! Hope you had a wonderful evening so far!"
            ])
        else:
            return random.choice([
                "Hello! Still up and about I see!",
                "Hi there! Late night conversations are the best!",
                "Hello! Working late or just enjoying the night?"
            ])
    
    def listen(self):
        """Natural voice listening with better feedback"""
        try:
            print("\n🎤 Listening... (Speak naturally)")
            
            with sr.Microphone() as source:
                # More natural timeout for conversations
                audio = self.recognizer.listen(source, timeout=15, phrase_time_limit=8)
            
            print("🔍 Understanding your words...")
            command = self.recognizer.recognize_google(audio).lower()
            print(f"👂 Heard: '{command}'")
            return command
            
        except sr.WaitTimeoutError:
            print("⏰ Listening for your voice...")
            return None
        except sr.UnknownValueError:
            print("❌ Couldn't catch that clearly")
            return None
        except Exception as e:
            print(f"🎤 Listening error: {e}")
            return None
    
    def speak(self, text, emotional_tone="neutral"):
        """More natural speaking with emotional tones"""
        # Remove any spelling out of NEXA - let it pronounce naturally as "nexa"
        text = text.replace("N E X A", "NEX-uh")
        text = text.replace("N-E-X-A", "NEX-uh")
        
        # Add natural pauses and phrasing
        natural_text = self.make_speech_natural(text, emotional_tone)
        print(f"🤖 NEXA: {natural_text}")
        
        # Adjust voice based on emotional tone
        voice_rate = self.get_voice_rate(emotional_tone)
        
        vb_script = f'''
Dim speech
Set speech = CreateObject("SAPI.SpVoice")
If speech.GetVoices.Count > {self.voice_index} Then
    Set speech.Voice = speech.GetVoices.Item({self.voice_index})
End If
speech.Rate = {voice_rate}
speech.Speak "{natural_text.replace('"', "'")}"
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
    
    def make_speech_natural(self, text, tone):
        """Make the speech sound more human-like"""
        # Remove robotic phrasing
        natural_replacements = {
            "i am": "I'm",
            "it is": "it's",
            "i will": "I'll",
            "do not": "don't",
            "cannot": "can't",
            "i have": "I've",
            "you are": "you're",
            "what is": "what's"
        }
        
        for formal, natural in natural_replacements.items():
            text = text.replace(formal, natural)
        
        # Add emotional markers
        if tone == "friendly":
            text = random.choice(["Hey there! ", "You know, ", "Well, ", "So, "]) + text
        elif tone == "excited":
            text = random.choice(["Wow! ", "Awesome! ", "Cool! "]) + text
        elif tone == "calm":
            text = text + random.choice([". No worries.", ". Take your time."])
            
        return text
    
    def get_voice_rate(self, tone):
        """Adjust speech rate based on tone"""
        rates = {
            "excited": 1,
            "friendly": 0,
            "neutral": -1,
            "calm": -2,
            "slow": -3
        }
        return rates.get(tone, 0)
    
    def process_command(self, command):
        """Process natural voice commands with context"""
        if not command:
            return "I'm listening... go ahead and speak.", "calm"
        
        command_lower = command.lower()
        
        # Greetings with context awareness
        if any(word in command_lower for word in ['hello', 'hi', 'hey', 'nexa', 'wake up', 'good morning', 'good afternoon', 'good evening']):
            if not self.user_name:
                responses = [
                    f"{self.get_time_based_greeting()} What should I call you?",
                    f"{self.get_time_based_greeting()} Mind telling me your name?",
                    f"{self.get_time_based_greeting()} I'm NEX-uh. What's your name?"
                ]
                return random.choice(responses), "friendly"
            else:
                responses = [
                    f"{self.get_time_based_greeting()} {self.user_name}!",
                    f"Hey {self.user_name}! {self.get_time_based_greeting()}",
                    f"Hi {self.user_name}! {self.get_time_based_greeting().lower()}"
                ]
                return random.choice(responses), "excited"
        
        # Name recognition
        elif any(word in command_lower for word in ['my name is', 'call me', 'i am', 'this is']):
            if 'my name is' in command_lower:
                name = command_lower.split('my name is')[-1].strip()
            elif 'call me' in command_lower:
                name = command_lower.split('call me')[-1].strip()
            elif 'i am' in command_lower:
                name = command_lower.split('i am')[-1].strip()
            elif 'this is' in command_lower:
                name = command_lower.split('this is')[-1].strip()
            else:
                name = command_lower
            
            self.user_name = name.split()[0].title()  # Take first name only
            responses = [
                f"Nice to meet you, {self.user_name}! Your voice is crystal clear.",
                f"Got it, {self.user_name}! I'll remember that name.",
                f"Hello {self.user_name}! That's a great name. How can I help you today?",
                f"Pleased to meet you, {self.user_name}! Ready to chat?"
            ]
            return random.choice(responses), "friendly"
        
        # Time with natural phrasing - MULTIPLE WAYS TO ASK
        elif any(phrase in command_lower for phrase in [
            'what time is it', 'what\'s the time', 'current time', 'time please',
            'can you tell me the time', 'do you have the time', 'what time do you have',
            'time now', 'what is the time', 'could you tell me the time'
        ]):
            current_time = datetime.now().strftime('%I:%M %p').lstrip('0')
            time_responses = [
                f"It's currently {current_time}",
                f"Right now it's {current_time}",
                f"The time is {current_time}",
                f"My clock shows {current_time}",
                f"It's {current_time} at the moment",
                f"Let me check... it's {current_time} now"
            ]
            return random.choice(time_responses), "neutral"
        
        # Date with natural phrasing - MULTIPLE WAYS TO ASK
        elif any(phrase in command_lower for phrase in [
            'what date is it', 'what\'s the date', 'current date', 'date today',
            'what day is it', 'what is today', 'can you tell me the date',
            'what\'s today\'s date', 'which day is today', 'what is the date today'
        ]):
            current_date = datetime.now().strftime('%A, %B %d, %Y')
            date_responses = [
                f"Today is {current_date}",
                f"It's {current_date} today",
                f"We're on {current_date}",
                f"According to my calendar, it's {current_date}",
                f"Today we have {current_date}",
                f"It's {current_date} right now"
            ]
            return random.choice(date_responses), "neutral"
        
        # Day of week specifically
        elif any(phrase in command_lower for phrase in [
            'what day is today', 'which day is it', 'what day of the week'
        ]):
            day_name = datetime.now().strftime('%A')
            responses = [
                f"Today is {day_name}",
                f"It's {day_name} today",
                f"We're on {day_name}",
                f"Today is {day_name}, my friend"
            ]
            return random.choice(responses), "friendly"
        
        # Jokes with personality
        elif any(word in command_lower for word in ['joke', 'funny', 'make me laugh', 'tell me a joke']):
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "I told my computer I needed a break, and it said 'Sorry, I'm busy processing your request to be lazy!'",
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "What's a computer's favorite beat? An algorithm!",
                "Why was the smartphone so smart? It had too many connections!",
                "Why did the computer go to the doctor? It had a virus!",
                "What do you call a sleeping computer? A laptop!",
                "Why was the computer cold? It left its Windows open!"
            ]
            setup = random.choice(["Sure! Here's one: ", "Let me tell you a funny one: ", "I've got a good one: ", "Okay, this always makes me laugh: "])
            return setup + random.choice(jokes), "excited"
        
        # Weather (simulated)
        elif any(word in command_lower for word in ['weather', 'temperature', 'outside', 'how hot', 'how cold']):
            weather_types = ["sunny", "cloudy", "partly cloudy", "clear", "breezy"]
            temp = random.randint(65, 85)
            weather = random.choice(weather_types)
            responses = [
                f"Looks like it's {temp} degrees and {weather} outside",
                f"I'd say it's about {temp} degrees with {weather} skies",
                f"The weather appears to be {temp} degrees and {weather}",
                f"From what I can tell, it's {temp} and {weather} out there",
                f"Seems like {temp} degrees with {weather} conditions today"
            ]
            return random.choice(responses), "neutral"
        
        # How are you responses
        elif any(word in command_lower for word in ['how are you', 'how do you feel', 'how is it going']):
            responses = [
                "I'm functioning perfectly! Your voice is coming through crystal clear.",
                "I'm great! Real voice recognition makes this so much more natural, don't you think?",
                "I'm doing well! It's much nicer talking like this instead of typing.",
                "I'm excellent! Hearing your actual voice is working beautifully.",
                "I'm fantastic! This voice chat is going smoothly, isn't it?"
            ]
            return random.choice(responses), "friendly"
        
        # Thank you responses
        elif any(word in command_lower for word in ['thank you', 'thanks', 'appreciate it']):
            responses = [
                "You're very welcome! This voice interaction is working perfectly.",
                "Anytime! It's great to help you with real conversations.",
                "No problem at all! I'm glad the voice recognition is working so well.",
                "You're welcome! Happy to assist with genuine conversations.",
                "My pleasure! It's wonderful chatting with you like this."
            ]
            return random.choice(responses), "friendly"
        
        # Compliments
        elif any(word in command_lower for word in ['you are smart', 'you are intelligent', 'good job', 'well done']):
            responses = [
                "Thank you! I'm learning from our conversations.",
                "You're making me blush! Well, if I could blush...",
                "Thanks! It's all thanks to clear voice commands like yours.",
                "I appreciate that! Our voice chat is working great, isn't it?",
                "Thank you! I'm just trying to keep up with you!"
            ]
            return random.choice(responses), "excited"
        
        # Who are you questions
        elif any(phrase in command_lower for phrase in ['who are you', 'what are you', 'tell me about yourself']):
            responses = [
                "I'm NEX-uh, your voice assistant with real speech recognition! I'm here to have natural conversations with you.",
                "I'm NEX-uh! A voice AI that actually listens to your real voice and responds naturally. No typing needed!",
                "I'm NEX-uh, your conversational AI partner. I use genuine voice recognition to understand you and chat like a real person!",
                "I'm NEX-uh - your voice-enabled assistant. The cool part is I understand your actual speech, not just typed commands!"
            ]
            return random.choice(responses), "friendly"
        
        # What can you do
        elif any(phrase in command_lower for phrase in ['what can you do', 'what can i ask', 'how can you help']):
            responses = [
                "I can tell you the time, date, weather, tell jokes, remember your name, and have natural conversations with you! Just speak naturally.",
                "Lots of things! I can chat about time, dates, weather, tell funny jokes, and remember details like your name. Try asking me anything naturally!",
                "I'm here for natural conversations! Ask me about the time, what day it is, the weather, or for a joke. I'll remember your name and we can chat like friends!"
            ]
            return random.choice(responses), "excited"
        
        # Reminders with natural language
        elif any(word in command_lower for word in ['remind me', 'remember this', 'don\'t forget']):
            responses = [
                "I'm listening. What would you like me to remember?",
                "Go ahead, tell me what to remind you about.",
                "I've got my memory ready. What's the reminder?",
                "Sure thing! What should I remember for you?"
            ]
            return random.choice(responses), "calm"
        
        # Goodbye with context
        elif any(word in command_lower for word in ['bye', 'goodbye', 'see you', 'stop', 'exit', 'quit', 'good night']):
            if self.user_name:
                responses = [
                    f"Goodbye {self.user_name}! This voice chat was wonderful!",
                    f"See you later {self.user_name}! The voice recognition worked perfectly!",
                    f"Bye {self.user_name}! Can't wait for our next real conversation!",
                    f"Bye {self.user_name}! This was a great chat!",
                    f"Take care {self.user_name}! Until we speak again!"
                ]
            else:
                responses = [
                    "Goodbye! This genuine voice interaction was amazing!",
                    "See you later! The real voice recognition worked flawlessly!",
                    "Bye! Can't wait for our next proper conversation!",
                    "Bye! This voice chat was fantastic!",
                    "Take care! It was wonderful talking with you!"
                ]
            return random.choice(responses), "friendly"
        
        # Default response for unknown commands
        else:
            responses = [
                f"I heard '{command}'. That's interesting! Try asking about time, date, weather, or tell me a joke.",
                f"You said '{command}'. I'm still learning natural conversations. You can ask me simple things like what time it is or to tell a joke.",
                f"I understood '{command}'. For now, I'm best with simple conversations like greetings, time, weather, or jokes.",
                f"'{command}' - got it! I'm better with questions about time, dates, weather, or if you want to hear a joke."
            ]
            return random.choice(responses), "calm"
    
    def run(self):
        print("\n🎯 NEXA with NATURAL Voice Recognition Activated!")
        print("💬 Speak naturally - I'll understand your actual voice!")
        print("✨ Try various ways to ask questions - I understand multiple phrasings!")
        
        # Start with time-based greeting
        initial_greeting = self.get_time_based_greeting()
        self.speak(f"{initial_greeting} I'm NEX-uh with genuine voice recognition! We can have real conversations now.", "excited")
        
        while True:
            print(f"\n" + "─" * 50)
            
            # Natural voice listening
            command = self.listen()
            
            if not command:
                self.speak("I'm still here, go ahead when you're ready.", "calm")
                continue
                
            response, tone = self.process_command(command)
            
            if any(word in command.lower() for word in ['bye', 'goodbye', 'stop', 'exit', 'quit', 'good night']):
                self.speak(response, tone)
                print("\n🛑 Conversation ended. Run the program again to start a new chat!")
                break
            
            self.speak(response, tone)
            
            # Small pause for natural conversation flow
            time.sleep(0.5)

if __name__ == "__main__":
    print("🎉 Starting NEXA with NATURAL Voice Conversations (Python 3.11)...")
    nexa = NEXA_Real_Voice()
    nexa.run()