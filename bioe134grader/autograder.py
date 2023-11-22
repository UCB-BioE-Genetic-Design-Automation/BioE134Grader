import types
import importlib

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
        grader_script_name = cls.__name__ + "Grader"
        return BioE134Autograder._run_script(grader_script_name)

    @staticmethod
    def _handle_function(func):
        # Logic for handling functions
        grader_script_name = func.__name__ + "Grader"
        return BioE134Autograder._run_script(grader_script_name)

    @staticmethod
    def _handle_instance(instance):
        # Logic for handling class instances
        grader_script_name = type(instance).__name__ + "Grader"
        return BioE134Autograder._run_script(grader_script_name)

    @staticmethod
    def _run_script(grader_script_name):
        # Logic to import and run the grader script based on its name
        try:
            grader_module = importlib.import_module(grader_script_name)
            return grader_module.run()  # Assuming each grader script has a 'run' function
        except ImportError:
            return f"Grader script for '{grader_script_name}' not found."

