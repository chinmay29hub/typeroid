from click import option
import typer
from removebg import RemoveBg
import config
import time
import yfinance as yf
import pyfiglet
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import random
from pick import pick
from scihub import SciHub

app = typer.Typer()
sh = SciHub()


def removing_link(link):
    rmbg = RemoveBg(config.api_key, "error.log")
    rmbg.remove_background_from_img_url(
        link)


@app.command()
def remove_bg_link():
    typer.echo(pyfiglet.figlet_format("remove.link"))
    link = typer.prompt(
        "Enter the link of the image you want to remove the background from")
    typer.echo("\n")
    total = 0
    with typer.progressbar(removing_link(link), length=100, label="Removing Background") as progress:
        for remove in progress:
            time.sleep(0.01)
            total += 1
    typer.echo("\n")
    typer.secho(f"Done! Image downloaded in current directory", fg=typer.colors.BLUE,
                bg=typer.colors.YELLOW, bold=True)
    typer.echo("\n")


def removing_file(file):
    rmbg = RemoveBg(config.api_key, "error.log")
    rmbg.remove_background_from_img_file(file)


@app.command()
def remove_bg_file():
    typer.echo(pyfiglet.figlet_format("remove.file"))
    file = typer.prompt(
        "Enter the path of the file you want to remove the background from")
    typer.echo("\n")
    total = 0
    with typer.progressbar(removing_file(file), length=100, label="Removing Background") as progress:
        for remove in progress:
            time.sleep(0.01)
            total += 1
    typer.echo("\n")
    typer.secho(f"Done! Image downloaded in image path", fg=typer.colors.BLUE,
                bg=typer.colors.YELLOW, bold=True)
    typer.echo("\n")


@app.command()
def removebg():
    title = pyfiglet.figlet_format("remove.bg")
    options = ['Remove from a image file?',
               'Remove from a link?', 'Back', 'Exit']
    option, index = pick(options, title, indicator='=>', default_index=0)
    if option == 'Remove from a image file?':
        remove_bg_file()
    elif option == 'Remove from a link?':
        remove_bg_link()
    elif option == 'Back':
        menu()
    else:
        exit()


@app.command()
def repository():
    typer.echo(pyfiglet.figlet_format("Repo"))
    typer.secho(f"\nOpening Github Repository in your Default browser\n",
                fg=typer.colors.BLUE, bg=typer.colors.YELLOW, bold=True)
    typer.launch("https://github.com/chinmay29hub/typer")


def stock_loading(symbol, start, end):
    data = yf.download(symbol, start, end, progress=False)
    file_name = f"{symbol}-{start}-to-{end}.csv"
    data.to_csv(file_name)


@app.command()
def stock():
    typer.echo(pyfiglet.figlet_format("stock"))
    symbol = typer.prompt(
        "\nEnter Company Symbol | eg. AAPL, IBM, GOOGL, etc.")
    typer.echo("\n")
    start = typer.prompt("Enter start date | eg. 2020-01-01")
    typer.echo("\n")
    end = typer.prompt("Enter end date | eg. 2021-01-01")
    typer.echo("\n")
    total = 0
    with typer.progressbar(stock_loading(symbol, start, end), length=100, label="Downloading dataset") as progress:
        for loading in progress:
            time.sleep(0.01)
            total += 1
    typer.echo("\n")
    typer.secho(f"Done! Dataset downloaded in current directory", fg=typer.colors.BLUE,
                bg=typer.colors.YELLOW, bold=True)
    typer.echo("\n")


def word_cloud():
    df = pd.read_csv("dataset/android-games.csv")
    df.head()
    df.isna().sum()
    text = " ".join(cat.split()[1] for cat in df.category)
    word_cloud = WordCloud(width=1600, height=800, max_font_size=200,
                           collocations=False, background_color='black').generate(text)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


@app.command()
def wordcloud():
    typer.echo(pyfiglet.figlet_format("wordcloud"))
    total = 0
    with typer.progressbar(length=100, label="Creating wordcloud") as progress:
        for loading in progress:
            time.sleep(0.02)
            total += 1
    typer.echo("\n")
    typer.secho(f"Done! Here it is", fg=typer.colors.BLUE,
                bg=typer.colors.YELLOW, bold=True)
    word_cloud()
    typer.echo("\n")


def pass_generate(c):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()__+"
    all = lower + upper + numbers + symbols
    password = "".join(random.sample(all, c))
    typer.secho(
        f"\nYour generated password is : {password}", fg=typer.colors.GREEN, bold=True)


@app.command()
def password():
    typer.echo(pyfiglet.figlet_format("password"))
    lengthh = typer.prompt("\nEnter length of password | eg. 16 ")
    typer.echo("\n")
    c = int(lengthh)
    total = 0
    with typer.progressbar(length=100, label="Generating password") as progress:
        for loading in progress:
            time.sleep(0.015)
            total += 1
    typer.echo("\n")
    pass_generate(c)
    typer.echo("\n")
    typer.secho(f"Done!", fg=typer.colors.BLUE,
                bg=typer.colors.YELLOW, bold=True)


def download_file(link, file_name):
    result = sh.download(link, path=f'{file_name}.pdf')


@app.command()
def scihub():
    typer.echo(pyfiglet.figlet_format("sci-hub"))
    link = typer.prompt("Enter the link of the article you want to download ")
    typer.echo("\n")
    file_name = typer.prompt("Enter the filename to give to the pdf ")
    typer.echo("\n")
    total = 0
    with typer.progressbar(download_file(link, file_name), length=100, label="Downloading Paper") as progress:
        for loading in progress:
            time.sleep(0.01)
            total += 1
    typer.echo("\n")
    typer.secho(f"Done! PDF downloaded in current directory", fg=typer.colors.BLUE,
                bg=typer.colors.YELLOW, bold=True)
    typer.echo("\n")


@app.command()
def menu():
    title = pyfiglet.figlet_format("Typeroid")
    options = ['Generate Wordcloud', 'Generate Password', 'Fetch Stock Data',
               'Remove Background from image', 'Sci-Hub - Download any research paper', 'Open this Repository', 'Exit']
    option, index = pick(options, title, indicator='=>', default_index=0)
    if option == 'Generate Wordcloud':
        wordcloud()
    elif option == 'Generate Password':
        password()
    elif option == 'Fetch Stock Data':
        stock()
    elif option == 'Remove Background from image':
        removebg()
    elif option == 'Sci-Hub - Download any research paper':
        scihub()
    elif option == 'Open this Repository':
        repository()
    else:
        exit()


@app.callback()
def main(ctx: typer.Context):
    """
    please execute any one command.
    """
    typer.secho(
        f"\nAbout to execute command: {ctx.invoked_subcommand}\n", fg=typer.colors.GREEN)


if __name__ == "__main__":
    app()
