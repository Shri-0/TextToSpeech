from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

# download and load all models
preload_models()

# generate audio from text

text_prompt = """
     추석은 내가 가장 좋아하는 명절이다. 나는 며칠 동안 휴식을 취하고 친구 및 가족과 시간을 보낼 수 있습니다.
"""

text_prompt_two = """
     I have a silky smooth voice, and today [clears throat] I will tell you about
    the exercise regimen of the common sloth.
"""
# audio_array = generate_audio(text_prompt, history_prompt="en_speaker_3")

audio_array = generate_audio(text_prompt)


# save audio to disk
write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)

# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)
