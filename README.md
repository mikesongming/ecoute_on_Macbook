
THIS IS A **MACBOOK VERSION** adapted from the original Windows version.

# 🎧 Ecoute

Ecoute is a live transcription tool that provides real-time transcripts for both the user's microphone input (You) and the user's speakers output (Speaker) in a textbox. It also generates a suggested response using OpenAI's GPT-3.5 for the user to say based on the live transcription of the conversation.

## 📖 Demo

<https://github.com/SevaSk/ecoute/assets/50382291/8ac48927-8a26-49fd-80e9-48f980986208>

Ecoute is designed to help users in their conversations by providing live transcriptions and generating contextually relevant responses. By leveraging the power of OpenAI's GPT-3.5, Ecoute aims to make communication more efficient and enjoyable.

## 🚀 Getting Started

Follow these steps to set up and run Ecoute on your local machine.

### 📋 Prerequisites

- Install the virtual audio driver [**Blackhole**](https://github.com/ExistentialAudio/BlackHole) and configure [**Multi-Output Device**](https://github.com/ExistentialAudio/BlackHole/wiki/Multi-Output-Device) as directed. [Howfinity](https://www.youtube.com/@Howfinity)'s clip <https://youtu.be/LSmM5FXzVBg> is recommended for details.
- 3.8.0 <=  Python < 3.10.0
- An OpenAI API key
- MacOSX
- FFmpeg

If FFmpeg is not installed in your system, you can install it using Homebrew.

### 🔧 Installation

1. Clone the repository:

   ```
   git clone https://github.com/SevaSk/ecoute
   ```

2. Navigate to the `ecoute` folder:

   ```
   cd ecoute
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Create a `keys.py` file in the ecoute directory and add your OpenAI API key:

   - Option 1: You can utilize a command on your command prompt. Run the following command, ensuring to replace "API KEY" with your actual OpenAI API key:

      ```
      python -c "with open('keys.py', 'w', encoding='utf-8') as f: f.write('OPENAI_API_KEY=\"API KEY\"')"
      ```

   - Option 2: You can create the keys.py file manually. Open up your text editor of choice and enter the following content:

      ```
      OPENAI_API_KEY="API KEY"
      ```

      Replace "API KEY" with your actual OpenAI API key. Save this file as keys.py within the ecoute directory.

### 🎬 Running Ecoute

Run the main script:

```
python main.py
```

For a more better and faster version that also works with most languages, use:

```
python main.py --api
```

Upon initiation, Ecoute will begin transcribing your microphone input and speaker output in real-time, generating a suggested response based on the conversation. Please note that it might take a few seconds for the system to warm up before the transcription becomes real-time.

The --api flag will use the whisper api for transcriptions. This significantly enhances transcription speed and accuracy, and it works in most languages (rather than just English without the flag). It's expected to become the default option in future releases. However, keep in mind that using the Whisper API will consume more OpenAI credits than using the local model. This increased cost is attributed to the advanced features and capabilities that the Whisper API provides. Despite the additional expense, the substantial improvements in speed and transcription accuracy may make it a worthwhile investment for your use case.

### ⚠️ Limitations

While Ecoute provides real-time transcription and response suggestions, there are several known limitations to its functionality that you should be aware of:

**Default Mic and Speaker:** Ecoute is currently configured to listen only to the default microphone and speaker set in your system. It will not detect sound from other devices or systems. If you wish to use a different mic or speaker, you will need to set it as your default device in your system settings.

**Whisper Model**: If the --api flag is not used, we utilize the 'tiny' version of the Whisper ASR model, due to its low resource consumption and fast response times. However, this model may not be as accurate as the larger models in transcribing certain types of speech, including accents or uncommon words.

**Language**: If you are not using the --api flag the Whisper model used in Ecoute is set to English. As a result, it may not accurately transcribe non-English languages or dialects. We are actively working to add multi-language support to future versions of the program.

## 📖 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve Ecoute.
