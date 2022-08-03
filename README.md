# **Description**
This [bot](https://twitter.com/SilmarillionQo1) posts images with quotes from the J.R.R Tolkien book the Silmarillion every 2 hours between 8am and 10pm


## **Updates**
> - 22/07/22 - Added functionality to like own tweets
> - 24/07/22 - Bot now creates images which display the quote on it
> - 30/07/22 - Improved text visibility by adding an opaque box around text
> - 31/07/22 - Now tweets every 2 hours from 8am-8pm


## ***The Process***
- First textConverty.py, which was obtained from [this thread](https://stackoverflow.com/questions/4576077/how-can-i-split-a-text-into-sentences), was used to split The Silmarillion into sentences
- As full stops inside Quotation Marks weren't caught by the programme, some sentences had to be manually formatted
- A folder was created for each chapter, containing a related image and text file with sentences from that chapter
- SilmarillionQoutes.py runs every 2 hours between 8am and 8pm and chooses a random quote and tweets it out
- It also looks for specific words in that quote that are made to be hashtags
- imageCreator.py creates the background image and places the quotes text onto the image using [this font](https://fonts.google.com/specimen/Courgette?query=courgette)
- The Code is ran on replit 24/7
