# TranslateGrader.py

class TranslateGrader:
    @staticmethod
    def grade(translate_class):
        translate_instance = translate_class()
        translate_instance.initiate()

        test_sequences = [
            'ATGCGTAA',  # Invalid, not multiple of 3
            'ATGCGT',    # Valid
            'ATBXYZ',    # Invalid characters
            'ATGCGTAAA'  # Valid, with stop codon
        ]

        for seq in test_sequences:
            try:
                result = translate_instance.run(seq)
                if len(seq) % 3 == 0 and all(c in 'ATCG' for c in seq):
                    assert result is not None, f"Failed on valid input: {seq}"
                else:
                    assert result is None, f"Error not raised for invalid input: {seq}"
            except Exception as e:
                return f"Error occurred with sequence '{seq}': {str(e)}"
        return "All tests passed successfully!"
