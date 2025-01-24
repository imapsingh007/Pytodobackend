from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to My Backend App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background: linear-gradient(to bottom, #1e3c72, #2a5298);
                color: #ffffff;
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            h1 {
                font-size: 3rem;
                margin: 0;
            }
            p {
                font-size: 1.5rem;
            }
            footer {
                margin-top: 20px;
                font-size: 1rem;
                color: #d9d9d9;
            }
            a {
                color: #00ffcc;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>Hello, This is the Backend Application!</h1>
        <p>FastAPI is running smoothly 🚀</p>
        <footer>
            <p>Visit <a href="https://fastapi.tiangolo.com" target="_blank">FastAPI Documentation</a></p>
        </footer>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
