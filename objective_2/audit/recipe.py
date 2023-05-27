import requests
import json

class Recipe:
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
        
        # Retrieve the generated recipe from the API response
        if response.status_code == 200:
            data = response.json()
            recipe= data['choices'][0]['message']['content']
            return recipe
        else:
            return 'API call failed'
