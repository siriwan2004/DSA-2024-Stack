class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0


# ฟังก์ชันสำหรับกลับลำดับตัวอักษรโดยใช้ Stack
def reverse_string(input_string):
    stack = Stack()

    # ใส่ตัวอักษรทั้งหมดลงใน Stack
    for char in input_string:
        stack.push(char)

    # ดึงตัวอักษรออกจาก Stack และสร้างข้อความใหม่
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


# รับข้อความจากผู้ใช้
user_input = input("ป้อนข้อความที่ต้องการกลับลำดับตัวอักษร: ")
result = reverse_string(user_input)

# แสดงผลลัพธ์
print("ข้อความที่กลับลำดับตัวอักษร: ", result)
