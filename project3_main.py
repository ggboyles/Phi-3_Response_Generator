# Processes reviews, analyzes sentiments with Phi-3, and generates sentiment graph.

import os
from phi3_sentiment_analyzer import Phi3SentimentAnalyzer
from graph_generator import generate_sentiment_graph

def main():
    analyzer = Phi3SentimentAnalyzer(model="phi3")

    input_folder = "reviews"
    output_folder = "sentiments"
    sentiment_counts = {}

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)  # Use same name as input
            print(f"Processing file: {input_path}")

            # Analyzes sentiment
            counts = analyzer.analyze_sentiment(input_path, output_path, max_reviews=10)

            # Collect counts for graph
            sentiment_counts[os.path.splitext(filename)[0]] = counts

    # Generates graph
    generate_sentiment_graph(sentiment_counts)
    print("Graph generated and saved as 'sentiment_graph.png'.")

if __name__ == "__main__":
    main()
