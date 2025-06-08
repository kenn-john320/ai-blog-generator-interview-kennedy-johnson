# Get the OpenAPI SDK
from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Python library to get the env
from dotenv import load_dotenv

# Load env variables and initialize OPENAI Api Key
load_dotenv()

def generate_blog(keyword, random_metrics):
    fakePrompt = f"""
Imagine you are a professional SEO content writer.
    
Write a detailed blog post about "{keyword}" including these sections:
    
- An Introduction Section
- Key Insights
_ Product suggestions (use placeholders with the format of {{AFF_LINK_1}}, {{AFF_LINK_2}})
- Conclusion paragraph with a summary of what has been discussed"

SEO Metrics:
- Search Volume: {random_metrics["search_volume"]}
- Keyword Difficulty: {random_metrics["keyword_difficulty"]}   
- Avg CPC: ${random_metrics["averageClicksperCost"]}
    
Make this blog engaging, and include HTML tags for the headings, paragraphs and links associated.
    """

    # Uses GPT 4
    response = client.chat.completions.create(model= "gpt-4",
    messages= [{"role": "user", "content": fakePrompt}],
    temperature = 0.8)

    content = response.choices[0].message.content
    return content.replace("{{AFF_LINK_1}}", "https://examplesite.com/product1")\
        .replace("{{AFF_LINK_2}}", "https://examplesite.com/product2")