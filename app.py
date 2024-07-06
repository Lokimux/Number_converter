import streamlit as st

def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(decimal):
    return bin(int(decimal))[2:]

def binary_to_hexadecimal(binary):
    return hex(int(binary, 2))[2:]

def hexadecimal_to_binary(hexadecimal):
    return bin(int(hexadecimal, 16))[2:]

def decimal_to_hexadecimal(decimal):
    return hex(int(decimal))[2:]

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def binary_to_octal(binary):
    return oct(int(binary, 2))[2:]

def octal_to_binary(octal):
    return bin(int(octal, 8))[2:]

def decimal_to_octal(decimal):
    return oct(int(decimal))[2:]

def octal_to_decimal(octal):
    return int(octal, 8)

def hexadecimal_to_octal(hexadecimal):
    return oct(int(hexadecimal, 16))[2:]

def octal_to_hexadecimal(octal):
    return hex(int(octal, 8))[2:]

st.title("Number Conversion Application")

conversion_type = st.selectbox("Choose conversion type", [
    "Binary to Decimal",
    "Decimal to Binary",
    "Binary to Hexadecimal",
    "Hexadecimal to Binary",
    "Decimal to Hexadecimal",
    "Hexadecimal to Decimal",
    "Binary to Octal",
    "Octal to Binary",
    "Decimal to Octal",
    "Octal to Decimal",
    "Hexadecimal to Octal",
    "Octal to Hexadecimal"
])

input_value = st.text_input("Enter the number to convert")

if st.button("Convert"):
    if conversion_type == "Binary to Decimal":
        result = binary_to_decimal(input_value)
    elif conversion_type == "Decimal to Binary":
        result = decimal_to_binary(input_value)
    elif conversion_type == "Binary to Hexadecimal":
        result = binary_to_hexadecimal(input_value)
    elif conversion_type == "Hexadecimal to Binary":
        result = hexadecimal_to_binary(input_value)
    elif conversion_type == "Decimal to Hexadecimal":
        result = decimal_to_hexadecimal(input_value)
    elif conversion_type == "Hexadecimal to Decimal":
        result = hexadecimal_to_decimal(input_value)
    elif conversion_type == "Binary to Octal":
        result = binary_to_octal(input_value)
    elif conversion_type == "Octal to Binary":
        result = octal_to_binary(input_value)
    elif conversion_type == "Decimal to Octal":
        result = decimal_to_octal(input_value)
    elif conversion_type == "Octal to Decimal":
        result = octal_to_decimal(input_value)
    elif conversion_type == "Hexadecimal to Octal":
        result = hexadecimal_to_octal(input_value)
    elif conversion_type == "Octal to Hexadecimal":
        result = octal_to_hexadecimal(input_value)
    
    st.write(f"Result: {result}")
