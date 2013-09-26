# Scraping Go Games from PDF's

> Go Classified: SGF of Cho’s Encyclopedia of Life and Death
> Sep 25, 2013 04:00 pm | Chris Garlock
> 
> 
> “I’d like to get the SGF for Cho’s Encyclopedia of Life and Death,” writes Merlyn. “Does anyone know about this? I’ve found the PDF online, and I do know that Kiseido used to sell it on a 3.5″ disk.”

As Merlyn promised, I found Cho Chikun's [Encyclopedia of Life and Death](http://tsumego.tasuki.org/books/cho-1-elementary.pdf) online it is large collection of Go problems in PDF.

I was able to copy paste the output and arrange it into a board:

    !(!(((((((((((((((> 
    @+!@@+++++++++++++] 
    !!+!@+++++++++++++] 
    @+!!@++++*+++++*++] 
    [@@@@+++++++++++++] 
    [+++++++++++++++++]

Each character corresponds to an intersection on the board.  We can decipher the code:

- `!` = white
- `@` = black
- `+` = empty
- `*` = star point
- `[` = left edge
- `]` = right edge
- `(` = top edge
- `<` = top right corner

The next steps in the workflow are scraping the games, writing the SGF files and place in an SGF reader and host.

## Scraperwiki

Google `scraping pdf python` I found that [School of Data](http://schoolofdata.org/), has a [tutorial for scraperwiki](http://schoolofdata.org/2013/08/16/scraping-pdfs-with-python-and-the-scraperwiki-module/).

    pip install scraperwiki

The scraperwiki library turned the PDF into quite regular XML.  In two lines I got the XML

    u=file("cho-1-elementary.pdf")
    x=scraperwiki.pdftoxml(u.read())
    soup = BeautifulSoup(x)
    book = soup.get_text().split('\n')

After a short parsing puzzle, you have every problem in the book in ASCII format.

## SGF

The [SGF](http://www.red-bean.com/sgf/) specification exists for any game: Backgammon, Twixt, Hex.  I don't remember the specification for [Go](http://www.red-bean.com/sgf/go.html) with a helpful discussion on [make-a-move vs add-a-stone](http://www.red-bean.com/sgf/ff5/m_vs_ax.htm)

All KGS games are publicly available.  Here are mine, [`mrcactu5`](http://www.gokgs.com/gameArchives.jsp?user=mrcactu5).

Here is problem 6 from the *Life and Death Encyclopedia*:

> (;AB[be][bf][cb][cc][cd][eb]AW[ab][ae][ba][bb][bc][bd]C[problem 6])

One line - it reads on any `sgf` editor.  Then we can join the games together:

> ((C[game A])(C[game B])(C[game C]))

In this way I printed all 900 problems from Vol 1.  