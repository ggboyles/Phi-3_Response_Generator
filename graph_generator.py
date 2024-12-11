## Generates a bar chart to visualize positive, neutral, and negative sentiment counts for products.

import matplotlib.pyplot as plt

def generate_sentiment_graph(sentiment_counts):
    products = []
    positive = []
    neutral = []
    negative = []

    # Prepare data for the graph
    for product, counts in sentiment_counts.items():
        products.append(product)
        positive.append(counts.get("positive", 0))
        neutral.append(counts.get("neutral", 0))
        negative.append(counts.get("negative", 0))

    # Create the bar chart
    bar_width = 0.25
    r1 = range(len(products))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]

    plt.bar(r1, positive, color='blue', width=bar_width, label='Positive')
    plt.bar(r2, neutral, color='orange', width=bar_width, label='Neutral')
    plt.bar(r3, negative, color='green', width=bar_width, label='Negative')

    # Add labels and title
    plt.xlabel('Products')
    plt.ylabel('Count')
    plt.title('Sentiment Analysis for Each Product')
    plt.xticks([r + bar_width for r in range(len(products))], products, rotation=45)
    plt.legend()

    # Save the graph
    plt.tight_layout()
    plt.savefig("sentiment_graph.png", dpi=300)
    plt.show()
