## Why does this repo exist?

I saw a [tweet](https://twitter.com/onPolygon_/status/1711035183682510921?s=20) in twitter made by Polygon and saw these binary strings and I was curius! so I thought that it was Unicodes of letters 

Repository made to cypher and de-cypher Unicode texts from and to different forms, it supports binary, regular integers and regular text

## API

This script probides simple functions to encode text to different forms with simple names

```python
# converts a regular utf-8 string to decimal from, dividing each character to it's ASCII representation
utf8_to_decimal(string) 

# does the same thing as the function before but in binary form, it gives de option to have spaces between charecters
utf8_to_binary(string, with_spaces: bool)

# etc ...
```

This script provides conversions from and to decimal, utf-8 (nomal strings) and binary

utf-8 <=> decimal <=> binary
