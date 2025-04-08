from termcolor import colored as tc

colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
text = "Welcome to Pedro's Portfolio!"

def main():
    for i, char in enumerate(text):
        color = colors[i % len(colors)] 
        print(tc(char, color), end="")
    print("\n", tc("""This portfolio is a menu project that includes a list of 6 projects that I am proud of, all of the projects come with a breif description. """, 'light_grey'), sep="\n")
          