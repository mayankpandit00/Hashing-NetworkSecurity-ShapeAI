import hashlib

text = input("Enter the text to be hashed :  ")

hashed_text = hashlib.md5(text.encode())

print("---------------OUTPUT---------------")
print("Text: ", text)
print("Hashed Text: ", hashed_text.hexdigest())
