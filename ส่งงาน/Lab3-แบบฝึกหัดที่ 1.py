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

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items


# สร้าง Stack
stack = Stack()

# ให้ผู้ใช้ป้อนข้อมูลเอง
print("=== Push ข้อมูล 5 ตัว ===")
for i in range(5):
    value = input(f"ป้อนค่าที่ต้องการใส่ใน Stack (ครั้งที่ {i+1}): ")
    stack.push(value)

print("\nหลังจาก push ข้อมูล 5 ตัว: ", stack.display())

# ใช้ peek แสดงข้อมูลบนสุด
print("ข้อมูลบนสุดของ Stack (peek): ", stack.peek())

# Pop ข้อมูลออก 3 ตัว
print("\n=== Pop ข้อมูลออก 3 ตัว ===")
for i in range(3):
    removed = stack.pop()
    print(f"Pop ครั้งที่ {i+1}: {removed}")

print("\nหลังจาก pop ข้อมูลออก 3 ตัว: ", stack.display())
