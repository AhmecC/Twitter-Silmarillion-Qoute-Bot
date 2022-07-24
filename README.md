
**Description**
> This [bot](https://twitter.com/SilmarillionQo1) posts images with quotes from the J.R.R Tolkien book the Silmarillion every 3 hours.


**Updates**
> - 22/07/22 - Added functionality to like own tweets
> - 24/07/22 - Bot now creates images which display the quote on it

**Upcoming Updates**
> - Ability to like posts on feed


**Process**
> The file textConverter.py was obtained from [this thread](https://stackoverflow.com/questions/4576077/how-can-i-split-a-text-into-sentences) and with some changes it was used to split the Silmarillion into sentences. As i wanted a background image that was relevant to each chapter, i placed each chapter into its own folder along with a relevant image. The programme runs every 3 hours and chooses a random file and then a random quote from the selected chapter. Then the imageCreator places this text in a suitable fashion ontop of the background image. This is relayed back to the main programme which sends it off as a tweet. The programme also looks for currently relevant characters in the text and creates hashtags to boost engagement and can like its own tweets. It is running 24/7 on replit
