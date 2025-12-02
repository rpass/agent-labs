from agent_tools.forex_tool import get_exchange_rate


def main():
    print("Hello from agent-labs!")
    print("I'm going to show you how the forex tool works...")
    print("I'm going to get the exchange rate for GBP to ZAR")
    print(get_exchange_rate(currency_from="GBP", currency_to="ZAR"))


if __name__ == "__main__":
    main()
