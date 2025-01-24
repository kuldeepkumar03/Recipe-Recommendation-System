from flask import Flask, render_template, request, jsonify
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Load the model components
with open('model_n.pkl', 'rb') as file:
    model_data = pickle.load(file)

vectorizer = model_data['vectorizer']
ingredient_matrix = model_data['ingredient_matrix']
recipes_df = model_data['recipes']

# Recommendation logic
def recommend_recipes_by_ingredients(input_ingredients, top_n=5):
    # Preprocess user input
    user_ingredients = set(map(str.strip, input_ingredients.lower().split(',')))
    
    recommendations = []

    for index, row in recipes_df.iterrows():
        # Process recipe ingredients
        recipe_ingredients = set(map(str.strip, row['Ingredients'].lower().split(',')))
        
        # Check if all user ingredients are present in the recipe
        if user_ingredients.issubset(recipe_ingredients):
            # Calculate extra ingredients
            extra_ingredients = list(recipe_ingredients - user_ingredients)
            extra_ingredients_count = len(extra_ingredients)
            recommendations.append({
                'Recipe Name': row['Recipe Name'],
                'Extra Ingredients Count': extra_ingredients_count,
                'Extra Ingredients': ', '.join(extra_ingredients),  # Corrected key
                'Link': row['Link']
            })

    # Sort by extra ingredients count (ascending)
    recommendations = sorted(recommendations, key=lambda x: x['Extra Ingredients Count'])
    
    # Return the top N recipes
    return pd.DataFrame(recommendations[:top_n])

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    ingredients = request.form.get('ingredients', '').strip()
    if not ingredients:
        return jsonify({'error': 'No ingredients provided!'}), 400

    try:
        recommendations_df = recommend_recipes_by_ingredients(ingredients)
        recommendations = recommendations_df.to_dict(orient='records')
        return jsonify({'recommendations': recommendations})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



# Run the application
if __name__ == '__main__':
    app.run(debug=False)
