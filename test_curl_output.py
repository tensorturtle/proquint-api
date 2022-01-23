import re

def test_curl_output():
    with open('curl_output.txt', 'r') as f:
        output = f.readline()
    pattern = "[a-z]{5}-[a-z]{5}"
    re_result = re.match(pattern, output)
    print(re_result)
    assert re_result is not None

if __name__ == "__main__":
    test_curl_output()
