import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'

# Define the function to interact with GPT-3
def ask_gpt(prompt, max_tokens=50):
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose a different engine if you want
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

# Example prompt
if 0:
    prompt = "Q: What is the meaning of life?\nA:"

    # Get GPT-3's response

    response = ask_gpt(prompt)

    print("GPT-3 Response:", response)
###########################
    
if 0:
    import speech_recognition as sr

    # Function to transcribe speech to text
    def transcribe_audio():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                print("Could not understand audio.")
                return ""
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                return ""

    # Main loop to continuously listen and respond
    while True:
        # Get audio input from microphone and transcribe to text
        speech_text = transcribe_audio()
        
        if speech_text:
            print("You said:", speech_text)
###############
if 0:
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    # Function to visualize audio levels
    def visualize_audio():
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        
        fig, ax = plt.subplots()
        x = np.arange(0, 2 * CHUNK, 2)
        line, = ax.plot(x, np.random.rand(CHUNK))

        ax.set_ylim(0, 5)
        ax.set_xlim(0, 2 * CHUNK)
        ax.set_title('Live Audio Waveform')
        ax.set_xlabel('Samples')
        ax.set_ylabel('Volume')

        p = pyaudio.PyAudio()
        stream = p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            output=True,
            frames_per_buffer=CHUNK
        )

        def update_plot(frame):
            data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
            line.set_ydata(data*2)
            return line,

        ani = FuncAnimation(fig, update_plot, blit=True)
        plt.show()

    # Show audio visualization without waiting for input
    visualize_audio()


###############
if 0:
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    import sounddevice as sd

    # Function to visualize audio levels with amplification
    def visualize_audio(amplification_factor):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        
        fig, ax = plt.subplots()
        x = np.arange(0, 2 * CHUNK, 2)
        line, = ax.plot(x, np.random.rand(CHUNK))

        ax.set_ylim(-50 * amplification_factor, 50 * amplification_factor)
        ax.set_xlim(0, 2 * CHUNK)
        ax.set_title('Live Audio Waveform')
        ax.set_xlabel('Samples')
        ax.set_ylabel('Volume')

        p = pyaudio.PyAudio()
        stream = p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            output=True,
            frames_per_buffer=CHUNK
        )

        def update_plot(frame):
            data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
            amplified_data = data * amplification_factor
            line.set_ydata(amplified_data)
            return line,

        ani = FuncAnimation(fig, update_plot, blit=True)
        plt.show()

    # Set amplification factor
    amplification_factor = 2.0  # Adjust this value to change the amplification

    # Set input volume (0.0 to 1.0)
    input_volume = 0.8  # Adjust this value to change the input volume

    # Adjust the input volume using sounddevice
    sd.default.device = "Microphone"
    sd.default.channels = 1
    sd.default.samplerate = 44100
    sd.default.blocksize = 1024
    sd.default.dtype = 'int16'
    sd.default.latency = 'low'
    sd.default.extra_settings = None

    # Start visualization
    visualize_audio(amplification_factor)
if 0: # plot frequency vs amplitude
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    # Function to visualize audio spectrum with FFT
    def visualize_audio_spectrum():
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        
        fig, ax = plt.subplots()
        x = np.fft.rfftfreq(CHUNK, 1/RATE)  # Use rfftfreq for real-valued input
        line, = ax.plot(x, np.random.rand(len(x)))

        ax.set_ylim(0, 100)  # Adjust the y-axis limit based on the expected amplitude range
        ax.set_xlim(0, RATE / 2)
        ax.set_title('Audio Spectrum')
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Amplitude')

        p = pyaudio.PyAudio()
        stream = p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            output=True,
            frames_per_buffer=CHUNK
        )

        def update_plot(frame):
            data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
            fft_data = np.fft.rfft(data)  # Use rfft for real-valued input
            magnitude_spectrum = np.abs(fft_data)
            line.set_ydata(magnitude_spectrum)
            return line,

        ani = FuncAnimation(fig, update_plot, blit=True)
        plt.show()

    # Start visualization
    visualize_audio_spectrum()

if 0:#amplitude over time
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    # Function to visualize audio amplitude over time
    def visualize_audio_amplitude():
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        
        fig, ax = plt.subplots()
        x = np.arange(0, CHUNK)
        line, = ax.plot(x, np.random.rand(CHUNK))

        ax.set_ylim(-5, 5)  # Adjust the y-axis limit based on the expected amplitude range
        ax.set_xlim(0, CHUNK)
        ax.set_title('Audio Amplitude over Time')
        ax.set_xlabel('Time (samples)')
        ax.set_ylabel('Amplitude')

        p = pyaudio.PyAudio()
        stream = p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            output=True,
            frames_per_buffer=CHUNK
        )

        def update_plot(frame):
            data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
            line.set_ydata(data)
            return line,

        ani = FuncAnimation(fig, update_plot, blit=True)
        plt.show()

    # Start visualization
    visualize_audio_amplitude()
