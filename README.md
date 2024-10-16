# Analyze text with LLM

This workshop is based on a collaboration with Babylotse, a program offered by Kinderschutzbund –
Bezirksverband Frankfurt am Main e. V.. We extend our sincere thanks to Nicola Küpelikilinc (<babylotse@kinderschutzbund-frankfurt.de>) for her permission to publish and use the data.

![approach](./approach.png)

## Setup

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
1. Clone this repo `git clone https://github.com/CorrelAid/workshop-babylotse.git`
1. Open your terminal and navigate to the repository (which I will call `root` directory)
1. Run `uv venv` to create a new virtual environment `.venv` with all the dependencies listed in `pyproject.toml`. Alternatively, you can also run `uv sync`, if you are already in a fresh environment (like conda)
1. Now you can use either your IDE or `jupyter lab` to access the notebooks

### Using LLM

To be able to use a LLM, you need to either have one installed locally (see [Ollama](https://ollama.com/)), or you need an API key.

- Use [OpenAI Platform](https://platform.openai.com/), register for an account and create your [API key](https://platform.openai.com/api-keys)
- Use [Groq Cloud](https://console.groq.com/login), register for an account and create your [API key](https://console.groq.com/keys)

I have listed the packages for each API as an optional dependency, thus you have to install the related Python library.

For openai:

```bash
uv sync --extra openai
```

For Groq:

```bash
uv sync --extra groq
```

Now you have to put your API key into the `.env` file:

1. Copy `.env.default` and rename it to `.env`
2. Fill in your API key for either OpenAI or Groq

You are ready to start with the notebooks!
