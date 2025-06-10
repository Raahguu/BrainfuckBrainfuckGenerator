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

char_count_to_new_line = 50
for i in range(1, len(new_code)//char_count_to_new_line + 1):
    new_code = new_code[:i * char_count_to_new_line] + "\n" + new_code[i * char_count_to_new_line:]

print(f"The new brainfuck code: \n{setup_code}\n{new_code}")