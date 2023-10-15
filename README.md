# Type Faster

## Overview

The "Type Faster" project is a simple Python script that automates typing on the Human Benchmark typing test available at https://humanbenchmark.com/tests/typing. It uses the Selenium and PyAutoGUI libraries to retrieve the test content and simulate typing, allowing you to test your typing speed effortlessly.

## Dependencies

Before you can run the script, you need to install the required dependencies. You can install them using pip:

```bash
pip install selenium beautifulsoup4 pyautogui
```

Make sure you also have the Chrome WebDriver installed. You can download it from [here](https://sites.google.com/chromium.org/driver/).

## Usage

1. Clone the repository or download the script to your local machine.

2. Ensure you have the required dependencies installed as mentioned in the "Dependencies" section.

3. Open the script (typically named `type_faster.py`) in a text editor of your choice.

4. Modify the script if needed. You may want to adjust the URL or customize the timing.

5. Run the script using Python:

```bash
python type_faster.py
```

6. The script will open a Chrome browser, load the typing test, retrieve the text to type, and simulate typing it. It will wait for 400,000 seconds (approximately 4.6 days) by default, which can be adjusted in the script.

7. After running the script, sit back and watch it type the text for you. It will measure your typing speed automatically.

## Customization

You can customize the script by modifying the following parameters:

- `url`: Change this variable to the URL of the typing test you want to automate.
- `time.sleep()`: Adjust the sleep duration to control the time the script waits before simulating typing.
- `time.sleep(400000)`: Change this line to adjust the duration of the typing test. By default, it waits for 400,000 seconds, but you can set it to any desired duration.

## Disclaimer

Please note that automating online tests or websites without permission may violate the terms of service of the website and may be considered unethical or even illegal in some cases. Ensure you have the appropriate permissions before using this script, and use it responsibly.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it for your needs, but be responsible and respectful of others' work and terms of service.
