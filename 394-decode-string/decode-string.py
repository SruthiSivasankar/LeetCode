class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_string = ""
        
        for char in s:
            if char.isdigit():
                # Build the current number (could be more than one digit)
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current number and string onto the stack
                stack.append((current_string, current_num))
                # Reset for the new segment
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop the last string and number
                last_string, num = stack.pop()
                # Repeat the current string num times and append to the last string
                current_string = last_string + current_string * num
            else:
                # It's a letter, append to the current string
                current_string += char
        
        return current_string

        