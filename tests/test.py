import pytest
from aiohttp import ClientSession

BASE_URL = "http://127.0.0.1:8000"

@pytest.mark.asyncio
async def test_duplicate_guess_game_over():
    user_id = "1"

    async with ClientSession() as session:
        # Start the game
        start_resp = await session.post(f"{BASE_URL}/start", json={"id": user_id})
        assert start_resp.status == 200
        start_data = await start_resp.json()
        assert start_data["message"] == "Game started"

        # First guess
        first_guess_resp = await session.post(f"{BASE_URL}/guess", json={
            "id": user_id,
            "guess": "paper",
            "persona": "serious"
        })
        assert first_guess_resp.status == 200
        first_guess_data = await first_guess_resp.json()
        assert "message" in first_guess_data

        # Duplicate guess
        duplicate_guess_resp = await session.post(f"{BASE_URL}/guess", json={
            "id": user_id,
            "guess": "paper",  # Same guess again
            "persona": "serious"
        })
        assert duplicate_guess_resp.status == 200
        duplicate_data = await duplicate_guess_resp.json()
        assert duplicate_data["message"] == "Game Over! Duplicate guess."
        assert "history" in duplicate_data
