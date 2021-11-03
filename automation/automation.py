import re


def check_exists(query):
    """
    Check if the query exists in the file existing-constacts.txt.

    Args:
        query (str): A string that might be a phone number or an email.

    Returns:
        bool: True if the query string exists in that file, and False otherwise.
    """
    with open('assets/existing-contacts.txt', 'r') as e:
        return query in e.read()


with open("assets/potential-contacts.txt", "r") as f:
    content = f.read()

phone_numbers = list(filter(lambda v: not check_exists(v), list(set([item[0] for item in re.findall(
    r"((\+?\d{1,3}\W)?(\(?(\d{3})?\)?(-|\s)?)?\d{3}\W?\d{4}(x\d+)?)", content)]))))

new_phone_numbers = []
for number in phone_numbers:
    number = re.sub(r"(\+1\W)|(001\W)", "", number)
    num = ''
    for n in number:
        if n == 'x' or len(num) >= 12:
            break
        elif n.isdigit():
            num += n
            if (len(num) == 3) or (len(num) == 7):
                num += "-"

    new_phone_numbers.append(num)

emails = sorted(list(set(list(filter(lambda v: not check_exists(v), [
                item[0] for item in re.findall(r"(\w+@(\w+[-]?)+\.(com|info|net|org|biz))", content)])))))
with open('phone_numbers.txt', 'a') as p:
    for num in sorted(new_phone_numbers):
        p.write(num + '\n')

with open('emails.txt', 'a') as e:
    for email in emails:
        e.write(email + '\n')


#print(re.sub(r"\w-", "@", "h-ello m- an"))
#phone_numbers = sorted(list(map(lambda num : ''.join([n if n.isdigit() else ""  for i,n in enumerate(re.sub(r"(\+1\W)|(001\W)","",num))]), phone_numbers)))
