
library = {'red rising': 'a cool book about social classes', 'mask of shadows': 'A book by tbd about a theif that finds a flyer for auditions to be the queens assasin, called the left hand. When he leaves his old life behind, he finds his new one much more dangerous and threatening.', 'devastation': 'by tbd explanation tbd', 'maniac magee': 'a kid who runs away and best book ever', 'harry potter': 'fun', 'diary of a wimpy kid': 'a wimpy dude that goes to school with Rowley'}
amount = {'red rising': 1, 'funjungle': 1, 'mask of shadows': 1, 'devastation': 1, 'maniac magee': 1, 'harry potter': 0, 'diary of a wimpy kid': 1}
  
#my library of books by title then author 






book = input('Type in the title of the book')
book = book.lower()
#enter name of book, new addition, delete a book, or change a book explanation






#for changing an explanation
def change(key_to_find, definition):
    for key in library.keys():
        if key == key_to_find:
           library[key] = definition








if book[0:3] == 'add':
    library[book[4:100]] = input('what is the description of this book')
    amount[book[4:100]] = 1
elif book[0:6] in 'delete':
    del(library[book[7:100]])
    print(book[7:100], 'has been deleted')
elif book[0:6] in 'change':
    change(book[7:100], input('what do you want the new description to be'))
elif book in library:
    print(library[book])
    checkout = input('would you like to check out this book')
    if checkout == 'yes':
        amount[book] -= 1
    elif checkout == 'no':
        if input('would you like to return this book') == 'yes':
            amount[book] += 1
    else:
        print('have a great day!')
else:
    print('Cole does not own that book, or you messed up')
   





#save library
content = []
with open(__file__,"r") as f:
    for line in f:
        content.append(line)
 

with open(__file__,"w") as f:
    content[1] = "library = {n}\n".format(n=library)
    content[2] = "amount = {n}\n".format(n=amount)
    for i in range(len(content)):
        f.write(content[i])
         








library_file = open('my_books.txt', 'w')
print (library, file=library_file)
print (amount, file=library_file)
library_file.close()
