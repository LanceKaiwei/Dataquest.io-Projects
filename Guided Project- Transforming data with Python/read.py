def load_data():
    import pandas as pd
    stories = pd.read_csv("hn_stories.csv", header=None)
    stories.columns = ["submission_time", "upvotes", "url", "headline"]
    return stories

if __name__ == "__main__":
    load_data()


#echo -e 'if __name__ == "__main__":\n    print("Welcome to a Python script")' > script.py     