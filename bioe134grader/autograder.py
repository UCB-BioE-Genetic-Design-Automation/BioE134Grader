import types
# Import grader modules here
import TranslateGrader  # Example grader import

class BioE134Autograder:
    @staticmethod
    def grade(entity):
        # Determine the type of the entity and relay to the appropriate helper
        if isinstance(entity, type):
            return BioE134Autograder._handle_class(entity)
        elif isinstance(entity, types.FunctionType):
            return BioE134Autograder._handle_function(entity)
        elif isinstance(entity, object):
            return BioE134Autograder._handle_instance(entity)
        else:
            raise ValueError("Unsupported entity type")

    @staticmethod
    def _handle_class(cls):
        # Logic for handling classes
        grader_name = cls.__name__ + "Grader"
        return BioE134Autograder._run_script(grader_name)

    @staticmethod
    def _handle_function(func):
        # Logic for handling functions
        grader_name = func.__name__ + "Grader"
        return BioE134Autograder._run_script(grader_name)

    @staticmethod
    def _handle_instance(instance):
        # Logic for handling class instances
        grader_name = type(instance).__name__ + "Grader"
        return BioE134Autograder._run_script(grader_name)

    @staticmethod
    def _run_script(grader_name):
        # Logic to execute the grader based on its name
        graders = {
            'TranslateGrader': TranslateGrader,
            # Add more graders here as needed
        }

        grader = graders.get(grader_name)
        if grader and hasattr(grader, 'run'):
            return grader.run()
        else:
            return f"Grader script for '{grader_name}' not found."
