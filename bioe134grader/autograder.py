
""" Autograder module for BioE134Grader package. """

class BioE134Autograder:
    @staticmethod
    def grade(translate_class):
        # Instantiate the Translate class
        translate_instance = translate_class()
        translate_instance.initiate()

        # DNA sequences to test
        test_sequences = [
            'ATGCGTAA',  # Invalid, not multiple of 3
            'ATGCGT',    # Valid
            'ATBXYZ',    # Invalid characters
            'ATGCGTAAA'  # Valid, with stop codon
        ]

        # Test the 'run' method
        for seq in test_sequences:
            try:
                result = translate_instance.run(seq)
                if len(seq) % 3 == 0 and all(c in 'ATCG' for c in seq):
                    # Valid test, should not raise an error
                    assert result is not None, f"Failed on valid input: {seq}"
                else:
                    # Invalid test, should raise an error
                    assert result is None, f"Error not raised for invalid input: {seq}"
            except Exception as e:
                return f"Error occurred with sequence '{seq}': {str(e)}"
        return "All tests passed successfully!"
