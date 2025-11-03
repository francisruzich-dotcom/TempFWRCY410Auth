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

## Current Status
- The authentication module has been fully implemented and tested.
- All unit tests are passing.
- All changes have been committed and pushed to the remote Git repository.