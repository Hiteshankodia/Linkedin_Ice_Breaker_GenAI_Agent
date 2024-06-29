
import os
#from langchain_google_genai import GoogleGenerativeAIEmbeddings
#Converting text to vectors by Google Embeddings 

import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkedin_profile
load_dotenv()
#os.getenv("API_KEY")
#genai.configure(api_key=os.getenv("API_KEY"))

if __name__ == "__main__":

    print("Hello LangChain")
    

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    
    lmodel = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3)
    
    chain = summary_prompt_template | lmodel
    information = scrape_linkedin_profile(
            linkedin_profile_url = 'https://www.linkedin.com/in/eden-marco/', 
            mock=True
        )
    res = chain.invoke(input={"information": information})

    print(res.content)
