n = int(input())
languages_all = set()
languages_any = set()

for i in range(n):
    m = int(input())
    languages_current = set()
    for x in range(m):
        language = input()
        languages_current.add(language)
    if not languages_all:
        languages_all = languages_current.copy()
    else:
        languages_all.intersection_update(languages_current)
    languages_any.update(languages_current)

languages_all = sorted(languages_all)
languages_any = sorted(languages_any)

print(len(languages_all))
for language in languages_all:
    print(language)
print(len(languages_any))
for language in languages_any:
    print(language)
