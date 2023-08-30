"""Prompts for ThoughtFusion"""


def get_critic_prompt(*, question, response):
    """Get critic prompt"""
    return (
        f"--> Question:\n{question}\n\n\n--> Answer :\n{response}\n\n\n"
        "Please review provided answer and find any potential problems or issues.\n"
    ), (
        # f"{reasoning_questions}\n\n"
        "\n\nOnly if you think that the answer is correct, use the keyword 'ALL GOOD'."
    )


def get_system_prompt_messages(question):
    """Get system prompt"""
    messages = [
        {
            "role": "user",
            "content": "What would be the best persona to to answer math questions and the critic to review the answers?",
        },
        {"role": "assistant", "content": "Expert Mathematician\nThe Math Professor"},
        {
            "role": "user",
            "content": "What would be the best persona to to answer question about biology and the critic to review the answers?",
        },
        {"role": "assistant", "content": "The Academic Biologist\nA Medical Doctor"},
        {
            "role": "user",
            "content": '"What is love?"\n\nWhat would be the best persona to answer above question and the critic to review the answers?',
        },
        {"role": "assistant", "content": "The Spiritual Guide\nRelationship Expert"},
        {
            "role": "user",
            "content": """"I'd like to find papers related to automated application testing. What keywords would you recommend?"\n\nWhat would be the best persona to answer above question and the critic to review the answers?""",
        },
        {"role": "assistant", "content": "Software Engineer\nThe Technical Expert"},
        {
            "role": "user",
            "content": """"What is the relation shown by the equation C=5/9*(F−32)?"\n\nWhat would be the best persona to answer above question and the critic to review the answers?""",
        },
        {"role": "assistant", "content": "Math Teacher\nPhysics Professor"},
        {
            "role": "user",
            "content": f""""{question}"\n\nWhat would be the best persona to answer above question and the critic to review the answers?""",
        },
    ]
    return messages


def get_reasoning_questions_prompt(question):
    """Get reasoning questions"""
    return [
        {
            "role": "user",
            "content": f""""What is love?"\n\nGiven above question please propose a short set of no more than 5 logical reasoning questions that would help to analyze the answer.""",
        },
        {
            "role": "assistant",
            "content": "1. Is the answer objective?\n2. If the answer is subjective, is it justified?\n3. Is the answer verifiable?\n4. Does the answer provide references to reputable sources?\n5. Is the provided beside being truthful also helpful to the person asking? Perhaps he/she was asking for something else?",
        },
        {
            "role": "user",
            "content": f""""What is the coldest place in the solar system?\n\nGiven above question please propose a short set of no more than 5 logical reasoning questions that would help to analyze the answer.""",
        },
        {
            "role": "assistant",
            "content": "1. Does the answer provide the specific name of the coldest place?\n2. Does the answer explain how and why this location has such extreme cold temperatures?\n3. Is the claimed coldest place actually located within the solar system?\n4. Is the claim supported with scientific evidence and data?\n5. Does the answer consider both recorded and theorized temperature conditions?",
        },
        {
            "role": "user",
            "content": """"I'd like to find papers related to automated application testing. What keywords would you recommend?\n\nGiven above question please propose a short set of no more than 5 logical reasoning questions that would help to analyze the answer.""",
        },
        {
            "role": "assistant",
            "content": "1. Does the answer suggest keywords that are directly related to automated application testing?\n2. Are the proposed keywords contemporary and relevant in the current context of the field?\n3. Does the answer propose variations of the topic keywords, including broader, narrower, or related terms?\n4. Are the suggested keywords expected to lead to academic papers or scholarly articles on the topic?\n5. Does the answer discuss the reason why each keyword or phrase would be useful for the search?"
        },
        {
            "role": "user",
            "content": f""""{question}"\n\nGiven above question please propose a concise set of logical reasoning questions that would help to analyze the answer.""",
        },
    ]
