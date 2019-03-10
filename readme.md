# QuickText
## About
This project is designed to provide a quick and easy way to text larges numbers of club members stored in a csv file. Member names, emails, phone numbers, and other relevant details are parsed from a csv file, a text file with a custom message is read and filled with relevant data, before using Twilio's sms api service to text all imported members.

## Usage
```python index.py [csvfile] [textfile]```