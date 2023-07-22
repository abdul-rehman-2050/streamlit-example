import streamlit as st
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root(name: str):
    return {"message": f"Hello, {name}! This is a simple Streamlit API."}

def main():
    st.title("Streamlit API Example")

if __name__ == "__main__":
    main()
