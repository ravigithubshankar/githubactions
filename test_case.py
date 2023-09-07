with open("test_cases.json", "r") as file:
    test_cases = json.load(file)

# Run test cases
for idx, test_case in enumerate(test_cases, start=1):
    input_data = test_case["input"]
    expected_output = test_case["expected_output"]

    # Run the function with the input data
    func(input_data)

    # Check if the result matches the expected output
    if input_data == expected_output:
        print(f"Test case {idx}: Passed")
    else:
        print(f"Test case {idx}: Failed")
