import download
import gui


link = ["https://www.youtube.com/watch?v=U-FEuCRxsC8", "https://www.youtube.com/watch?v=WIDoB3K-moI"]


def main():
    #for i in (len((gui.gui()))):
    temp = ""
    url = []
    tempgui = gui.gui()
    for i in range(len(tempgui)):
        if tempgui[i] != "\n":
            temp = temp + tempgui[i]
            url.append(temp)
            temp = ""
    url.append(temp)
    for y in range(len(url)):
        download.download(url[y])
                

    
        

    
    #test.Download(link)


if main() == __name__:
    main()