import custom_speech_recognition as sr
import pyaudio
from datetime import datetime

RECORD_TIMEOUT = 3
ENERGY_THRESHOLD = 1000
DYNAMIC_ENERGY_THRESHOLD = False

class BaseRecorder:
    def __init__(self, source, source_name):
        self.recorder = sr.Recognizer()
        self.recorder.energy_threshold = ENERGY_THRESHOLD
        self.recorder.dynamic_energy_threshold = DYNAMIC_ENERGY_THRESHOLD

        if source is None:
            raise ValueError("audio source can't be None")

        self.source = source
        self.source_name = source_name

    def adjust_for_noise(self, device_name, msg):
        print(f"[INFO] Adjusting for ambient noise from {device_name}. " + msg)
        with self.source:
            self.recorder.adjust_for_ambient_noise(self.source)
        print(f"[INFO] Completed ambient noise adjustment for {device_name}.")

    def record_into_queue(self, audio_queue):
        def record_callback(_, audio:sr.AudioData) -> None:
            data = audio.get_raw_data()
            audio_queue.put((self.source_name, data, datetime.utcnow()))

        self.recorder.listen_in_background(self.source, record_callback, phrase_time_limit=RECORD_TIMEOUT)

class DefaultMicRecorder(BaseRecorder):
    def __init__(self):
        super().__init__(source=sr.Microphone(sample_rate=16000), source_name="You")
        self.adjust_for_noise("Default Mic", "Please make some noise from the Default Mic...")

class DefaultSpeakerRecorder(BaseRecorder):
    def __init__(self):
        p = pyaudio.PyAudio()
        blackhole_info = None
        for i in range(p.get_device_count()):
           device_info = p.get_device_info_by_index(i)
           if 'blackhole' in device_info['name'].lower():
              blackhole_info = device_info

        assert blackhole_info, 'Blackhole not found!'
        p.terminate()

        source = sr.Microphone(speaker=True,
                               device_index= blackhole_info["index"],
                               sample_rate=int(blackhole_info["defaultSampleRate"]),
                               chunk_size=pyaudio.get_sample_size(pyaudio.paInt16),
                               channels=blackhole_info["maxInputChannels"])
        super().__init__(source=source, source_name="Speaker")
        self.adjust_for_noise("Default Speaker", "Please make or play some noise from the Default Speaker...")