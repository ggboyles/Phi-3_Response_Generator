# This file defines the `Phi3SentimentAnalyzer` class, which processes product reviews,
# summarizes each review in one sentence, and determines its sentiment (positive, neutral, or negative).

import ollama

class Phi3SentimentAnalyzer:
    def __init__(self, model="phi3"):
        self.model = model

    def get_response(self, prompt):
        # Sends prompt to the Phi-3 model loaclly and retrieves the response
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": f"Summarize this comment in one sentence and state if it is positive, negative, or neutral. Comment: {prompt}"
                    }
                ],
            )
            return response["message"]["content"]
        except Exception as e:
            return f"Error: {str(e)}"

    def analyze_sentiment(self, input_path, output_path, max_reviews=None):
        # Reads reviews from a file, determines sentiment, and writes results to output file
        try:
            # Read and split reviews from file
            with open(input_path, "r") as file:
                reviews = file.read().split("\n----------------------------------------\n")
                if max_reviews:
                    reviews = reviews[:max_reviews]

            results = []
            sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}  # Initialize sentiment counts

            # Processes each review
            for review in reviews:
                response_content = self.get_response(review.strip())  # Get model response

                # Extracts sentiment based on response
                if "positive" in response_content.lower():
                    sentiment = "positive"
                    sentiment_counts["positive"] += 1
                elif "negative" in response_content.lower():
                    sentiment = "negative"
                    sentiment_counts["negative"] += 1
                elif "neutral" in response_content.lower():
                    sentiment = "neutral"
                    sentiment_counts["neutral"] += 1
                else:
                    sentiment = "Error"

                # Appends review and sentiment to results
                results.append(f"Review: {review.strip()}\nSentiment: {sentiment}\n")

            # Writes results to output file
            with open(output_path, "w") as file:
                file.write("\n".join(results))
            print(f"Sentiments saved to {output_path}")
            return sentiment_counts
        except FileNotFoundError as e:
            print(f"Error: {str(e)}")
            return None
