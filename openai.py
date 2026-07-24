class OpenAI:
    def __init__(self, *args, **kwargs):
        self.chat = type("Chat", (), {"completions": type("Completions", (), {"create": None})()})()

    def __call__(self, *args, **kwargs):
        return self


__all__ = ["OpenAI"]
