import random

def generate_private_key(p):
    return random.randint(2, p-2)

def calculate_public_key(g, private_key, p):
    return pow(g, private_key, p)

def calculate_shared_secret(public_key, private_key, p):
    return pow(public_key, private_key, p)


p = 23 
g = 5   


private_key_A = generate_private_key(p)
private_key_B = generate_private_key(p)

public_key_A = calculate_public_key(g, private_key_A, p)
public_key_B = calculate_public_key(g, private_key_B, p)

shared_secret_A = calculate_shared_secret(public_key_B, private_key_A, p)
shared_secret_B = calculate_shared_secret(public_key_A, private_key_B, p)


assert shared_secret_A == shared_secret_B

print(f"Shared Secret: {shared_secret_A}")
