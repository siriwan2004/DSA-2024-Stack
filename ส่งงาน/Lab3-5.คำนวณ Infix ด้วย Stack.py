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

# ฟังก์ชันตรวจสอบลำดับการดำเนินการ
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

# ฟังก์ชันสำหรับคำนวณนิพจน์
def apply_operator(op, b, a):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b

# ฟังก์ชันสำหรับคำนวณ Infix Expression
def evaluate_infix(expression):
    values = Stack()  # Stack สำหรับเก็บตัวเลข
    operators = Stack()  # Stack สำหรับเก็บตัวดำเนินการ

    i = 0
    while i < len(expression):
        char = expression[i]

        if char == ' ':
            i += 1
            continue

        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.push(num)

        elif char == '(':
            operators.push(char)
            i += 1

        elif char == ')':
            while not operators.is_empty() and operators.peek() != '(':
                op = operators.pop()
                val2 = values.pop()
                val1 = values.pop()
                values.push(apply_operator(op, val2, val1))
            operators.pop()  # pop '('
            i += 1

        else:  # ตัวดำเนินการ
            while (not operators.is_empty() and precedence(operators.peek()) >= precedence(char)):
                op = operators.pop()
                val2 = values.pop()
                val1 = values.pop()
                values.push(apply_operator(op, val2, val1))
            operators.push(char)
            i += 1

    # คำนวณที่เหลือใน Stack
    while not operators.is_empty():
        op = operators.pop()
        val2 = values.pop()
        val1 = values.pop()
        values.push(apply_operator(op, val2, val1))

    return values.pop()

# รับค่า Infix Expression จากผู้ใช้งาน
infix_expression = input("กรุณากรอก Infix Expression: ")

# คำนวณผลลัพธ์
result = evaluate_infix(infix_expression)

# แสดงผลลัพธ์
print(f"ผลลัพธ์ของนิพจน์ Infix คือ: {result}")
