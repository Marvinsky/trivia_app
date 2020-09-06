curl -X DELETE http://localhost:5000/questions/26

curl -X POST -H "Content-Type: application/json" -d '{"question": "First president of Peru?","answer": "San Martin","difficulty": 3,"category": 4}' http://localhost:5000/questions


curl -X POST -H "Content-Type: application/json" -d '{"searchTerm": "title"}' http://localhost:5000/questions

curl -X GET http://localhost:5000/categories/4/questions

curl -X POST -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"id": 1, "type": "Science"}}' http://localhost:5000/quizzes
