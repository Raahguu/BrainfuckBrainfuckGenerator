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
