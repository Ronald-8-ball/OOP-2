class employee:
    def __init__(self):
     print("I am employeed")
    def __del__(self):
     print("I am a destroyer")
obj = employee()
del obj