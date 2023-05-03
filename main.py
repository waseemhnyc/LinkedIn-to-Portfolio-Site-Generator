import shutil
import subprocess
import os

from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter

from dotenv import load_dotenv
load_dotenv()

def create_mdx_file(filename, content):
    with open(filename, "w") as mdx_file:
        mdx_file.write(content)

def upload_to_vercel():
    project_directory = "nextjs-portfolio-starter"

    os.chdir(project_directory)

    build_command = "vercel build --yes --yes"
    deploy_command = "vercel deploy --prebuilt"

    try:
        subprocess.run(build_command, check=True, shell=True)
        subprocess.run(deploy_command, check=True, shell=True)
        shutil.rmtree(".vercel")
        shutil.rmtree(".next")
        print("The .vercel and .next folders have been removed.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during deployment: {e}")

    except FileNotFoundError as e:
        print(f"Error removing folder: {e}")


loader = PyPDFLoader("../../Downloads/Profile.pdf")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
splitted_documents = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

db = Chroma.from_documents(splitted_documents, embeddings)

chat = ChatOpenAI(temperature=0, model_name="gpt-4")
chain = RetrievalQAWithSourcesChain.from_chain_type(
    llm=chat,
    chain_type="stuff",
    retriever=db.as_retriever(search_kwargs={"k": 1}),
)

result = chain({ "question": "Respond with this profiles first name, only" })
first_name = result["answer"]
print('First Name:', first_name)

result = chain({ "question": "Summarize all skills, experiences and about this profile. This description should catch the eye of the reader. Write in 1st person. Keep response short - like 3-5 sentences." })
description = result["answer"]
print('Description:', description)

result = chain({ "question": "List all of this profiles experiences in markdown format, include information about each experience. No code blocks." })
experiences = result["answer"]
print('Experiences:', experiences)

result = chain({ "question": "List all of this profiles contact info in markdown format. Following the format [Duck Duck Go](https://duckduckgo.com). No code blocks." })
urls = result["answer"]
print('Contact URLs:', urls)

index_content = f'''
# Hey 👋 my name is {first_name}

{description}

---

Experience
----------
{experiences}

---

Contact or Find Me Here
----------
{urls}
'''

mdx_filename = "nextjs-portfolio-starter/pages/index.mdx"
create_mdx_file(mdx_filename, index_content)
input("Press Enter to continue...")
upload_to_vercel()
