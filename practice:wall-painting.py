print("Hey dude, how's it hangin braaa?")
print("Aw dawg you're doin' some wall paintin? Sick.")
print("What's the width of that wall? Is it THICC?")
width=float(input())
print("How tall is the wall? Is it crazy huge?")
height=float(input())
print("Aw man that's gotta be nasty expensive tho.\nHow much is a single can of paint?")
cost=float(input())
squarefeet=height*width
paintcans=squarefeet/400
finalCost=paintcans*cost
print("Wow so that's gonna cost ya $", finalCost, " for one coat. \nHow many coats are you putting on?")
coats=float(input())
coatsCost=finalCost*coats
print("That's gonna be $", coatsCost, " in total. \nThat's a lotta money for makin' your wall a different color.")
