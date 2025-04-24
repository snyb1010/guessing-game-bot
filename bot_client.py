import socket

host = "127.0.0.1"
port = 7777

s = socket.socket()
s.connect((host, port))

data = s.recv(1024)
print(data.decode().strip())

# Set difficulty level (1: Easy, 2: Medium, 3: Hard)
difficulty = 2
s.sendall(f"{difficulty}\n".encode())

# Define range based on difficulty
if difficulty == 1:
    low, high = 1, 10
elif difficulty == 2:
    low, high = 1, 50
else:
    low, high = 1, 100

while True:
    guess = (low + high) // 2
    print(f"Bot guesses: {guess}")
    s.sendall(f"{guess}\n".encode())
    reply = s.recv(1024).decode().strip()
    print(reply)
    if "CORRECT!" in reply:
        break
    elif "Guess Lower" in reply:
        high = guess - 1
    elif "Guess Higher" in reply:
        low = guess + 1

s.close()
