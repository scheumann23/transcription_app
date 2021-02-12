import streamlit as st
import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

st.title('Audio Transcription Tool')

audio_file = st.sidebar.file_uploader('Select an audio file to transcribe:', type='wav')

st.audio(audio_file)

speech, rate = librosa.load(audio_file, sr=16000)

input_values = tokenizer(speech, return_tensors = 'pt').input_values

logits = model(input_values).logits

predicted_ids = torch.argmax(logits, dim = -1)

transcription = tokenizer.decode(predicted_ids[0])

st.write('Transcription:', transcription)

