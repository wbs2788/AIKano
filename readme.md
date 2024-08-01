# AIKano

Step into the enchanting world of AIKano, where technology and anime-inspired tales blend seamlessly! AIKano isn't just any chatbot—it's a portal to engaging conversations with characters inspired by your favorite anime, thanks to the power of the Transformers library and the cutting-edge LLaMA 3.1 model. Enhanced with advanced quantization techniques, AIKano promises smooth and lively interactions, making each dialogue session uniquely immersive.

## 📋 Upcoming Features（TODOs）

- **Multi Language Support**: Although the LLaMA 3.1 model does not currently support Chinese, it performs well in English and Japanese. We are exploring solutions to extend support to additional languages.
- **Automatic Speech Recognition (ASR)**: Speak directly to your AI characters; let them hear your voice. （Comparing Qwen-Audio, whisper, etc.）
- **Text-to-Speech (TTS)**: Hear your favorite characters respond with actual voiced dialogue, bringing them closer to reality. (Considering GPT-SoVITS, etc.)

## ✨ Features

- 🚀 Engage in real-time conversations with AI that mimic beloved anime characters.
- 📖 Save and load custom conversation histories, creating your own story as you go.
- 🌏 Operates on Beijing time, ready for a global audience.
- 📚 Dynamic conversation histories and colorful text highlights.
- 🎯 Optimized performance through quantization for those intense.

## 🎒 Prerequisites

- Python 3.8 or newer
- PyTorch with CUDA support to handle the fire of your anime heroes (8 GB minimum, 12 GB recommended for full power!)
- Transformers library for all the dialogue magic

## 🚀 Installation

1. Clone the spirit of AIKano:

   ```bash
   git clone https://github.com/wbs2788/AIKano
   cd AIKano
   ```

2. Install the libraries:

   ```bash
   pip install -r requirements.txt
   ```

**Embark on this journey with a virtual environment to keep your powers contained and ready!**

## 🌟 Usage

Use AIKano by running:

```bash
python main.py
```

Choose your path by loading an existing saga or starting a new epic. Command the AI with your keyboard and dive into adventures!

### Commands

- 🗨️ Chat away and watch the story unfold with every message.
- 🚪 Type 'quit' when you need to retreat and save the realm.

## 🔧 Customizing Your AI

The AIKano project is highly customizable, allowing users to change the character persona of the AI to suit different narratives or themes. Initially configured to emulate Jean Gunnhildr from Genshin Impact, the model can easily be adapted to simulate other characters or personalities.

### Changing Character Persona

To change the character persona:

1. Edit the initial message in the conversation history JSON file to reflect the new character's attributes and speech style.
2. Adjust the `role` and `content` keys in the history JSON file to match the new character.
3. Optionally, modify the response generation settings (such as `top_k` and `top_p`) to suit the new character’s typical dialogue style.

### Example Characters

- **Diluc from Genshin Impact**: A reserved and dignified businessman with a vigilant yet caring demeanor.
- **Sherlock Holmes**: Known for his sharp observational skills and deductive reasoning.
- **Mikasa Ackerman from Attack on Titan**: A strong and protective persona, usually stoic but deeply emotional about her close ones.

By customizing these elements, you can engage the AI in various thematic dialogues, making it suitable for different applications such as gaming, storytelling, or educational tools.

## 🤝 Contributing

Heroes wanted! If you're ready to add your magic to AIKano, check out `CONTRIBUTING.md`. Together we can craft the most enchanting AI conversations.

## 📜 License

Embark on this quest freely — AIKano is shared under the MIT License. See the [LICENSE](LICENSE) for the saga details.

## 🌸 Acknowledgments

- Thanks to the mages at Hugging Face for the Transformers library.
- Shoutout to the PyTorch wizards for their phenomenal framework.
- Eternal gratitude to the creators of Genshin Impact for inspiring us with Jean Gunnhildr.
- A special thanks to Jean Gunnhildr, the wind that guides us, for inspiring this project and bringing a touch of Teyvat to our digital world.

## 📬 Contact

Should you have inquiries or require assistance, open an issue in our [GitHub repository](https://github.com/wbs2788/AIKano).

