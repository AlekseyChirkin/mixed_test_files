# 1 of beer on the wall,
# 1 of beer!
# Take one down.
# Pass it around.
# 1 bottle of beer on the wall.
# No more bottle of beer on the wall!
bott = 'bottles'

for i in range(99, 0, -1):
    if i == 1:
        bott = 'bottle'
    print(f"{i} {bott} of beer on the wall.")
    print(f"{i} {bott} of beer!")
    print("Take one down.\nPass it around!\n")
print("No more bottle of beer on the wall!")
