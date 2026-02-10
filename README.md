# NEXA – Voice-Activated Personal AI Assistant

NEXA is a JARVIS-inspired personal AI assistant I built in Python. It uses speech recognition for voice input and text-to-speech for output. This project applies skills from my Artificial Intelligence internship at My Job Grow (February 2025, in collaboration with Techfest IIT Bombay), including AI fundamentals, data processing, and end-to-end solution development.

## Features
- Real-time voice recognition (using microphone or simulation)
- Natural text-to-speech with customizable voices (e.g., female variant)
- Handles commands like: time/date queries, jokes, greetings (time-based), reminders/alarms, system status
- Error handling and user-friendly responses
- Multiple versions showing project evolution (basic TTS → full voice integration)

## Technologies Used
- Python 3
- Libraries: speech_recognition (for voice input), subprocess, datetime, random, os, tempfile
- Windows SAPI for TTS (via VBScript)
- No external JSON files needed yet (reminders/alarms are in code; future update planned)

## How to Run
1. Install Python if not already (python.org).
2. Install the main library: Open command prompt and run `pip install speechrecognition`.
3. Download the files from this repo.
4. Run a script, e.g., `python nexa_final_perfected.py` (type commands) or `python nexa_real_voice_311.py` (for real voice).
5. Speak or type commands like "hello", "what time is it", "tell me a joke".

## Files in This Repo
- `test_real_voice.py`: Tests microphone voice recognition.
- `nexa_final_voice.py`: Basic voice output version.
- `nexa_female_voice.py`: Female voice variant.
- `nexa_final_perfected.py`: Perfected command handler.
- `nexa_jarvis.py`: JARVIS-style with reminders.
- `nexa_no_pyaudio.py`: Fallback without PyAudio.
- `nexa_voice_input.py`: Voice input simulation.
- `nexa_real_voice_311.py`: Advanced real voice mode.

No JSON files are included yet — the code mentions `nexa_data.json` for future saving of reminders.

## About Me
Built by Pranjal Shirsat, 2nd-year B.Tech ECS student at St. John College, Mumbai.  
LinkedIn: linkedin.com/in/pranjal-shirsat  
Inspired by my AI internship certificates (completion declaration, upskilling course, IIT Bombay collab).

Star ⭐ the repo if you like it! Open to feedback.
