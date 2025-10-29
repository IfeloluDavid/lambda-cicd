import json
import urllib.request
import random
import os
import boto3

def lambda_handler(event, context):
    # Random emojis & reactions
    emojis = ["🔥", "🤯", "😎", "🦄", "💥", "🛸", "🤖", "🐍", "⚡"]
    reactions = [
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

    # Randomly decide to call itself once
    invoked = event.get("invoked", False)
    if not invoked:
        print("Summoning Lambda recursion 🔁")
        lambda_client = boto3.client("lambda")
        lambda_client.invoke(
            FunctionName=os.environ["AWS_LAMBDA_FUNCTION_NAME"],
            InvocationType="Event",
            Payload=json.dumps({"invoked": True})
        )

    # Build chaotic output
    crazy_output = {
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
