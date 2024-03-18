## Schedule Whatsapp message

This script allows you write a message, select a contact and schedule the message using a simple prompt.
The contact list used comes from a simple contacts.json

Limitatons:

Requires Whatsapp web to works.
I's not recurring.

## Setup

### Virtual enviroment

Create the virtual enviroment for dependecies:

`python3 -m venv .venv`

`source .venv/bin/activate`

### Already created

`pip freeze > requirements.txt`

### Dependencies

`python3 -m pip install pywhatkit`

`python3 -m pip install InquirerPy`

or

`pip install -r requirements.txt`

## Contacts

Rename `contacts_example.json` by `contacts.json` and populate with your contacts.

## Use

`python3 w_bot.pyt`
