from dt import dt

def run(node):
    """Recursively traverse the decision tree."""
    if isinstance(node, str):
        print("\nGreat picks! Here is your movie! Recommendation Path:", node, "\n")
        return

    question = node["question"]
    answer = input(question).strip().lower()

    branches = node["branches"]
    if answer in branches:
        run(branches[answer])
    else:
        print("Please type one of the provided options. Try again.\n")
        run(node)

if __name__ == "__main__":
    print("Welcome to the Movie Recommendation Decision Tree!\n Made By: Joey Vos\n")
    run(dt)


