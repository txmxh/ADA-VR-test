import time
import numpy as np
import msvcrt
def input_password(prompt):
    print(prompt, end='', flush=True)
    chars = []
    timings = []
    prev_time = None
    while True:
        ch = msvcrt.getch()
        if ch in [b'\r', b'\n']:  # Enter key
            print()
            break
        elif ch == b'\x08':  # Backspace
            if chars:
                chars.pop()
                if timings:
                    timings.pop()
                print('\b \b', end='', flush=True)
            continue
        else:
            try:
                char = ch.decode('utf-8')
            except:
                continue
            print(char, end='', flush=True)  # <-- Show the character itself
            chars.append(char)
            now = time.time()
            if prev_time is not None:
                timings.append(now - prev_time)
            prev_time = now
    return ''.join(chars), timings
def enrollment_phase():
    enrolled_timings = []
    password_ref = None
    print("Enter your password for enrollment (5 attempts):")
    for i in range(5):
        while True:
            password, timings = input_password(f"Attempt {i+1}: ")
            if password_ref is None:
                password_ref = password
            if password != password_ref:
                print("Passwords do not match. Please re-enter this attempt.")
                continue
            if len(timings) == 0:
                print("Password too short. Try again.")
                continue
            enrolled_timings.append(timings)
            break
    avg_timings = np.mean(enrolled_timings, axis=0)
    print("\nAverage inter-key timing pattern per user:\n", avg_timings)
    return password_ref, avg_timings
def verify_login(password_ref, avg_timings, threshold=0.5):
    print("\n(login phase)")
    password, timings = input_password("Enter your password: ")
    if password != password_ref:
        print("Access denied! (incorrect password)")
        return
    if len(timings) != len(avg_timings):
        print("Access denied! (timing pattern mismatch)")
        return
    distance = np.linalg.norm(np.array(timings) - np.array(avg_timings))
    print(f"Euclidean distance from average timing vector: {distance:.5f}")
    if distance < threshold:
        print("Access granted!")
    else:
        print("Access denied!")
if __name__ == "__main__":
    password_ref, avg_timings = enrollment_phase()
    verify_login(password_ref, avg_timings)