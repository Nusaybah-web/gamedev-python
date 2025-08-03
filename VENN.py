num={1,2,3,4,5,6,7,8,9,0,1,2,3}

print(num)

num.add(10)

print(num)

num.remove(0)

print(num)

num.discard(11)

print(num)

#to stop makeing changes

num=frozenset(num)

#setoperations

ops1={1,2,3,4,5,6}

ops2={5,6,7,8,9,0}

#unioun

print(ops1.union(ops2))

print(ops1|ops2)

#intersection

print(ops1.intersection(ops2))

print(ops1&ops2)

#diffrence

print(ops1.difference(ops2))

print(ops2-ops2)

#symmetricdiffrence

print(ops1.symmetric_difference(ops2))

print(ops1^ops2)
