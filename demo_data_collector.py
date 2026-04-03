import json
import time
import random

# ── DEMO SETTINGS ─────────────────────────────
OPENAI_MODEL = "gpt-4o-mini"
DELAY_BETWEEN_ROWS = 1

SENTIMENT_OPTIONS = [
    "Bullish",
    "Slightly Bullish",
    "Neutral",
    "Slightly Bearish",
    "Bearish"
]

# Dummy dataset
data_rows = [
    {"Ticker": "AAPL", "News Paragraph": "Apple releases record quarterly earnings."},
    {"Ticker": "TSLA", "News Paragraph": "Tesla faces supply chain issues affecting production."},
    {"Ticker": "AMZN", "News Paragraph": "Amazon announces new AI-driven logistics initiative."}
]

# ── DEMO FUNCTIONS ───────────────────────────

def analyze_sentiment_demo(ticker, news_paragraph):
    """
    Demo version of sentiment analysis.
    In production, this would call OpenAI API for real analysis.
    """
    result = {
        "sentiment": random.choice(SENTIMENT_OPTIONS),
        "headline": f"Demo headline for {ticker}",
        "reasoning": "This is a demo reasoning based on the news paragraph.",
        "confidence_score": random.randint(50, 100)
    }
    return result


def run_demo_pipeline():
    processed = 0
    for row_idx, row in enumerate(data_rows, start=1):
        ticker = row.get("Ticker", "")
        news_paragraph = row.get("News Paragraph", "")

        if not ticker or not news_paragraph:
            print(f"Row {row_idx}: Skipping empty row.")
            continue

        print(f"Row {row_idx} [{ticker}]: Analysing...")
        result = analyze_sentiment_demo(ticker, news_paragraph)
        print(f"Result: {json.dumps(result, indent=2)}\n")
        processed += 1
        time.sleep(DELAY_BETWEEN_ROWS)

    print(f"Demo pipeline completed. Processed {processed} rows.")


if __name__ == "__main__":
    run_demo_pipeline()
