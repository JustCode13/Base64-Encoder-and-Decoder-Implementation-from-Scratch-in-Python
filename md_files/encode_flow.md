Text → bytes → bits → 6-bit groups → Base64 chars → add `=` if needed.

---

### Quick flow with example (`"Hi"`)

```python
"Hi"
```

```python
b'Hi' = [72, 105]                    # raw_input.encode("utf-8")
```

```python
72  → 01001000
105 → 01101001                      # format(byte, "08b")
```

```python
0100100001101001                    # "".join(...)
→ 010010 000110 1001                # split into 6 bits
→ 010010 000110 100100              # last padded (ljust)
```

```python
[18, 6, 36]                         # int(group, 2)
→ "SGk"                             # Base64 map
→ "SGk="                            # padding added
```
