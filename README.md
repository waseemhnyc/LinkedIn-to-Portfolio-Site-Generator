# Linkedin to Portfolio Site Generator

This project is a Python script that scrapes your [Linkedin PDF](https://www.linkedin.com/in/waseemhnyc/) and generates a customized portfolio site using OpenAI's GPT-4 model.

We interact with the GPT-4 model using [LangChain](https://github.com/hwchase17/langchain).

1. Embed the Linkedin PDF
2. Store the embeddings into a Chroma vector database
3. Query that database to get relevant information
4. Generate text with OpenAI's GPT-4
5. With the generated text we use the [Next JS portfolio site](https://github.com/vercel/nextjs-portfolio-starter), powered by [Nextra](https://nextra.site/), to create the main portfolio file
6. Build and deploy site on [Vercel](https://vercel.com/templates/next.js/portfolio-starter-kit)

## Demo

For this demo, I used LangChain's Co-founder and CEO [Harrison Chase](https://twitter.com/hwchase17)'s LinkedIn.

You can find his deployed site here: <https://harrison-six.vercel.app/>
Video: https://www.youtube.com/watch?v=jY5UnSBq8sI

[![Demo Video](assets/screenshot.png)](https://www.youtube.com/watch?v=jY5UnSBq8sI)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Installed a recent version of Python (3.7 or newer) installed and a way to create virtual environments (virtualenv or conda)
- Created a Vercel account and have downloaded/login into Vercel CLI locally
- Created OpenAI API account and obtain an OpenAI API key

## Getting Started

Clone the repo

```bash
git clone https://github.com/waseemhnyc/LinkedIn-to-Portfolio-Site-Generator
```

Create a virutalenv and source the environment

```bash
python3 -m venv myenv
source venv/bin/activate
```

Install the necessary libraries

```bash
pip install -r requirements.txt
```

Create a .env file and input your OpenAI API Key in the file

```bash
cp .env.example .env
```

## Usage

To run the program, run the following command in the terminal:

```bash
python main.py
```

## Ways to Improve

- Accept more inputs like resumes/CVs
- Grab data from Github and Twitter
- Integrate with other portfolio templates
- Push to Github so you could make your own changes
- Use LangChains output parser


## Questions or Get in Touch

- Twitter: https://twitter.com/waseemhnyc
- Email: waseemh.nyc@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE file for details.
