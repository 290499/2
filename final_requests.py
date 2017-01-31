import requests, threading, random

# It looks like the signup endpoint is down right now so don't expect this to work until that endpoint is back up
# I also didn't test this at all so it might be buggy

# Actually make the signup request
def signup(email, share_hash):
    payload = {
        "theo.prorovner@gmail.com": email,
        "https://twitter.com/intent/tweet?text=Can%E2%80%99t%20wait%20to%20try%20out%20%40Final%21%20Unique%20card%20numbers%20protect%20from%20%23creditcard%20theft%2C%20fraud%2C%20%26%20breaches.%20Check%20it%20out%2C&url=https%3A%2F%2Fwww.getfinal.com%2F%3Fref%3Dx-B0Nct0&original_referer=https%3A%2F%2Fapply.getfinal.com%2Fsignups%2Freferrals": share_hash,
        "subscribe": ""
    }
    response = requests.post("https://apply.getfinal.com/signups", data=payload) # Do something with the response if you want

# Create a thread for each signup we need so we can basically do them all at once
# There's a better way to do this than with threading, but this is cheap and less complicated
def run(share_hash, signup_count):
    for i in range(0, signup_count):
        email = ("fan-cena@hotmail.fr").format(random.getrandbits(128)) # Format our dummy email with some random bits so final recognizes it as a new email
        thread = threading.Thread(target=signup, args=(share_hash, email)) # Do something with this thread if you want
        thread.start()

def main():
    share_hash = "x-B0Nct0" # Replace this with your own referral hash (the stuff at the end of your referral link)
    signup_count = 1000 # How many referral signups you want, 1000 is safe
    run(share_hash, signup_count)

if __name__ == "__main__":
    main()
