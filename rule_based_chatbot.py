from typing import Optional

responses = {
    "hello": "Hi! How can I help you today?",
    "hi": "Hey! What's up?",
    "hey": "Hello! Good to see you.",
    "how are you": "I'm just a chatbot, but I'm doing great!",
    "what is your name": "I'm RuleBot, a rule-based assistant built for DecodeLabs.",
    "who are you": "I'm RuleBot — a logic-driven chatbot, not a learning AI (yet!).",
    "what can you do": "I can chat using predefined rules. Type 'help' to see some topics.",
    "thanks": "You're welcome!",
    "thank you": "Anytime!",
    "help": "Try asking me: hello, how are you, what is your name, what can you do, or just say bye to leave.",
    "weather": "I can't check live weather yet — that's outside my rule-based logic for now!",
}


exit_commands = {"exit", "quit", "bye", "goodbye", "see you"}


def sanitize(raw_input: str) -> str:
    return raw_input.lower().strip()


def match_intent(clean_input: str) -> Optional[str]:
    for keyword, reply in responses.items():
        if keyword in clean_input:
            return reply
    return None


def get_bot_reply(raw_input: str) -> str:
    clean_input = sanitize(raw_input)
    reply = match_intent(clean_input)
    return reply if reply is not None else "I do not understand. Type 'help' to see what I can talk about."


def is_exit_command(clean_input: str) -> bool:
    return any(cmd in clean_input for cmd in exit_commands)


def main():
    print("Bot: Hello! I'm RuleBot. Type 'help' for topics, or 'bye' anytime to leave.")

    while True:  
        raw_input_text = input("You: ")
        clean_input = sanitize(raw_input_text)

        if is_exit_command(clean_input):
            print("Bot: Goodbye! Have a great day.")
            break  

        reply = get_bot_reply(raw_input_text)
        print(f"Bot: {reply}")


if __name__ == "__main__":
    main()