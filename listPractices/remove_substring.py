mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
new1=(mainStr.split())
index=0
while index<len(new1):
    if new1[index]=="over":
        del new1[index]
    index=index+1
print new1
print " ".join(new1)

new1=(mainStr.split())
a="over"
b="on"
i=0
while i<len(new1):
    if new1[i]==a:
        new1[i]=b
    i=i+1
print new1
print " ".join(new1)

