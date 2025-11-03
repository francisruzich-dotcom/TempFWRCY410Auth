# Authentication Module Development Progress

## Project Initialization
- Initialized a new Git repository and linked it to `https://github.com/francisruzich-dotcom/TempFWRCY410Auth.git`.
- Created an initial empty commit and pushed it to the remote repository.

## Authentication Module Implementation
- **Backend:** Python.
- **User Database:** Each user's data is stored in a separate JSON file within the `users/` directory.
- **Security:** Passwords are salted and hashed using cryptographically secure SHA-256.
- **Interface:** Command-line interface (CLI) with two options:
    - `create <username> <name> <password>`: To create a new user.
    - `login <username> <password>`: To authenticate an existing user.
- **User Attributes:** Each user has a `username`, `name`, and `password`.

## Unit Testing and Refactoring
- Added a comprehensive suite of unit tests using Python's `unittest` framework.
- **Security Testing:** The tests specifically cover:
    - Vague error messages for login to prevent username enumeration.
    - Correctness of the password hashing and salting mechanism.
    - Enforcement of unique usernames.
- **Code Refactoring:** The application was refactored to improve modularity and testability by removing global variables and using function arguments for dependencies.

## Web Application Development
- **Backend (Flask Server):**
    - Implemented a Flask server (`server.py`) to expose authentication functionalities (`create_user`, `login`) via RESTful API endpoints (`/api/create_user`, `/api/login`).
    - Refactored `app.py` functions to return boolean status for seamless integration with the Flask server.
- **Frontend (HTML/JavaScript):**
    - Developed a basic web interface (`index.html`, `profile.html`) using HTML and JavaScript.
    - `index.html` provides forms for user creation and login.
    - `profile.html` serves as a landing page after successful login.
    - Enhanced frontend aesthetics and user experience by integrating Bootstrap CSS.
    - Implemented client-side JavaScript to handle form submissions, make asynchronous API calls to the Flask backend, and manage page navigation.

## Current Status
- The authentication module has been fully implemented and tested.
- All unit tests are passing.
- The web application (Flask server and frontend) is set up and functional.
- All changes, including the new web application components and `.gitignore` for `__pycache__`, have been committed and pushed to the remote Git repository.
