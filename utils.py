from google.generativeai.types.model_types import Model as GeminiModel

BOLD = "\033[1m"
RESET = "\033[0m"
GREEN = "\033[32m"
BLUE = "\033[34m"

def print_gemini_model(model: GeminiModel) -> None:
    print(f"{BOLD}{BLUE}{model.name}{RESET} ({model.display_name})")
    print(f"    {GREEN}{model.description}{RESET}")
    print(f"    {BOLD}Max input tokens:{RESET} {model.input_token_limit}")
    print(f"    {BOLD}Max output tokens:{RESET} {model.output_token_limit}")