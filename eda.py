import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_mbti_distribution(df):
    """Plot the distribution of MBTI personalities."""
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='mbti_personality')
    plt.title('Distribution of MBTI Personalities')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_tweet_metrics_by_mbti(df):
    """Plot tweet metrics by MBTI type."""
    tweet_metrics = ['average_tweet_length', 'average_hashtag_count', 
                    'average_mentions_count', 'average_url_count']
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Tweet Characteristics by MBTI Type')

    for i, metric in enumerate(tweet_metrics):
        ax = axes[i//2, i%2]
        avg_metric = df.groupby('mbti_personality')[metric].mean()
        sns.barplot(x=avg_metric.index, y=avg_metric.values, ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        ax.set_title(f'Average {metric.replace("_", " ").title()}')

    plt.tight_layout()
    plt.show()

def plot_followers_by_mbti(df):
    """Plot average follower count by MBTI type."""
    plt.figure(figsize=(12, 6))
    
    avg_followers = df.groupby('mbti_personality')['followers_count'].mean().sort_values(ascending=False)
    sns.barplot(x=avg_followers.index, y=avg_followers.values)
    
    plt.title('Average Follower Count by MBTI Personality Type', fontsize=12, pad=15)
    plt.xlabel('MBTI Personality Type', fontsize=10)
    plt.ylabel('Average Follower Count', fontsize=10)
    plt.xticks(rotation=45)
    
    def format_func(value, tick_number):
        return f'{value/1000:.0f}K'
    
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_func))
    plt.tight_layout()
    plt.show()

def plot_mbti_follow_matrix(edges_df, mbti_df):
    # Create a mapping of user IDs to MBTI types
    user_mbti = dict(zip(mbti_df['id'], mbti_df['mbti_personality']))
    
    # Create a matrix of follow relationships between MBTI types
    mbti_types = sorted(mbti_df['mbti_personality'].unique())
    follow_matrix = pd.DataFrame(0, index=mbti_types, columns=mbti_types)
    
    # Fill the matrix with follow counts
    for _, row in edges_df.iterrows():
        follower_id = row['follower_id']
        followee_id = row['followee_id']
        
        if follower_id in user_mbti and followee_id in user_mbti:
            follower_type = user_mbti[follower_id]
            followee_type = user_mbti[followee_id]
            follow_matrix.loc[follower_type, followee_type] += 1
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(follow_matrix, 
                annot=True, 
                fmt='g',
                cmap='YlOrRd',
                cbar_kws={'label': 'Number of Follows'})
    
    plt.title('Follow Relationships Between MBTI Types')
    plt.xlabel('Followee MBTI Type')
    plt.ylabel('Follower MBTI Type')
    plt.tight_layout()
    plt.show()
    
    return follow_matrix

def analyze_follow_proportions(follow_matrix):
   # Get list of MBTI types
    mbti_types = follow_matrix.index.tolist()
    
    # Calculate proportion of same-type follows for each personality type
    same_type_proportions = pd.Series(index=mbti_types)
    for mbti_type in mbti_types:
        row_sum = follow_matrix.loc[mbti_type].sum()
        if row_sum > 0:  # Avoid division by zero
            same_type_proportion = follow_matrix.loc[mbti_type, mbti_type] / row_sum
            same_type_proportions[mbti_type] = same_type_proportion
        else:
            same_type_proportions[mbti_type] = 0

    # Sort and display results
    print("Proportion of same-type follows by personality:")
    print(same_type_proportions.sort_values(ascending=False).apply(lambda x: f"{x:.2%}"))
    
    return same_type_proportions