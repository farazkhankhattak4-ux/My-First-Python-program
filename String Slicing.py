text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(":")          # find where the colon lives
num_str = text[pos+1:]        # slice everything after the colon
num_str = num_str.strip()     # remove the extra spaces

value = float(num_str)        # convert to float
print(value)