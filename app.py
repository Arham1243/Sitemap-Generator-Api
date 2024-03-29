import streamlit as st
import asyncio
from pysitemap import crawler
from pysitemap.parsers.lxml_parser import Parser

files_to_ignore = [
    ".pdf", ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp", ".tif", ".tiff",
    ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".3gp","wp"
]

def generate_sitemap(url):
    root_url = url
    exclude_media_extensions = files_to_ignore
    exclude_urls = [ext for ext in exclude_media_extensions]

    asyncio.set_event_loop(asyncio.new_event_loop())  # Set up a new event loop for each thread

    crawler(
        root_url,
        out_file="sitemap.xml",
        exclude_urls=exclude_urls,
        http_request_options={"ssl": False},
        parser=Parser,
    )

def main():
    st.title("Sitemap Generator")

    url = st.text_input("Enter URL")
    if st.button("Generate Sitemap"):
        if not url:
            st.error("URL parameter is missing")
        else:
            generate_sitemap(url)
            with open("sitemap.xml", "r") as file:
                sitemap_content = file.read()
            st.success("Sitemap Generated Successfully!")
            st.write(sitemap_content)

if __name__ == "__main__":
    main()
