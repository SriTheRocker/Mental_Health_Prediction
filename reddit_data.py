pip install praw

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import praw
import warnings
from prawcore.exceptions import Redirect, NotFound, Forbidden  # Add relevant exceptions

import logging

# Suppress praw warnings by setting logging level to ERROR or higher
logging.getLogger("praw").setLevel(logging.ERROR)

# Initialize Reddit instance
reddit = praw.Reddit(client_id="N7DOl9JBD-JRGZwMf-u5AA",
                     client_secret="8Jow6L5T8e5ISabCCeP5VFMSMuZOkw",
                     user_agent="Health_predicton")

# List of mental health-related subreddits
subreddits = [
    'mentalhealth', 'therapy', 'anxiety', 'depression', 'ptsd',
    'bipolar', 'ADHD', 'selfhelp', 'stopgaming', 'decidingtobebetter',
    'mentalhealthsupport', 'sad', 'suicidewatch', 'emotionalhealth', 'stress',
    'chronicpain', 'eatingdisorders','socialanxiety', 'ocd', 'addiction',
    'mentalillness', 'loneliness', 'autism', 'dissociation', 'anger',
    'selfimprovement', 'panicdisorder','borderline', 'schizophrenia', 'mentalwellness',
    'counseling', 'selfcare', 'mindfulness', 'grief','trauma',
    'yoga', 'lifeadvice', 'lifeafterdeath', 'selflove', 'mooddisorders',
    'psychology', 'psychiatry','mentalhealthnews', 'selflove','mentalwellness','counseling'
]

# Loop through each subreddit and save data to separate DataFrame
for subreddit_name in subreddits:
    print(f"Scraping {subreddit_name}...")
    data = []  # Clear the data for each subreddit
    try:
        # Attempt to access the subreddit
        subreddit = reddit.subreddit(subreddit_name)

        # Scrape top 10 posts in each subreddit
        for post in subreddit.top(limit=100):
            # Append post details
            data.append({
                'Subreddit': subreddit_name,
                'Type': 'Post',
                'Post_id': post.id,
                'Title': post.title,
                'Author': post.author.name if post.author else 'Unknown',
                'Timestamp': pd.to_datetime(post.created_utc, unit='s'),
                'Text': post.selftext,
                'Score': post.score,
                'Total_comments': post.num_comments,
                'Post_URL': post.url
            })

            # Check if the post has comments and scrape them
            if post.num_comments > 0:
                post.comments.replace_more(limit=20)  # Load up to 20 more comments
                for comment in post.comments.list():
                    # Append comment details
                    data.append({
                        'Subreddit': subreddit_name,
                        'Type': 'Comment',
                        'Post_id': post.id,
                        'Title': post.title,
                        'Author': comment.author.name if comment.author else 'Unknown',
                        'Timestamp': pd.to_datetime(comment.created_utc, unit='s'),
                        'Text': comment.body,
                        'Score': comment.score,
                        'Total_comments': 0,  # Comments don't have total comments
                        'Post_URL': None  # Comments don't have a separate URL
                    })

    except Redirect:
        print(f"Subreddit {subreddit_name} does not exist. Skipping...")
        continue
    except NotFound:
        print(f"Subreddit {subreddit_name} not found. Skipping...")
        continue
    except Forbidden:
        print(f"Access to subreddit {subreddit_name} is forbidden. Skipping...")
        continue
    except Exception as e:
        print(f"An error occurred while scraping {subreddit_name}: {e}")
        continue

    # Create a pandas DataFrame for this subreddit
    df = pd.DataFrame(data)

    # Save DataFrame to an Excel file with the subreddit name
    file_name = f"{subreddit_name}.xlsx"
    df.to_excel(file_name, index=False)
    print(f"Data for {subreddit_name} saved to {file_name}")


