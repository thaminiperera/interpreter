import silly

while True:
    text = input('silly >> ')
    result, error = silly.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)