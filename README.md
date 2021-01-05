# Full Stack API Project: Trivia

## Full Stack Trivia

This project is a virtual bank questions for users. By using this application, the user will be able to:

1. Display questions - both all questions and by category. Questions should show the question, category, difficulty scale, and rating scale by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question, answer text, category, difficulty scale, and rating scale.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/).

## Technical Skills & Concepts:

- API Development and Documentation
- Implementing well formatted API endpoints that leverage knowledge of HTTP and API development best practices.
- The ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

## Table of Contents

- [About the Stack](#About-the-Stack)
- [Getting Started](#Getting-Started)
- [API Reference](#API-Reference)

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup.

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency.

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API.

[View the README.md within ./frontend for more details.](./frontend/README.md)

## Getting-Started

### Pre-requisites and Local Development

Developers using this project should already have Python3, pip and node installed on their local machines.

#### Backend

From the backend folder run `pip install requirements.txt`. All required packages are included in the requirements file.

To run the application run the following commands:

```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

The application is run on `http://127.0.0.1:5000/` by default and is a proxy in the frontend configuration.

#### Frontend

From the frontend folder, run the following commands to start the client:

```
npm install // only once to install dependencies
npm start
```

By default, the frontend will run on localhost:3000.

### Tests

In order to run tests navigate to the backend folder and run the following commands:

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

The first time you run the tests, omit the dropdb command.

All tests are kept in that file and should be maintained as updates are made to app functionality.

## API-Reference

### Getting Started

- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration.
- Authentication: This version of the application does not require authentication or API keys.

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```

The API will return three error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable
- 405: Method Not allowed

#### GET /categories

- General:
  - Returns a dictionary of all available categories with key=id and value=type, and success value.
- Sample: `curl http://127.0.0.1:5000/categories`

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```

#### GET /questions

- General:
  - Returns a dictionary of all available categories, a list of questions objects, success value, and total number of questions
  - Results of questions are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: `curl http://127.0.0.1:5000/questions`

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
      "rating": 1
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
      "rating": 5
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
      "rating": 3
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
      "rating": 4
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?",
      "rating": 2
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?",
      "rating": 3
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?",
      "rating": 2
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?",
      "rating": 1
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?",
      "rating": 5
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?",
      "rating": 4
    }
  ],
  "success": true,
  "total_questions": 18
}
```

#### DELETE /questions/{question_id}

- General:
  - Deletes the question of the given ID if it exists. Returns the id of the deleted question, success value, total questions, dictionary of all available categories, and questions list based on current page number to update the frontend.
- `curl -X DELETE http://127.0.0.1:5000/questions/13?page=1`

```
{
  "categories": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "deleted": 13,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
      "rating": 1
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
      "rating": 5
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
      "rating": 3
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
      "rating": 4
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?",
      "rating": 2
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?",
      "rating": 3
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?",
      "rating": 2
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?",
      "rating": 1
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?",
      "rating": 4
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?",
      "rating": 3
    }
  ],
  "success": true,
  "total_questions": 17
}
```

#### POST /questions

- General:
  - Creates a new question using the question text, answer, category, difficulty, and rating. Returns the id of the created question, success value, total questions, and questions list based on current page number to update the frontend.
- `curl http://127.0.0.1:5000/questions?page=2 -X POST -H "Content-Type: application/json" -d '{"question":"What is the capital of Egypt?", "answer":"Cairo", "category":3, "difficulty":1, "rating":3}'`

```
{
  "created": 32,
  "questions": [
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?",
      "rating": 1
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?",
      "rating": 5
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?",
      "rating": 4
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?",
      "rating": 3
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?",
      "rating": 2
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?",
      "rating": 1
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?",
      "rating": 5
    },
    {
      "answer": "Cairo",
      "category": 3,
      "difficulty": 1,
      "id": 32,
      "question": "What is the capital of Egypt?",
      "rating": 3
    }
  ],
  "success": true,
  "total_questions": 18
}
```

#### POST /questions/search

- General:
  - Searches the questions by any phrase. Returns the a list of questions that only include that string within their question, success value, and total questions (the number of search results. The questions list based on current page number to update the frontend.
- `curl http://127.0.0.1:5000/questions/search?page=1 -X POST -H "Content-Type: application/json" -d '{"searchTerm":"title"}'`

```
{
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
      "rating": 3
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
      "rating": 4
    }
  ],
  "success": true,
  "total_questions": 2
}
```

#### GET /categories/{category_id}/questions

- General:
  - Returns a list of questions objects based on the given category, success value, an object of current category, and total number of questions belongs to that category.
  - Results of questions are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: `curl -X GET http://127.0.0.1:5000/categories/5/questions?page=1`

```
{
  "current_category": {
    "id": 6,
    "type": "Sports"
  },
  "questions": [
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?",
      "rating": 3
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?",
      "rating": 2
    }
  ],
  "success": true,
  "total_questions": 2
}
```

#### POST /quizzes

- General:
  - Returns a list of questions to play the quiz.
  - This endpoint takes category and previous question parameters and returns success value, a random question within the given category, if provided, and that is not one of the previous questions..
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions":[16], "quiz_category":{"id":2, "type":"Art"}}'`

```
{
  "question": {
    "answer": "One",
    "category": 2,
    "difficulty": 4,
    "id": 18,
    "question": "How many paintings did Van Gogh sell in his lifetime?",
    "rating": 5
  },
  "success": true
}
```

## Authors

- Frontend Part: Udacity Team
- Backend Part: Mahmoud Esmat

## Acknowledgements

Thanks a lot to all Udacity Team
