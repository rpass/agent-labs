#!/usr/bin/env python3
"""Test script for the agent - can be run from console."""

import asyncio
import sys

from agent import app


async def test_agent(message: str = None, user_id: str = "test_user"):
    """Test the agent with a query."""
    if message is None:
        message = "What is the exchange rate from US dollars to SEK today?"

    print(f"Testing agent with message: {message}\n")
    print("Agent response:\n")

    async for event in app.async_stream_query(
        user_id=user_id,
        message=message,
    ):
        print(event)


def main():
    """Main entry point for the test script."""
    # Allow passing a custom message as command line argument
    message = sys.argv[1] if len(sys.argv) > 1 else None

    # Run the async test
    asyncio.run(test_agent(message))


if __name__ == "__main__":
    main()
