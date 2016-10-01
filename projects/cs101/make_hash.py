def make_hash(nbuckets):
  i = 0
  table = []
  while i < nbuckets:
    table.append([])
    i = i + 1
  return table

print make_hash(3)
