import json
import random

BOLD = '\033[1m'
UNDERLINE = '\033[4m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
MAGENTA = '\033[35m'
END = '\033[0m'


class Email_sender:
    def __init__(self, full_name):
        self.full_name = full_name

    def __str__(self):
        return '\u258DSender: {0}'.format(str(self.full_name))


class Email_theme:
    def __init__(self, theme=None):
        self.theme = theme

    def __str__(self):
        return '\u258DHeadline: {0}'.format(str(self.theme))


class Email_attachments:
    def __init__(self, attachments=None):
        self.attachments = attachments or []

    def __str__(self):
        return '\u258DAttachments: {0}'.format('Empty' if len(self.attachments) == 0 else str(self.attachments))


class Email_message:
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return '\u258DMessage: {}'.format(str(self.message))


class Email_status:
    def __init__(self, status):
        self.__status = status

    def get_value(self):
        return 1 if self.__status == 'Read' else 0

    def __str__(self):
        return 'Status: {}'.format(self.__status)


class Email_date:
    def __init__(self, date):
        self.__days = int(str(date).split('/')[0])
        self.__month = int(str(date).split('/')[1])
        self.__year = int(str(date).split('/')[2])

    def __cmp__(self, other):
        result = -1
        if self.__days == other.days() and self.__month == other.month() and self.__year == other.year():
            result = 0

        elif self.__days > other.days():
            if self.__month > other.month():
                if self.__year >= other.year():
                    result = 1
                else:
                    result = -1
            else:
                if self.__year > other.year():
                    result = 1
                else:
                    result = -1
        else:
            if self.__month > other.month():
                if self.__year >= other.year():
                    result = 1
                else:
                    result = -1
            else:
                if self.__year > other.year():
                    result = 1
                else:
                    result = -1

        return result

    def days(self):
        return self.__days

    def month(self):
        return self.__month

    def year(self):
        return self.__year

    def __str__(self):
        return '{0}{1}'.format(' ' * 7, '[{}/{}/{}]'.format(self.__days, self.__month, self.__year))


class Email:

    def __init__(self, sender, theme, attachments, message, date, status):
        self.__sender = sender
        self.__theme = theme
        self.__attachments = attachments
        self.__message = message
        self.__status = status
        self.__date = date

    def __str__(self):
        if self.__status.get_value() == 1:
            result = "{0}{1}{2}".format(CYAN, '{}\n{}\n{}\n{}\n{}'.format(str(self.__date), str(self.__sender),
                                                                          str(self.__theme),
                                                                          str(self.__attachments),
                                                                          str(self.__message)), END)
        else:
            result = "{0}{1}{2}".format(BOLD, MAGENTA,
                                        '{}\n{}\n{}\n{}\n{}'.format(str(self.__date), str(self.__sender),
                                                                    str(self.__theme),
                                                                    str(self.__attachments),
                                                                    str(self.__message)), END)
        return result

    def __cmp__(self, other):
        return self.__date.__cmp__(other.date())

    def show_status(self):
        return self.__status

    def get_key(self):
        return self.__date


class Email_builder:

    def __init__(self, sender=None, theme=None, attachments=None, message=None, status=None, date=None):
        self.__date = date
        self.__status = status
        self.__message = message
        self.__attachments = attachments
        self.__theme = theme
        self.__sender = sender

    def build_sender(self, sender):
        self.__sender = Email_sender(sender)

    def build_theme(self, theme):
        self.__theme = Email_theme(theme)

    def build_attachments(self, attachments):
        self.__attachments = Email_attachments(attachments)

    def build_message(self, message):
        self.__message = Email_message(message)

    def build_status(self, status):
        self.__status = Email_status(status)

    def build_date(self, date):
        self.__date = Email_date(date)

    def build_email(self):
        return Email(self.__sender, self.__theme, self.__attachments, self.__message, self.__date, self.__status)


class Email_chain:
    def __init__(self):
        self.__chain = []

    def add_to_chain(self, email):
        self.__chain.append(email)
        self.__chain = self.__sort(self.__chain)

    def __cmp__(self, other):
        return self.__chain[0].__cmp__(other.get_last_email)

    def __str__(self):
        chain = ''
        for i in range(len(self.__chain)):
            chain += ''.join('\n' + '  ' * i + k for k in str(self.__chain[i]).split('\n'))
        return chain

    def get_first_email(self):
        return self.__chain[0]

    def __sort(self, array):
        if len(array) < 2:
            return array
        result = []
        mid = int(len(array) / 2)
        left = self.__sort(array[:mid])
        right = self.__sort(array[mid:])
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i].get_key().__cmp__(right[j].get_key()) == 1:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result


class Email_spam:
    def __init__(self):
        self.__spam = []

    def add_email(self, chain):
        self.__spam.append(chain)
        self.__spam = self.__sort(self.__spam)

    def remove_email(self, chain):
        self.__spam.remove(chain)

    def __str__(self):
        return '{0}{1}SPAM:{2} {3}'.format(UNDERLINE, DARKCYAN, END, ''.join(str(k) for k in self.__spam))

    def __len__(self):
        return len(self.__spam)

    def __sort(self, array):
        if len(array) < 2:
            return array
        result = []
        mid = int(len(array) / 2)
        left = self.__sort(array[:mid])
        right = self.__sort(array[mid:])
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i].get_first_email().get_key().__cmp__(right[j].get_first_email().get_key()) == 1:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result


class Email_work:
    def __init__(self):
        self.__work = []

    def add_email(self, chain):
        self.__work.append(chain)
        self.__work = self.__sort(self.__work)

    def remove_email(self, chain):
        self.__work.remove(chain)

    def __sort(self, array):
        if len(array) < 2:
            return array
        result = []
        mid = int(len(array) / 2)
        left = self.__sort(array[:mid])
        right = self.__sort(array[mid:])
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i].get_first_email().get_key().__cmp__(right[j].get_first_email().get_key()) == 1:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def __str__(self):
        return '{0}{1}WORK:{2} {3}'.format(UNDERLINE, DARKCYAN, END, ''.join(str(k) for k in self.__work))

    def __len__(self):
        return len(self.__work)


class Email_duties:
    def __init__(self):
        self.__duties = []

    def add_email(self, chain):
        self.__duties.append(chain)
        self.__duties = self.__sort(self.__duties)

    def remove_email(self, chain):
        self.__duties.remove(chain)

    def __str__(self):
        return '{0}{1}DUTIES:{2} {3}'.format(UNDERLINE, DARKCYAN, END, ''.join(str(k) for k in self.__duties))

    def __len__(self):
        return len(self.__duties)

    def __sort(self, array):
        if len(array) < 2:
            return array
        result = []
        mid = int(len(array) / 2)
        left = self.__sort(array[mid:])
        right = self.__sort(array[:mid])
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i].get_first_email().get_key().__cmp__(right[j].get_first_email().get_key()) == 1:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result


class Inbox:
    def __init__(self):
        self.__spam = Email_spam()
        self.__duties = Email_work()
        self.__work = Email_duties()

    def add_to_spam(self, chain):
        self.__spam.add_email(chain)

    def add_to_duties(self, chain):
        self.__duties.add_email(chain)

    def add_to_work(self, chain):
        self.__work.add_email(chain)

    def __str__(self):
        return '{}\n\n{}\n\n{}'.format(self.__spam, self.__duties, self.__work)


class Inbox_builder:
    def __init__(self):
        self.__path = ''

    def set_path_to_json(self, path):
        self.__path = str(path)

    def build_inbox(self):
        inbox = Inbox()
        random_species = ['Spam', 'Work', 'Duties']
        builder = Email_builder()
        with open(self.__path) as f:
            json_data = json.load(f)
            for sender, theme, attach, message, date, status in zip(list(json_data['senders']),
                                                                    list(json_data['themes']),
                                                                    list(json_data['attachments']),
                                                                    list(json_data['messages']),
                                                                    list(json_data['dates']),
                                                                    list(json_data['status'])):
                builder.build_date(date)
                builder.build_message(message)
                builder.build_status(status)
                builder.build_attachments(attach)
                builder.build_theme(theme)
                builder.build_sender(sender)
                email = builder.build_email()
                chain = Email_chain()
                chain.add_to_chain(email)
                choice = random.choice(random_species)
                inbox.add_to_work(chain) if choice == 'Work' else inbox.add_to_duties(
                    chain) if choice == 'Duties' else inbox.add_to_spam(chain)
        return inbox


def main():
    builder = Inbox_builder()
    builder.set_path_to_json('/home/vestjevs/files/progs/Json/emails.json')
    inbox = builder.build_inbox()
    print(inbox)


if __name__ == '__main__':
    main()
