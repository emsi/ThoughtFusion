def get_critic_prompt(question, response):
    """Get critic prompt"""
    return (
        f"--> Question:\n{question}\n\n\n--> Answer :\n{response}\n\n\n"
        " Please review provided answer and find any potential problems or issues.\n"
        " Don't be too picky.\n"
        " If you think that the answer is correct, please answer with 'ALL GOOD' (without quotes)."
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
            "content": """"What is the relation shown by the equation C=59(F−32)?"\n\nWhat would be the best persona to answer above question and the critic to review the answers?""",
        },
        {"role": "assistant", "content": "Math Teacher\nPhysics Professor"},
        {
            "role": "user",
            "content": f""""{question}"\n\nWhat would be the best persona to answer above question and the critic to review the answers?""",
        },
    ]
    return messages
