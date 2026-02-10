import speech_recognition as sr

def test_real_voice():
    recognizer = sr.Recognizer()
    
    print("🎤 Testing REAL Voice Recognition with Python 3.11...")
    print("This should work now!")
    
    try:
        with sr.Microphone() as source:
            print("🔊 Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("✅ Ready!")
            
            print("🎤 Listening... SPEAK NOW!")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)
            
        print("🔍 Processing your voice...")
        text = recognizer.recognize_google(audio)
        print(f"🎉 SUCCESS! I heard: '{text}'")
        return text
        
    except sr.WaitTimeoutError:
        print("⏰ No speech detected")
        return None
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    result = test_real_voice()
    if result:
        print(f"\n🚀 REAL VOICE RECOGNITION IS WORKING!")
        print("🎯 Now NEXA will listen to your actual voice!")
    else:
        print("\n🔧 Let's troubleshoot PyAudio installation...")