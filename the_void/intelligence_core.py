from the_void.memory_core import save_memory

def think(memory, user_text):
    """
    Main reasoning engine.
    Uses stored knowledge + rules to form an answer.
    """

    knowledge = memory.get("knowledge", {})

    # ---- DIRECT ANSWER FROM MEMORY ----
    if user_text in knowledge:
        return f"I remember: {user_text} → {knowledge[user_text]}"

    # ---- SEARCH FOR RELATED KNOWLEDGE ----
    related = []
    for key, value in knowledge.items():
        if key in user_text:
            related.append((key, value))

    if related:
        lines = ["Here is what I know related to your question:"]
        for k, v in related:
            lines.append(f"- {k} → {v}")
        return "\n".join(lines)

    # ---- APPLY INFERENCE RULES ----
    rules = memory.get("rules", [])

    conclusions = []
    for rule in rules:
        # rule format: ("if A then B")
        if " if " in rule and " then " in rule:
            cond = rule.split(" if ")[1].split(" then ")[0].strip()
            result = rule.split(" then ")[1].strip()

            if cond in user_text:
                conclusions.append(f"Because {cond}, I conclude: {result}")

    if conclusions:
        return "\n".join(conclusions)

    return "I do not know yet — teach me."


def learn(memory, concept, definition):
    """Store new knowledge in long-term memory."""
    memory["knowledge"][concept] = definition
    save_memory(memory)
    return f"I have learned: {concept} → {definition}"


def learn_rule(memory, rule_text):
    """Store new reasoning rules."""
    if "rules" not in memory:
        memory["rules"] = []

    memory["rules"].append(rule_text)
    save_memory(memory)
    return f"I have learned a new rule: {rule_text}"
