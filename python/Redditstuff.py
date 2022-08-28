
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser
import requests


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Create the widgets for our gui

        self.label1 = Label(self, text="Enter a subreddit:")
        self.label1.grid(row=0, column=0)

        self.entry1 = Entry(self)
        self.entry1.grid(row=0, column=1)

        self.button1 = Button(self, text="Submit", command=self.get_link)
        self.button1.grid(row=0, column=2)

    def get_link(self):  # This function gets the link from the subreddit and opens it in a browser window

        subreddit = str(self.entry1.get())  # Get the subreddit from the entry box and convert it to a string

        url = "https://www.reddit.com/r/" + subreddit + "/top/.json?sort=top&t=day&limit=10"  # Create the url to pull from reddit using the subreddit entered by user

        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}  # Set up headers so we can access reddit without getting blocked by their API

        response = requests.get(url, headers=headers)  # Send a request to reddit using our url and headers we set up earlier

        data = response.json()  # Convert the response into json format so we can parse through it easier later on in this function

        children = data['data']['children']  # Get all of the children of data which is where all of our links are stored in json format

        for child in children:  # Loop through each child in children and get its title and url then print them out to console for testing purposes only
            title = child['data']['title']
            link_url = child['data']['url']
            print("Title: " + title + "\nLink: " + link_url + "\n")

            webbrowser.open_new_tab(link_url)  # Open up a new tab with our link that was pulled from reddit using webbrowser module in python3 standard library


root = tk.Tk()
app = Application(master=root)
app.mainloop()