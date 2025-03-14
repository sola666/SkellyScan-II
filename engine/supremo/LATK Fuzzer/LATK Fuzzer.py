import wfuzz
for r in wfuzz.get_payload(range(100)).fuzz(hl=[97], url="http://angola-saiago.net/index.html"):
    print(r)