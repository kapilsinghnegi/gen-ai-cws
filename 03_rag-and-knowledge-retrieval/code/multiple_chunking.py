text = """
Our courses lasts for a year.
Students get access to all recorded classes.
Live classes happen from Monday to Friday.
Refund requests are accepted within 7 days of the purchase.
Students must complete all assignments before placement support starts.
Eligible students receive minimum 3 interview opportunities. 
"""

lines = text.strip().split('\n')
chunks = []

for i in range(0, len(lines), 2):
    chunk = " ".join(lines[i:i+2])
    chunks.append(chunk)

for index, chunk in enumerate(chunks, start=1):
    print(f"Chunk {index}: {chunk}")
