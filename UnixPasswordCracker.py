import argparse
import crypt


class UnixPwdCrack:
    def __init__(self):
        # Parsing Shadow file
        open_shadow = open('shadow.txt', 'r')
        self.shadow_file = {}
        for line in open_shadow:
            comps = line.split(":")
            self.shadow_file[comps[0]] = comps[1]

    def parse_password(self, args):
        # Parsing password for the asked username
        if args.username in self.shadow_file:
            password = self.shadow_file[args.username].split('$')
            if password[1] == '*' or password[1] == 'x' or password[1] == '!':
                print('No password found')
                exit(0)
            wordlist = open(args.wordlist, 'r')
            for word in wordlist:
                cryptpass = crypt.crypt(word, f"${password[1]}${password[2]}$")
                if cryptpass == self.shadow_file[args.username]:
                    print(f"Password Found: {word}")
                    exit(0)
        else:
            print("The requested username was not found in the system. Please try another username !!")
            exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This tool helps in cracking Unix Passwords. '
                                                 'Do note to run this tool you need to be a root user because shadow '
                                                 'file cannot be accessed from a normal user')
    parser.add_argument('-u', '--username', dest='user', help='Enter the username to crack')
    parser.add_argument('-w', '--wordlist', help='Enter the wordlist file name')

    args = parser.parse_args()

    cracker = UnixPwdCrack()
    cracker.crack(args)
