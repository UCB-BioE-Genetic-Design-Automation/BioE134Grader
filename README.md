
# BioE134Grader

BioE134Grader is an autograder library designed for easy integration in Google Colab notebooks. It allows students to grade their code by importing the library and invoking it directly within their notebooks.

## Installation

To install BioE134Grader, follow these steps:

1. **Upload to GitHub:**
   - Push this entire folder to a new GitHub repository.

2. **Installation in Google Colab:**
   - Use pip to install the library directly from GitHub:
     ```
     !pip install git+https://github.com/your-username/BioE134Grader.git
     ```

## Usage

1. **Import the Library:**
   - In your Google Colab notebook, import the BioE134Grader library:
     ```python
     from bioe134grader.autograder import BioE134Autograder
     ```

2. **Create the Translate Class:**
   - Implement the `Translate` class as specified, with `initiate` and `run` methods.

3. **Use the Autograder:**
   - Create an instance of your `Translate` class and pass it to the `grade` method of the `BioE134Autograder` class.
   - Example usage is provided in the `example_usage.ipynb` notebook.

## Example

Refer to the `example_usage.ipynb` in this repository for a detailed example of how to use the BioE134Grader in a Google Colab notebook.

---

*Note: Replace 'your-username' with your actual GitHub username in the installation command.*
