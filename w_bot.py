import pywhatkit
from datetime import datetime, timedelta
import time
from InquirerPy import prompt, inquirer
import json

# use country code for phone number

# Opening JSON file
f = open("contacts.json")
# returns JSON object as  a dictionary
data = json.load(f)
contacts = data["contacts"]

choices = [contact["name"] for contact in contacts]  # ["evy", "diego"]


def get_send_immediately():
    print(datetime.now())
    # print(datetime.today())
    currentHour = datetime.now()
    delay = currentHour + timedelta(minutes=1)
    hour = int(delay.strftime("%H"))
    minutes = int(delay.strftime("%M").lstrip("0"))
    # minutes = delay[1:] if delay.startswith("0") else delay
    return hour, minutes


def get_send_scheduled():
    hour = int(input("Enter hour (24hs format)"))
    minutes = int(input("Enter minute"))
    return hour, minutes


def groupPrompt():
    questions = [
        {"type": "input", "message": "Enter the message:", "name": "message"},
        {
            "type": "list",
            "message": "Select a contact:",
            "choices": choices,
        },
        {"type": "confirm", "message": "Confirm?"},
    ]
    asnwers = prompt(questions)
    message = asnwers["message"]
    contact = asnwers[1]
    confirm = asnwers[2]
    return message, contact, confirm


def individualPrompt():
    message = inquirer.text(message="Enter the message:").execute()
    contact = inquirer.select(
        message="Select a contact:",
        choices=choices,
    ).execute()
    confirm = inquirer.confirm(message="Confirm?").execute()
    return message, contact, confirm


def send_message(phone, message, hour, minutes):
    try:
        pywhatkit.sendwhatmsg(phone, message, hour, minutes)
        print("!!!!!")
    except:
        print("fuck!")


def main():
    typeSend = inquirer.select(
        message="Select send type:",
        choices=["immediately", "scheduled"],
    ).execute()

    print(typeSend)

    asnwers = groupPrompt()  # returns tuple
    message = asnwers[0]
    contact_name_selected = asnwers[1]

    is_confirmed = asnwers[2]

    # for c in contacts:
    #     if c["name"] == contact_name_selected:
    #         contact_number = c["number"]
    #         break
    # else:
    #     contact_number = None
    # print(contact_number)

    contact_number_selected = next(
        (c["number"] for c in contacts if c["name"] == contact_name_selected), None
    )
    print(
        f"Message: {message}\nContact_name_selected: {contact_name_selected}\nIs_confirmed: {is_confirmed}\nContact_number_selected: {contact_number_selected}"
    )

    if message and is_confirmed:
        if typeSend == "immediately":
            when = get_send_immediately()
        else:
            when = get_send_scheduled()
        print(when)
        send_message(contact_number_selected, message, when[0], when[1])
    else:
        print("Nothing to send.")


if __name__ == "__main__":
    main()
