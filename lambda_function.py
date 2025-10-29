import json
import urllib.request
import random
import os
import boto3

def lambda_handler(event, context):
    # Random emojis & reactions
    emojis = ["🔥", "🤯", "😎", "🦄", "💥", "🛸", "🤖", "🐍", "⚡"]
    reactions = [
        "David has done it again"
        "The CI/CD gods are pleased!",
        "Your pipeline just flexed its muscles 💪",
        "Lambda unleashed chaos successfully.",
        "Mission accomplished... probably.",
        "CodePipeline woke up and chose violence 🔥"
    ]

    # Fetch a random dad joke
    try:
        req = urllib.request.Request(
            "https://icanhazdadjoke.com/",
            headers={"Accept": "application/json"}
        )
        res = urllib.request.urlopen(req)
        joke = json.loads(res.read()).get("joke", "No joke found 🤔")
    except Exception as e:
        joke = f"Failed to fetch joke: {e}"

    # Build chaotic output
    crazy_output = {
        "David see" :" -it worked - again - I've added Manual Approval",
        "joke": joke,
        "emoji": random.choice(emojis),
        "reaction": random.choice(reactions),
        "build_id": random.randint(1000, 9999),
        "from_env": os.environ.get("AWS_EXECUTION_ENV", "unknown")
    }

    print("🔥 CI/CD Chaos Log:", json.dumps(crazy_output, indent=2))
    return {
        "statusCode": 200,
        "body": json.dumps(crazy_output)
    }
