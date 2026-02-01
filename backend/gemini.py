from google import genai

client = genai.Client(api_key = "AIzaSyCYu1ulr3pbvaeE62MvJCT1rtRtpKrtWy0")

def parse_requirements(query: str) -> dict:
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=f"Convert the following request into JSON with fields: energy_type, region, min_area_acres, criteria, constraints. Request: {query}")    
    print(response.text)   
    return response.text
