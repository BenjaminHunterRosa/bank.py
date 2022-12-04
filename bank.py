greeting = input("greeting: ")
greeting2 = []
for i in greeting:
   greeting2.append(i)
if "hello" in greeting.lower():
   print("hello: $0")
elif "h" in greeting2[0] or "H" in greeting2[0]:
   print("starts with `h`: $20")
else:
   print("not hello: $100 ")
