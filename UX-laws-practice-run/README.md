# UX-laws-practice-run
trying to create a program that helps remmembering the important UX-laws



**Entries and comments for README.MD from Yainra's contributions**
**1. Main idea for the project**
    Folder structure:
    scraps/
    |
    |--- main.py
    |--- question_table.py
    |--- utils/
    |       |---input_handler.py
    |       |---score_tracker
    |
    |--- data/
    |       |---questions.json
    |
    |--- README.md

    The rough sketch I'm going for would be a modular code that would be easy to swap in and out depending on the needs. As such, I intend to write a basic form of a quiz where the table of questions and answer keys can be swapped out, added to or taken away as needed.
        1.1 main.py: 
            The main block of code and logic handling for the quiz-like game. 
        1.2 question_table.py:
            Table of questions to be asked and the answer keys, with an explanation for either correct or incorrect answers.
                1.2: Example 
                ```
                questions = [
                    {"question": "What is the capital in Norway", "answer": "Oslo"},
                    {"question": "Who wrote '1984'?", "answer": "George Orwell"},
                    #...
                ]
                ```
        1.3  utils/  - helper functions for input validation, scoring and whatever else would be needed.
                input_handler.py
                score_tracker.py
        1.4 data/   - external question seets for easy swapping/choosing?
            question.json
            Unsure how this would work as I haven't used .json before, but for adding scope/flexibility? Could be worth to push argument to "select" a list of questions and asnwers when first starting said quiz? Would certainly be worthwhile for modularity.
                ```
                import json
                def load_questions(filepath):
                    with open(filepath 'r') as f:
                        return json.load(f)
                ```
        1.5 README.md
            Self explanatory I hope?

**2. Further ideas**
    The example used in 1.2 could be expanded upon further to include options if need be. example
        ```
        questions = [
            {
                "question": "What is the capital in Norway?",
                "answer": "Oslo",
                "explanation": "Oslo is the capital of Norway"
                "options": ["Vardø", "Kristiansand", "Bergen", "Trondheim"]
            }, 
            ...
        ]
        ```
    
-------

