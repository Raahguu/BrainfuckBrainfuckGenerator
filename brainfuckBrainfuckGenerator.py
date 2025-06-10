setup_code="""+++++++[>++++++<-]>+>>+++++++[<++++++>-]<+++>>
++++++++[<++++++>-]<-->>++++++++[<++++++++>-]<-->>
++++++++[<++++++++>-]<---->>++++++++++[<+++++++++>-]<+>>
++++++++++[<+++++++++>-]<+++>++++++++++<<<<<<<<"""

background_memory_array = [0, "+", "-", ".", ">", "<", "[", "]", "\n"]
cursor_index = 0
allowed_characters = "+-.><[]\n"

print("Input your Brainfuck:")
original_brainfuck = ""
while True:
    inp = input()
    if inp.strip() == "": break
    original_brainfuck += inp  + "\n"

original_brainfuck = original_brainfuck[:-1]

#Remove unnecessary characters
sanitised_brainfuck = "".join([char if char in allowed_characters else "" for char in list(original_brainfuck)])

new_code = ""
#Create the basic code
for char in sanitised_brainfuck:
    offset = background_memory_array.index(char) - cursor_index
    while offset > 0:
        new_code += ">"
        offset -= 1
        cursor_index += 1
    while offset < 0:
        new_code += "<"
        offset += 1
        cursor_index -= 1
    new_code += "."

#Add loops, so it istn't just arrows and dots
repeat_count = 0
max_repeat_count = 4
offset = 0
char_diff = 0
for i, char in enumerate(new_code):
    if char == ".":
        repeat_count += 1
        continue
    old_offset = offset
    if char == ">": offset += 1
    elif char == "<": offset -= 1
    if repeat_count <= max_repeat_count:
        repeat_count = 0
        continue
    insertion = "<" * old_offset + "+" * (int(repeat_count ** 0.5)) + "[" + ">" * old_offset + "." * int(repeat_count ** 0.5) + "<" * old_offset + "-]" + ">" * old_offset \
              + "." * (repeat_count - int(repeat_count ** 0.5) * int(repeat_count ** 0.5))
    replaced_code = new_code[i-repeat_count:i]
    new_code = new_code[:i-repeat_count + char_diff] + insertion + new_code[i + char_diff:]
    char_diff += len(insertion) - len(replaced_code)
    repeat_count = 0

#Get rid of useless '><' and '<>' occurences
old_code = ""
while new_code != old_code:
    old_code = new_code
    new_code = new_code.replace("<>", "")
    new_code = new_code.replace("><", "")

#Wraps text lines to a cap
char_count_to_new_line = 50
for i in range(1, len(new_code)//char_count_to_new_line + 1):
    new_code = new_code[:i * char_count_to_new_line] + "\n" + new_code[i * char_count_to_new_line:]

print(f"The new brainfuck code: \n{setup_code}\n{new_code}")