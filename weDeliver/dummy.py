from weDeliver.models import User


v = User.objects.filter(email__exact='manthan')

for x in v:
    print(x)

