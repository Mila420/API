Exercise 3: Data Handling in APIs
This project includes two primary components:

1. Pets Data Retrieval (pets.py):

- Fetches data on sold pets from an API and processes it into a structured format (DataFrame).
- The data includes pet IDs and names.
  
2. Pet Name Counter (pet_counter.py):

- Utilizes the data fetched from the API to count occurrences of each pet name.
- Provides a summary of the most common pet names.

3. How to Run Tests
- Tests for these components are included in the test_exercise.py file.
- Execute the tests using the command:
pytest --html=report.html --self-contained-html

Open the generated report.html file in a web browser to view the detailed test results.
This setup ensures the data processing and counting functionalities are thoroughly tested and verified.
