text = """
Our courses lasts for a year.
Live classes happen from Monday to Friday.
Students get access to all recorded classes.
Refund requests are accepted within 7 days of the purchase.
Students must complete all assignments before placement support starts.
Eligible students receive minimum 3 interview opportunities. 
"""

chunks = text.strip().split('\n')

for index, chunk in enumerate(chunks, start=1):
    print(f"Chunk {index}: {chunk}")