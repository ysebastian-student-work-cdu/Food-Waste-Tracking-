import requests
import json
'''import requests

url = 'https://api.openai.com/v1/chat/completions'
headers = {'Authorization': 'Bearer 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','Content-Type': 'application/json'}

body = """{
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "user", "content": f"Generate a recipe using the following ingredients: {food_items}"}]
}"""

req = requests.post(url, headers=headers, data=body)

print(req.status_code)
print(req.headers)
print(req.text)'''

def generate_recipe(item1, item2, item3):
    # Concatenate the food item names
    food_items = f"{item1}, {item2}, {item3}"

    # Define the prompt for the ChatGPT API request
    prompt = f"Generate a recipe using the following ingredients: {food_items}"

    # Set your OpenAI API key
    api_key = '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'
    
    # Make the API request to OpenAI ChatGPT3.5 Turbo
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        },
        json={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
             # Adjust the temperature for varied output
        }
    )
    
    print(response)

    # Retrieve the generated recipe from the API response
    if response.status_code == 200:
        data = response.json()
        return data['choices'][0]['message']['content']
    else:
        return 'API call failed'
x= generate_recipe("chicken", "rice", "broccoli")
print(x)