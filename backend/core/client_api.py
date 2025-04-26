import aiohttp

async def ai_response1(guess: str, seed: str, persona="serious") -> str:
    persona_intro = {
        "serious": "You are a factual game master.",
        "cheery": "You are a cheerful and witty game host!",
        "tricker": "You like to trick players by making them self doubt!"
    }
    prompt = (
        f"You are given two items, '{guess}' and '{seed}'. "
        f"Describe in one word whether '{guess}' has upper hand than '{seed}' in a competition in just YES OR NO"
    )

    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:11434/api/chat', json={
                "model": "mistral",
                "messages": [{"role": "user", "content": prompt}],
                "stream":False
            }) as response:
                response.raise_for_status()  # Raise an exception for non-2xx responses
                data = await response.json()  # Await the response as JSON
                print(data)
                return data["message"]["content"].strip()

async def ai_response2(guess: str, seed: str, persona="serious") -> str:
    persona_intro = {
        "serious": "You are a factual game master.",
        "cheery": "You are a cheerful and witty game host!",
        "tricker": "You like to trick players by making them self doubt!"
    }
    prompt = (
        f"{persona_intro[persona]} You are given two items, '{guess}' and '{seed}'. "
        "Describe in short which one has the upper hand in a competition and why. "
        f"Give an interesting explanation. Also, the last line should include 'so {guess} is winner' if it wins the battle."
    )

    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:11434/api/chat', json={
                "model": "mistral",
                "messages": [{"role": "user", "content": prompt}],
                "stream":False
            }) as response:
                response.raise_for_status()  # Raise an exception for non-2xx responses
                data = await response.json()  # Await the response as JSON
                print(data)
                return data["message"]["content"].strip()
