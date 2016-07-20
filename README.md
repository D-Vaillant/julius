# julius
A toy Vigenere cryptography package.

Most functionality is provided through argparser.

> cat plaintext.txt
This is the text.
> python -m julius/setup.py plaintext.txt a
thisisthetext
> python -m julius/setup.py plaintext.txt a --unsafe
This is the text.
> python -m julius/setup.py plaintext a
plaintext
>python -m julius/setup.py plaintext ab
pmajnueyt
