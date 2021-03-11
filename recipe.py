from tkinter import *
import webbrowser
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

master = Tk()
master.geometry('400x410')
master.title("Recipe Finder")

title = Label(master, text="VisionRecipe", font=("Lato", 35)).grid(row=0, column=1, padx=50, pady=25)
Label(master, text="Enter Image URL").grid(row=2, column=1, pady=50)
Label(master, text="Enter a picture of food, we give you a recipe!").grid(row=10, column=1)

e1 = Entry(master)
e1.insert(0, "Image URL")

e1.grid(row=2, column=1)

Button(master, text='Submit', command=master.quit).grid(row=11, column=1, sticky=W, pady=50, padx=200)

mainloop( )

app = ClarifaiApp(api_key='d43b260a30fd49768460baae0bdeb13f')

model = app.models.get('food-items-v1.0')
model2 = app.models.get('chinese-food')
image = ClImage(url=e1.get())
master.destroy()

printModel = model.predict([image])
printModel2 = model2.predict([image])
topValue = str(printModel)
topValue2 = str(printModel2)
print (topValue)
print (topValue2)

n = "0.999999"
n2 = "0.999999"

foundN = False
foundN2 = False

while foundN == False:

    if n in topValue:
      foundN = True
    else:
      n = float(n) - 0.000001
      n = "%.6f" % n
      print (n)
      n = str(n)

while foundN2 == False:

    if n2 in topValue2:
      foundN2 = True
    else:
      n2 = float(n2) - 0.000001
      if float(n2) < 0.50:
      	break
      n2 = "%.6f" % n2
      print (n2)
      n2 = str(n2)

if float(n) >= 0.92:

  charN = topValue.find(n) - 13
  
  word = topValue[charN]
  
  while topValue[charN - 1] != "'":
    charN = charN - 1
    word = word + str(topValue[charN])
  
  word = word[::-1]

  if float(n) >= float(n2):

    url = "http://allrecipes.com/search/results/?wt=" + word + "&sort=re"
  
    webbrowser.open_new_tab(url)

else:

  print("That is probably not edible")

  
if float(n2) >= 0.50:

  charN2 = topValue2.find(n2) - 13
  
  word2 = topValue2[charN2]
  
  while topValue2[charN2 - 1] != "'":
    charN2 = charN2 - 1
    word2 = word2 + str(topValue2[charN2])
  
  word2 = word2[::-1]

  if float(n2) > float(n):
  
    url2 = "http://allrecipes.com/search/results/?wt=" + word2 + "&sort=re"
  
    webbrowser.open_new_tab(url2)

elif float(n2) < 0.50 and float(n) < 0.92:

  print("That is probably not edible")

if float(n) >= 0.92:
	print (str(float(n) * 100) + ".........." + word.upper())

if float(n2) >= 0.50:
	print (str(float(n2) * 100) + ".........." + word2.upper())