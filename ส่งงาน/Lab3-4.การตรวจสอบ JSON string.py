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

# ฟังก์ชันตรวจสอบความถูกต้องของ JSON string
def is_valid_json(json_str):
    stack = Stack()
    valid_opening = {'{', '['}  # วงเล็บเปิดที่ถูกต้อง
    valid_closing = {'}': '{', ']': '['}  # วงเล็บปิดที่ต้องตรงกับวงเล็บเปิด

    # วนลูปตรวจสอบทีละตัวอักษรใน JSON string
    for char in json_str:
        if char in valid_opening:
            # ถ้าเป็นวงเล็บเปิด, เพิ่มลงใน stack
            stack.push(char)
        elif char in valid_closing:
            # ถ้าเป็นวงเล็บปิด, ตรวจสอบว่า Stack มีวงเล็บเปิดที่ตรงกันหรือไม่
            if stack.is_empty() or stack.pop() != valid_closing[char]:
                return False

    # ตรวจสอบว่า Stack ว่างเปล่าหรือไม่ (ถ้ามีวงเล็บเปิดที่ไม่ได้ปิด, Stack จะไม่ว่าง)
    return stack.is_empty()

# รับค่า JSON string จากผู้ใช้งาน
json_string = input("กรุณากรอก JSON string: ")

# ตรวจสอบความถูกต้องของ JSON string
if is_valid_json(json_string):
    print("JSON string ถูกต้อง")
else:
    print("JSON string ไม่ถูกต้อง")
