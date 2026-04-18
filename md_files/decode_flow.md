Base64 → chars → numbers → bits → bytes → text

---

### Quick flow with example (`"SGk="`)

```python
"SGk="
```

```python
['S','G','k','=']                  # read chars
→ [18, 6, 36]                      # map to numbers (ignore '=')
```

```python
18 → 010010
6  → 000110
36 → 100100                        # format(value, "06b")
```

```python
010010000110100100
→ remove padded bits → 0100100001101001
→ 01001000 01101001                # split into 8 bits
```

```python
[72, 105]                          # int(byte, 2)
→ b'Hi'
→ "Hi"                             # bytes.decode("utf-8")
```

0 * 2 = 0
1 * 2 = 2
2 * 2 = 4