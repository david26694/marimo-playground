import marimo

__generated_with = "0.10.18"
app = marimo.App(width="medium")


@app.cell
def _():
    x = 2
    return (x,)


@app.cell
def _():
    y = 3
    return (y,)


@app.cell
def _(x, y):
    x + y
    return


@app.cell
def _():
    import marimo as mo

    a = mo.ui.slider(1, 10, 0.1)
    a

    return a, mo


@app.cell
def _(a, y):
    a.value + y
    return


@app.cell
def _(a):
    a
    return


@app.cell
def _():
    return


@app.cell
def _():
    import polars as pl
     
    df = pl.read_csv("https://calmcode.io/static/data/titanic.csv")

    return df, pl


@app.cell
def _(df, mo):
    dd_list = [str(e) for e in df["survived"].unique().to_list()]

    category = mo.ui.dropdown(dd_list)
    category
    return category, dd_list


@app.cell
def _(category, df, pl):
    out = df
    if category.value:
        out = df.filter(pl.col("survived") == int(category.value))
    out

    return (out,)


@app.cell
def _(z):
    z
    return


@app.cell
def _():
    z = 2
    return (z,)


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
