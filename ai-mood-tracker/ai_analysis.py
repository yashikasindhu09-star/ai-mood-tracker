from openai import OpenAI

# Direct API key usage (OK for quick demo)
client = OpenAI(api_key="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")

def analyze_mood(text):
    prompt = f"""
    Classify the emotion of the following text as one of:
    Happy, Sad, Stressed, Anxious, or Neutral.

    Also give ONE short wellness suggestion.

    Respond ONLY in this format:
    Mood: <mood>
    Suggestion: <suggestion>

    Text: {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    lines = response.choices[0].message.content.strip().split("\n")

    mood = lines[0].replace("Mood:", "").strip()
    suggestion = lines[1].replace("Suggestion:", "").strip()

    return mood, suggestion
