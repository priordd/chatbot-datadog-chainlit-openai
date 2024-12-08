# Chatbot with Datadog, Chainlit, and OpenAI Integration

A powerful and interactive chatbot application built with **Chainlit**, integrated with **OpenAI's GPT models**, and enriched by **Datadog** observability for monitoring and logging.

---

## 🚀 Features

- **OpenAI GPT Integration**: Leverage state-of-the-art AI for conversational capabilities.
- **Chainlit Interface**: A streamlined and intuitive framework for building conversational agents.
- **Datadog Observability**: Monitor application performance, track logs, and visualize metrics with ease.
- **Customizable**: Easily adaptable to various use cases by modifying configurations and prompts.

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.11+](https://www.python.org/downloads/)
- [Datadog Agent](https://docs.datadoghq.com/agent/)

You'll also need API keys for:

- **OpenAI**: [Sign up here](https://platform.openai.com/signup/).
- **Datadog**: [Get your API key here](https://app.datadoghq.com/account/settings#api).

---

## 🛠 Installation

1. Clone the repository:

```bash
git clone https://github.com/priordd/chatbot-datadog-chainlit-openai.git
cd chatbot-datadog-chainlit-openai
```

2. Set up a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Configure your environment variables:

    * Copy the .env.example to .env file in the project root.
    * Fill all the required keys.

```shell
mv env.example .env  # Fill all the required keys
```

---

## 🔧 Usage

Run the application:

```
python app.py
```

Open your browser and navigate to the Chainlit interface (usually http://localhost:8000).

Start interacting with your AI-powered chatbot!

---

## 🌟 Highlights

#### OpenAI Integration

- Custom prompts and fine-tuned responses for engaging user interactions.
- Supports multiple GPT model configurations.

#### Datadog Observability

- Real-time metrics and logs for tracking bot performance and errors.
- Simple setup for monitoring system health.

#### Chainlit Framework

- User-friendly interface for building and deploying chatbots quickly.
- Supports customization for branding and additional features.

---

## 🐛 Troubleshooting

#### Common Issues

- Missing API Keys: Ensure all required keys are set in the .env file.
- Dependencies Not Installed: Double-check that all dependencies are installed using:

```
pip install -r requirements.txt
```

#### Logging

- View detailed logs in your terminal or Datadog dashboard for debugging.

#### If you're still in trouble...

- Open an [Issue](https://github.com/priordd/chatbot-datadog-chainlit-openai/issues)

---


## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:

```
git checkout -b feature-name
```
3. Commit your changes and push:

```
git commit -m "Description of changes"
git push origin feature-name
```
4. Submit a pull request for review.

### 🏃‍♂️ Fast track development environment

If you know this code, you certainly know what you're doing ;):

```shell
    poetry install
    mv env.example .env  # Fill all the required keys
    poetry run chainlit run app.py -w  # Run chat interface
    poetry export --without-hashes --format=requirements.txt > requirements.txt  # Export `requirements.txt`
```

## 📜 License

This project is licensed under the [MIT License](LICENSE).


# References

- https://docs.datadoghq.com/llm_observability/
- https://github.com/Chainlit/chainlit
- https://platform.openai.com/docs/concepts
- https://platform.openai.com/api-keys
- https://python.langchain.com/docs/introduction/
- https://medium.com/@tahreemrasul/how-to-build-your-own-chatbot-with-langchain-and-openai-f092822b6ba6
