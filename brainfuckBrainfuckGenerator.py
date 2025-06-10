setup_code="""+++++++[>++++++<-]>+>>
+++++++[<++++++>-]<+++>>
++++++++[<++++++>-]<-->>
++++++++[<++++++++>-]<-->>
++++++++[<++++++++>-]<---->>
++++++++++[<+++++++++>-]<+>>
++++++++++[<+++++++++>-]<+++<<<<<<<"""

background_memory_array = [0, "+", "-", ".", ">", "<", "[", "]"]
cursor_index = 0
allowed_characters = "+-.><[]"

original_brainfuck = input("Input your Brainfuck: \n")

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

print(f"The new brainfuck code: \n{setup_code}\n{new_code}")