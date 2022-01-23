import re
import subprocess

def curl_api(url):
    cmd = f"curl {url}"
    pattern = "[a-z]{5}-[a-z]{5}"
    curl_output = subprocess.check_output(cmd, shell=True, text=True)
    re_result = re.match(pattern, curl_output)
    print(re_result)
    return re_result

def test_curl_api(url='unique.tensorturtle.com'):
    assert curl_api(url) is not None

if __name__ == "__main__":
    test_curl_api
