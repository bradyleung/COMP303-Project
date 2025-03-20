import time
from mistralai import Mistral
import os

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-small-latest"

class APIWrapper:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = Mistral(api_key=api_key)
            cls._instance.last_request_time = 0  # Track the time of the last request
            cls._instance.request_interval = 6  # Minimum time in seconds between requests
        return cls._instance

    def get_response(
        self,
        prompt: str,
        temperature: float,
        frequency_penalty: float,
        presence_penalty: float,
    ) -> str:
        """
        Sends a prompt to the Mistral AI API and returns the response.
        Ensures a minimum wait time between requests to avoid rate limits.
        """
        try:
            # Calculate the time since the last request
            current_time = time.time()
            time_since_last_request = current_time - self.last_request_time

            # If the time since the last request is less than the required interval, wait
            if time_since_last_request < self.request_interval:
                time_to_wait = self.request_interval - time_since_last_request
                time.sleep(time_to_wait)

            # Update the last request time
            self.last_request_time = time.time()

            # Make the API request
            chat_response = self.client.chat.complete(
                model = model,
                max_tokens = 80,  # 
                messages = [{"role": "user", "content": prompt}],
                temperature = temperature,
                frequency_penalty = frequency_penalty,
                presence_penalty = presence_penalty,
            )
            return chat_response.choices[0].message.content

        except Exception as e:
            return f"Sorry, I'm busy right now! I'm trying to deal with {str(e)}"