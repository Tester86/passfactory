import passgen as pg

a = pg.Password(2, "")
b = a.generate()

c = a.copy()
print("Stats: " + str(a.stats()))

print(a.test())