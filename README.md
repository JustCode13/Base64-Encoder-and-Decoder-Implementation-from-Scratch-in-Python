# Base64 Encoder and Decoder Implementation from Scratch in Python

![Python](https://img.shields.io/badge/Python-100%25-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📋 Overview

A pure Python implementation of Base64 encoding and decoding built from first principles. This project processes text into bytes, converts to bit streams, groups into 6-bit values, and maps to Base64 characters with proper padding and validation. Perfect for learning how Base64 works under the hood!

## ✨ Key Features

- **From Scratch Implementation** - No reliance on Python's built-in `base64` module
- **Comprehensive Encoding/Decoding** - Full support for text and binary data
- **Proper Padding Handling** - Correct implementation of Base64 padding rules
- **Input Validation** - Error checking and validation for robust operation
- **Educational** - Well-documented code with detailed comments explaining the algorithm
- **Performance Efficient** - Optimized bit manipulation and character mapping
- **Pure Python** - No external dependencies required

## 📚 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [Algorithm Explanation](#algorithm-explanation)
- [API Reference](#api-reference)
- [Technical Details](#technical-details)
- [Performance Considerations](#performance-considerations)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/JustCode13/Base64-Encoder-and-Decoder-Implementation-from-Scratch-in-Python.git
cd Base64-Encoder-and-Decoder-Implementation-from-Scratch-in-Python
```

No additional dependencies required - this is pure Python!

## 🎯 Quick Start

```python
from base64_encoder_decoder import encode, decode

# Encoding text to Base64
text = "Hello, World!"
encoded = encode(text)
print(f"Encoded: {encoded}")
# Output: SGVsbG8sIFdvcmxkIQ==

# Decoding Base64 back to text
decoded = decode(encoded)
print(f"Decoded: {decoded}")
# Output: Hello, World!
```

## 📖 Usage Examples

### Basic String Encoding

```python
# Encode a simple string
message = "Python Base64"
encoded_message = encode(message)
print(encoded_message)  # UHl0aG9uIEJhc2U2NA==
```

### Binary Data Encoding

```python
# Encode binary data
binary_data = b"\x00\x01\x02\x03"
encoded_binary = encode(binary_data)
print(encoded_binary)  # AAECAA==
```

### Decoding Base64

```python
# Decode a Base64 string
base64_string = "UHl0aG9u"
decoded = decode(base64_string)
print(decoded)  # Python
```

### Error Handling

```python
try:
    invalid_base64 = decode("Invalid!!!")
except ValueError as e:
    print(f"Error: {e}")
```

## 🧮 Algorithm Explanation

### Encoding Process

The Base64 encoding algorithm works as follows:

1. **Convert to Bytes** - Transform input text into byte values
2. **Create Bit Stream** - Convert bytes to an 8-bit binary stream
3. **Group into 6-bit Chunks** - Divide the bit stream into 6-bit groups
4. **Pad if Necessary** - Add zeros to the right if the last group has fewer than 6 bits
5. **Map to Base64 Alphabet** - Convert each 6-bit value (0-63) to a Base64 character
6. **Add Padding** - Append `=` characters to maintain alignment to 4-character boundaries

### Base64 Character Set

```
A-Z (0-25) | a-z (26-51) | 0-9 (52-61) | + (62) | / (63) | = (padding)
```

### Example: Encoding "AB"

```
Input: "AB"
Bytes: [65, 66]
Binary: 01000001 01000010
6-bit groups: 010000 | 010100 | 0010 (padded: 001000)
Decimal: 16, 20, 8
Base64: Q, U, I
Padding: QUI=
```

## 🔧 API Reference

### `encode(data)`

Encodes input data to Base64 format.

**Parameters:**
- `data` (str or bytes): The data to encode

**Returns:**
- `str`: Base64 encoded string

**Example:**
```python
result = encode("Hello")
```

### `decode(data)`

Decodes Base64 encoded data back to original format.

**Parameters:**
- `data` (str): Base64 encoded string

**Returns:**
- `str`: Decoded data

**Raises:**
- `ValueError`: If invalid Base64 characters are found

**Example:**
```python
result = decode("SGVsbG8=")
```

## 🔬 Technical Details

### Bit Manipulation

The implementation uses Python's bitwise operators for efficient bit manipulation:
- `>>` - Right shift
- `<<` - Left shift
- `&` - Bitwise AND
- `|` - Bitwise OR

### Character Mapping

A lookup table (string or dictionary) maps 6-bit values to Base64 characters:

```python
BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
```

### Padding Rules

- Input length % 3 == 1 → Add 2 `=` characters
- Input length % 3 == 2 → Add 1 `=` character
- Input length % 3 == 0 → No padding needed

## ⚡ Performance Considerations

- **Time Complexity:** O(n) where n is the length of input data
- **Space Complexity:** O(n) for the output string
- **Optimization:** Uses lookup tables instead of calculations for character mapping
- **Scalability:** Handles large files efficiently without loading entire content into memory

## ✅ Testing

Run the included test suite:

```bash
python -m pytest tests/
```

Or test manually:

```python
from base64_encoder_decoder import encode, decode

# Test round-trip
original = "Test String 123"
encoded = encode(original)
decoded = decode(encoded)
assert decoded == original, "Round-trip encoding/decoding failed"
print("✓ All tests passed!")
```

### Test Cases

- Empty strings
- Single characters
- Long strings
- Special characters
- Binary data
- UTF-8 characters
- Padding variations

## 📚 Educational Value

This project is excellent for learning:

- **Bit Manipulation** - Understanding binary operations in Python
- **Algorithm Design** - Implementing complex algorithms from specifications
- **Data Encoding** - How data is transformed for transmission
- **Computer Science Fundamentals** - Number systems and character encoding
- **Python Programming** - Using Python's built-in functions and operators effectively

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code:
- Follows PEP 8 style guidelines
- Includes docstrings and comments
- Has corresponding test cases
- Maintains 100% Python compatibility

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**JustCode13**

- GitHub: [@JustCode13](https://github.com/JustCode13)

---

⭐ If you find this project helpful, please consider giving it a star!

**Happy Coding!**