# Recipe Recommendation System
## Overview

The Recipe Recommendation System is a web-based application designed to suggest the top N recipes based on the ingredients provided by the user. The system uses a dataset of recipes, implements a machine learning model for recommendation, and is deployed for easy access via the web.

## Features

- Ingredient-based Recipe Suggestions: Enter ingredients to get a list of recipes.

- User-Friendly Interface: A simple and intuitive interface for users.

- Fast Recommendations: Powered by a pre-trained model for quick results.

## Tech Stack

### Frontend

- HTML

- CSS

### Backend

- Python (Flask framework)

### Database

- No separate database is used. The system directly uses the provided dataset.

### Deployment

- The application is deployed on Render.

## Dataset

- The dataset contains cleaned and preprocessed recipes in a CSV format.

- The ingredients.txt file lists available ingredients for reference.

## Implementation Details

1. Model Training: The recommendation model is pre-trained and saved as model_n.pkl.

2. Core Logic: Implements the recommendation system using cosine similarity and machine learning techniques.

3. Integration:

  - Flask connects the frontend and backend.

  - The dataset is loaded directly for processing without additional database integration.
