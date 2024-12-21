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

# ฟังก์ชันคำนวณ Postfix Expression
def evaluate_postfix(expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])
    
    # แยกสตริงที่ได้รับเป็นคำๆ และวนลูปแต่ละคำ
    for token in expression.split():
        if token in operators:
            try:
                # ถ้าเป็นตัวดำเนินการ, ดึง 2 ค่าออกมาจาก stack และคำนวณ
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    result = operand1 / operand2
                stack.push(result)
            except IndexError:
                return "Error: Invalid Postfix Expression"
        else:
            try:
                # ถ้าเป็นตัวเลข, นำไปใส่ใน stack
                stack.push(float(token))
            except ValueError:
                return "Error: Invalid input (not a number or operator)"
    
    # ผลลัพธ์สุดท้ายจะอยู่ใน stack
    if len(stack.items) == 1:  # แก้ไขตรงนี้
        return stack.pop()
    else:
        return "Error: Invalid Postfix Expression"

# รับค่า Postfix Expression จากผู้ใช้งาน
postfix_expression = input("กรุณากรอก Postfix Expression: ")

# คำนวณผลลัพธ์
result = evaluate_postfix(postfix_expression)

# แสดงผลลัพธ์
print(f"ผลลัพธ์ของนิพจน์ Postfix คือ: {result}")
