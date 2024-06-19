# set = collection which is unordered, unindexed. no duplicate values

showroom1 = {"mustang","supra","dodge"}
showroom2 = {"bmw","supra","mercedes"}

# showroom1.add("astro martin")
# showroom2.remove("bmw")
# showroom1.clear()
# showroom1.update(showroom2)
# showrooms = showroom1.union(showroom2)
showrooms = showroom1.difference(showroom2)

for i in showrooms:
    print(i)