from whisper_live.client import TranscriptionClient
client = TranscriptionClient(
  "localhost",
  9090,
  lang="en",
  translate=False,
  model="small",
  use_vad=False,
    #save_output_recording=True,                         # Only used for microphone input, False by Default
    #output_recording_filename="./jfk_1963_0626_berliner.wav"  # Only used for microphone input
)

client("./jfk_1963_0626_berliner.wav")
