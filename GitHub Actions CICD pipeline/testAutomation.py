import requests

testcases = [
    {"url": "http://localhost:8000/add/2/2", "expected": 4, "description": "Test addition of 2 and 2"},
    {"url": "http://localhost:8000/subtract/5/3", "expected": 2, "description": "Test subtraction of 5 from 3"},
    {"url": "http://localhost:8000/multiply/2/3", "expected": 6, "description": "Test multiplication of 2 and 3"}
]

def test():
    for case in testcases:
        response = requests.get(case["url"])
        result = response.json()["result"]
        assert result == case["expected"], f"Test failed: {case['description']}. Expected {case['expected']}, got {result}"
        print(f"Test passed: {case['description']}")

    print("All tests passed!")

test()
