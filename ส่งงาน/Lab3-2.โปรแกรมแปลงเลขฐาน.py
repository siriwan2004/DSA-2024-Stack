class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

# ฟังก์ชันแปลงเลขฐาน 10 เป็นฐาน 2
def decimal_to_binary(decimal):
    stack = Stack()
    while decimal > 0:
        remainder = decimal % 2
        stack.push(remainder)
        decimal = decimal // 2
    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())
    return binary

# ฟังก์ชันแปลงเลขฐาน 10 เป็นฐาน 16
def decimal_to_hexadecimal(decimal):
    stack = Stack()
    hex_chars = "0123456789ABCDEF"
    while decimal > 0:
        remainder = decimal % 16
        stack.push(hex_chars[remainder])
        decimal = decimal // 16
    hexadecimal = ""
    while not stack.is_empty():
        hexadecimal += stack.pop()
    return hexadecimal

# รับค่าจากผู้ใช้งาน
decimal_number = int(input("กรุณากรอกเลขฐาน 10: "))

# แปลงเป็นฐาน 2 และฐาน 16
binary = decimal_to_binary(decimal_number)
hexadecimal = decimal_to_hexadecimal(decimal_number)

# แสดงผล
print(f"เลขฐาน 2: {binary}")
print(f"เลขฐาน 16: {hexadecimal}")
