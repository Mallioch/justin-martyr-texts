# justin-martyr-texts

Digitized and edited edition of Justin Martyr's writings as a [part of the greek-texts group](https://github.com/jtauber/greek-texts).

The base text for the two apologies is from [Gerardus Rauschen's *S. Iustini Apologiae Duae* (1911)](https://archive.org/details/siustiniapologia00just).

## Validation

Assuming you have text validator installed, this should validate the file according to the rules:

`validate-text text-validator.toml texts/1-apology.txt`

Also, you can convert a whole file to NFC by running this.

`python3 convert-to-nfc.py 1-apology.txt > texts/1-apology-output.txt`