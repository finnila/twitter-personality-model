# Twitter Personality Prediction Model

A machine learning project that predicts Myers-Briggs Type Indicator (MBTI) personality types from Twitter user data and tweets.

## Project Overview

This project aims to predict a Twitter user's MBTI personality type using their Twitter activity data and tweet content. The model analyzes various features including:
- Tweet content and language patterns
- User engagement metrics
- Account statistics
- Following/follower relationships

## Data

The project uses the following data sources:
- `user_tweets.csv`: Contains tweets and user activity data
- `mbti_labels.csv`: Contains MBTI personality labels for users
- `user_info.csv`: Contains user information 
- `edges.csv`: Contains following/follower relationships between users

### Features Used
- Tweet text (processed and embedded using SentenceTransformer)
- User metrics (followers, following, tweet counts, etc.)
- Engagement metrics (retweets, favorites, etc.)
- Network relationships between users

## Methodology

The project implements three different approaches to personality prediction:

1. **16-class Classification**
   - Treats each MBTI type as a separate class
   - Achieves 17.22% accuracy (better than random 6.25%)

2. **4-dimension Classification**
   - Predicts each MBTI dimension separately (I/E, S/N, T/F, J/P)
   - Dimension accuracies:
     - I/E (Introvert/Extrovert): 57.6%
     - S/N (Sensing/iNtuitive): 78.1%
     - T/F (Thinking/Feeling): 63.7%
     - J/P (Judging/Perceiving): 55.8%

3. **Text-only Classification**
   - Uses only tweet content for prediction
   - Leverages SentenceTransformer for text embeddings

## Key Findings

- The model performs significantly better than random guessing
- Best performance in predicting the S/N (Sensing/iNtuitive) dimension
- Notable class imbalance in the dataset:
  - More introverted types than extroverted
  - Higher representation of intuitive types over sensing types
- Tweet metrics alone show weak correlation with personality types

## Implementation Details

### Technologies Used
- Python
- Pandas for data processing
- SentenceTransformer for text embeddings
- Scikit-learn for machine learning models
- RandomForestClassifier as the main model

### Model Features
- Text embeddings from SentenceTransformer ('all-MiniLM-L6-v2')
- Standardized numerical features
- One-hot encoded categorical variables
- Balanced class weights to handle imbalanced data

## Future Improvements

- Collect more balanced dataset across personality types
- Experiment with different text embedding models
- Incorporate more sophisticated network analysis
- Try ensemble methods combining different classification approaches

## Results Visualization

The project includes various visualizations:
- MBTI type distribution
- Tweet metrics by personality type
- Follow relationship patterns between different types
- Model performance metrics

## Limitations

- Class imbalance in the dataset
- Potential self-selection bias in personality type labels
- Limited to English language tweets
- Accuracy constraints due to the complexity of personality prediction