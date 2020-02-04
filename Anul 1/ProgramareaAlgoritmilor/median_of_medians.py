from pathlib import Path



def medianOfMedians(v):

        if len(v) < 5:
            v.sort()
            return v[len(v)//2]

        # spart in grupuri de max 5 elem
        groups = [ v[i:i+5] for i in range(0, len(v),5)]

        # sortat
        groups = [ sorted(group) for group in groups]

        # format lista noua cu medianele fiecarui grup
        medians = [group[len(group)//2] for group in groups]

        return medianOfMedians(medians)


v = [int(x) for x in Path("input.txt").read_text().split(' ')]
print(v)
print(medianOfMedians(v))